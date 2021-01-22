"""Instantiate a Dash app."""
import numpy as np
import pandas as pd
import dash
import dash_table
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import plotly.express as px
from .data import create_dataframe
from .layout import html_layout
from .. import rf_model



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
    feat_importance_fig = px.bar(feature_importance,
                                 labels={'value': 'Importance', 'index': 'Features'})
    feat_importance_fig.layout.update(showlegend=False)

    # Create age/feature scatter plot
    x_graph = df[df['class'] == True]['Age'].value_counts().index
    y_graph = df[df['class'] == True]['Age'].value_counts().values
    age_scatter_fig = go.Figure()
    age_scatter_fig.add_trace(go.Scatter(x=x_graph, y=y_graph,
                                         mode='markers',
                                         name='Diabetes',
                                         marker={"size": 12, "color": 'blue'}))
    x_graphb = df[df['Polyuria'] == True]['Age'].value_counts().index
    y_graphb = df[df['Polyuria'] == True]['Age'].value_counts().values
    age_scatter_fig.add_trace(go.Scatter(x=x_graphb, y=y_graphb,
                                         mode='markers',
                                         name='Polyuria',
                                         marker={"size": 12, "color": 'MediumPurple'}))
    age_scatter_fig.update_layout(
        xaxis_title="Age",
        yaxis_title="Number of Patients",
        legend_title="Condition",
        )

    # Custom HTML layout
    dash_app.index_string = html_layout

    # Create Layout
    dash_app.layout = html.Div(
        children=[
            html.Br(),
            html.H5(children="Feature Heatmap", className="lh-1"),
            dcc.Graph(figure=feature_heatmap_fig),
            html.Br(),
            html.H5(children="Machine Learning Feature Importance", className="lh-1"),
            dcc.Graph(figure=feat_importance_fig),
            html.Br(),
            html.H5(children="Age Distribution", className="lh-1"),
            dcc.Graph(figure=age_scatter_fig),
            html.Br(),
            html.H5(children="Dataset Browser", className="lh-1"),
            html.Br(),
            html.Br(),
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
