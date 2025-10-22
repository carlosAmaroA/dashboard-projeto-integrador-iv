from dash import dcc,html 
import dash_bootstrap_components as dbc 
from dash_bootstrap_components import Row,Col,Container 
from components.geographic.graphs import *
from components.geographic.filters import *




layout = Container([
    Row([
        Col(filter,width=3),
        Col(dcc.Graph(figure=state_map(2017,'SP','choropleth'),id='state-map'))
    ],style={'height':'850px'})
])