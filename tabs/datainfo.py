import dash_bootstrap_components as dbc
from dash_bootstrap_components import Row,Col,Container
from dash import html

layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H2("Dataset Info – DataTran 2017–2024"), width=12)
    ], className="mb-4"),

    # Card com informações gerais
    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H4("Período do Dataset", className="card-title"),
                    html.P("2017 – 2024", className="card-text")
                ])
            ),
            width=6
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H4("Origem do Dataset", className="card-title"),
                    html.P("Documento CSV de Acidentes   (Agrupados por pessoa – Todas as causas e tipos de acidentes)", className="card-text")
                ])
            ),
            width=6
        )
    ], className="mb-4"),

    # Descrição
    dbc.Row([
        dbc.Col([
            html.H4("Descrição"),
            html.P("Registro de acidentes de trânsito envolvendo pessoas, abrangendo todas as causas e tipos de acidentes.")
        ])
    ], className="mb-4"),

    # Observações / limitações
    dbc.Row([
        dbc.Col([
            html.H4("Observações / Limitações"),
            html.Ul([
                html.Li("Alguns registros podem estar incompletos."),
                html.Li("Diferenças na notificação entre estados podem afetar comparações."),
                html.Li("Coordenadas ou outras informações podem ser aproximadas.")
            ])
        ])
    ])
], fluid=True, className="p-4")