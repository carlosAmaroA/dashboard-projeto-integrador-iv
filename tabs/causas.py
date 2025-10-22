from dash import dcc, html
import dash_bootstrap_components as dbc
from components.causas.filters import filters
from components.causas.graphs import bar_chart_causas

# Define o layout da aba
layout = dbc.Container([
    dbc.Row([
        # Coluna dos Filtros
        dbc.Col([
            filters # Importa o card de filtros
        ], width=12, lg=3),
        
        # Coluna do Gráfico
        dbc.Col([
            dcc.Graph(
                id='causas-bar-chart',
                figure=bar_chart_causas(2024) # Carrega o gráfico com um valor padrão
            )
        ], width=12, lg=9)
    ], className="mt-4")
], fluid=True)
