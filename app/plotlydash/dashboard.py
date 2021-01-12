"""Instantiate a Dash app."""
import numpy as np
import pandas as pd
import dash
import dash_table
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly.io as pio
import plotly.express as px
from .data import create_dataframe
from .layout import html_layout
from .. import rf_model, dt_model



def init_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/'
    )

    # Load DataFrame
    df = create_dataframe()


    # Create confusion matrix
    feature_heatmap_fig = px.imshow(df.corr(), color_continuous_scale=px.colors.sequential.ice)

    # Create feature importance bar chart
    feature_importance = pd.Series(rf_model.feature_importances_*100,
                                   index=df.columns[:-1]).sort_values(ascending=False)
    feat_import_fig = px.bar(feature_importance,
                             labels={'value': 'Importance', 'index': 'Features'})
    feat_import_fig.layout.update(showlegend=False)

    # Create age/feature scatter plot
    x_graph = df[df['class'] == True]['Age'].value_counts().index
    x_graph2 = x_graph
    y_graph = df[df['class'] == True]['Age'].value_counts().values
    fig_compare = go.Figure()
    fig_compare.add_trace(go.Scatter(x=x_graph, y=y_graph,
                             mode='markers',
                             name='Diabetes'))
    x_graphb = df[df['Polyuria'] == True]['Age'].value_counts().index
    y_graphb = df[df['Polyuria'] == True]['Age'].value_counts().values
    fig_compare.add_trace(go.Scatter(x=x_graphb, y=y_graphb,
                             mode='markers',
                             name='Polyuria'))

    # Custom HTML layout
    dash_app.index_string = html_layout

    # Create Layout
    dash_app.layout = html.Div(
        children=[
            dcc.Graph(figure=feature_heatmap_fig),
            dcc.Graph(figure=feat_import_fig),
            dcc.Graph(figure=fig_compare),
            create_data_table(df),
        ],
        id='dash-container'
    )
    return dash_app.server


def create_data_table(df):
    """Create Dash datatable from Pandas DataFrame."""
    table = dash_table.DataTable(
        id='database-table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        style_table={'overflowX': 'scroll'},
        sort_action="native",
        sort_mode='native',
        page_size=10
    )
    return table
