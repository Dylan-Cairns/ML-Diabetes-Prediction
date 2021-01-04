"""Instantiate a Dash app."""
import numpy as np
import pandas as pd
import dash
import dash_table
import dash_html_components as html
import dash_core_components as dcc
from .data import create_dataframe, create_dataframe_dylon
from .layout import html_layout


def init_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/'
    )

    # Load DataFrame
    df = create_dataframe()
    df_dylon = create_dataframe_dylon()

    # Custom HTML layout
    dash_app.index_string = html_layout

    # Create Layout
    dash_app.layout = html.Div(
        children=[
            dcc.Graph(
                id='histogram-graph',
                figure={
                    'data': [{
                        'x': df['complaint_type'],
                        'text': df['complaint_type'],
                        'customdata': df['key'],
                        'name': '311 Calls by region.',
                        'type': 'histogram'
                    }],
                    'layout': {
                        'title': 'NYC 311 Calls category.',
                        'height': 500,
                        'padding': 150
                    },
                },
            ),
            create_data_table(df_dylon),
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
