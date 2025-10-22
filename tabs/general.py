import dash_bootstrap_components as dbc 
from dash_bootstrap_components import Container,Row,Col 
from dash import dcc,html 
from components.general import *


state_picker = \
dbc.Card(
    dbc.CardBody([
        html.Label('Escolha Estado'),
        dcc.Dropdown(
            id='general-state-dropdown',
            options=[
                {'label': 'Acre', 'value': 'AC'},
                {'label': 'Alagoas', 'value': 'AL'},
                {'label': 'Amapá', 'value': 'AP'},
                {'label': 'Amazonas', 'value': 'AM'},
                {'label': 'Bahia', 'value': 'BA'},
                {'label': 'Ceará', 'value': 'CE'},
                {'label': 'Distrito Federal', 'value': 'DF'},
                {'label': 'Espírito Santo', 'value': 'ES'},
                {'label': 'Goiás', 'value': 'GO'},
                {'label': 'Maranhão', 'value': 'MA'},
                {'label': 'Mato Grosso', 'value': 'MT'},
                {'label': 'Mato Grosso do Sul', 'value': 'MS'},
                {'label': 'Minas Gerais', 'value': 'MG'},
                {'label': 'Pará', 'value': 'PA'},
                {'label': 'Paraíba', 'value': 'PB'},
                {'label': 'Paraná', 'value': 'PR'},
                {'label': 'Pernambuco', 'value': 'PE'},
                {'label': 'Piauí', 'value': 'PI'},
                {'label': 'Rio de Janeiro', 'value': 'RJ'},
                {'label': 'Rio Grande do Norte', 'value': 'RN'},
                {'label': 'Rio Grande do Sul', 'value': 'RS'},
                {'label': 'Rondônia', 'value': 'RO'},
                {'label': 'Roraima', 'value': 'RR'},
                {'label': 'Santa Catarina', 'value': 'SC'},
                {'label': 'São Paulo', 'value': 'SP'},
                {'label': 'Sergipe', 'value': 'SE'},
                {'label': 'Tocantins', 'value': 'TO'}
            ],
            value='SP',
            clearable=False,
            
        )
    ])
,style={'border':'none'})

year_picker = \
dbc.Card(
    dbc.CardBody([
        html.Label('Escolha o Ano'),
        dcc.Dropdown(
            id='general-year-dropdown',
            options=[{'label':str(x),'value':str(x)} for x in range(2017,2025)],
            value='2017',
            clearable=False,
        )
    ])
,style={'border':'none'})


filter = \
dbc.Card(
    dbc.CardBody([
        html.H2('Filtros'),
        year_picker,
        state_picker,
    ])
)

layout = Container([
    Row([
        Col(filter,width=3),
    ])
])