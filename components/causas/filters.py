from dash import dcc, html
import dash_bootstrap_components as dbc

# Lista de anos para o filtro
anos = list(range(2017, 2025))

# Cria o card de filtros
filters = dbc.Card(
    dbc.CardBody([
        html.H5("Filtros", className="card-title"),
        html.Hr(),
        html.P("Selecione o Ano:", className="card-text"),
        dcc.Dropdown(
            id='causas-select-year',
            options=[{'label': ano, 'value': ano} for ano in anos],
            value=2024, # Ano padrão
            clearable=False
        ),
    ]),
    className="mt-3"
)
