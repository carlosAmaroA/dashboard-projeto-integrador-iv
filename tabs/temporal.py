from dash import dcc,html 
from dash_bootstrap_components import Row,Col,Container
import dash_bootstrap_components as dbc

from components.temporal.filters import *
from components.temporal.graphs import *

layout = Container([
    Row([
        Col(filters,width = 3),
        Col(dcc.Graph(figure=tsa_additive_lines('2017-01-01','2024-12-31','all',365),id='tsa-additive'),width=9)
    ],style={'height':'100%'}),
    Row([
        Col(dcc.Graph(figure=temporal_line('2017-01-01','2024-12-31','all'),id='temporal-line-day'),width=6),
        Col(dcc.Graph(figure=temporal_line_media('2017-01-01','2024-12-31','all'),id='temporal-line-media'),width=6)
    ],style={'height':'300px'}),
    Row([
        Col(dcc.Graph(figure=temporal_heatmap('2017-01-01','2024-12-31','all'),id='temporal-heatmap'),width=12)
    ])
],fluid=True)