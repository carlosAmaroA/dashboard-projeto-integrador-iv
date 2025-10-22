import dash_bootstrap_components as dbc 
from dash import html, dcc 
from dash_bootstrap_components import Container,Row,Col
from components.types.filter import filter
from components.types.graphs import treemap_vehicles

layout = \
Container([
    Row([
        Col(filter,width=3),
        Col(dcc.Graph('treemap-vehicles',figure=treemap_vehicles(2017,'all')),width=9,style={'height': '100%'})
    ])
],fluid=True)
