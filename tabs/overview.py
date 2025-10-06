from components.overview.filters import *
from components.overview.graphs import *
from dash import dcc,html 
import dash_bootstrap_components as dbc
from dash_bootstrap_components import Row,Col,Container


kpi_acidentes = dbc.Card(
    dbc.CardBody([
        html.H6('Acidentes',className='card-title'),
        html.H4('50',className='card-text',id='kpi-acident')
    ])
,className='h-80')

kpi_feridos_leves = dbc.Card(
    dbc.CardBody([
        html.H6('Feridos Leves',className='card-title'),
        html.H4('50',className='card-text',id='kpi-feridos-leves')
    ])
,className='h-80')
kpi_feridos_graves = dbc.Card(
    dbc.CardBody([
        html.H6('Feridos Graves',className='card-title'),
        html.H4('50',className='card-text',id='kpi-feridos-graves')
    ])
,className='h-80')
kpi_mortos = dbc.Card(
    dbc.CardBody([
        html.H6('Mortos',className='card-title'),
        html.H4('50',className='card-text',id='kpi-mortos')
    ])
,className='h-80')
kpi_dados_faltando = dbc.Card(
    dbc.CardBody([
        html.H6('Registros Incompletos',className='card-title'),
        html.H4('50',className='card-text',id='kpi-registros-imcompletos')
    ])
,className='h-80')
layout = \
Container([
    Row([
        Col(dropdown,width=2),
        Col(kpi_acidentes,width=2),
        Col(kpi_feridos_leves,width=2),
        Col(kpi_feridos_graves,width=2),
        Col(kpi_mortos,width=2),
        Col(kpi_dados_faltando,width=2)
    ],className='g-3'),
    Row([
        Col(dcc.Graph(figure=overview_choropleth(2017),id='overview-choropleth'),width=5,style={'height':'750px'}),
        Col([
            Row([
                Col(dcc.Graph(figure=overview_piechart_acidentes(2017),id='overview-piechart-acidentes'),width=4,style={'height':'350px'}),
                Col(dcc.Graph(figure=overview_piechart_values(2017),id='overview-piechart-values'),width=4,style={'height':'350px'}),
                Col(dcc.Graph(figure=overview_bar_rank(2017),id='overview-bar-rank'),width=4,style={'height':'350px'}),
            ]),
            Row([
                Col(dcc.Graph(figure=overview_stackedbar_month(2017),id='overview-stackedbar-month'),width=12,style={'height':'350px'}),
            ])
        ],width=7),
    Row([
        Col(dcc.Graph(figure=overview_histogram_days(2017),id='overview-histogram-days'),width=9),
        Col(dcc.Graph(figure=overview_pie_data(2017),id='overview-pie-data'),width = 3)
    ])
    ])
],fluid=True)
