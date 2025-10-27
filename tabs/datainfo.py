import dash_bootstrap_components as dbc
from dash import html

layout = dbc.Container([

    dbc.Row([
        dbc.Col(
            html.H2("Informações sobre o Dataset – DataTran 2017–2024", className="text-center"),
            width=12
        )
    ], className="mb-5"),

    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H4("Período do Dataset", className="card-title"),
                    html.P("2017 – 2024", className="card-text")
                ]),
                className="mb-4"
            ),
            width=12
        )
    ], className="mb-3 justify-content-center"),

    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H4("Origem do Dataset", className="card-title"),
                    html.P(
                        "Dados abertos da Polícia Rodoviária Federal – registros de acidentes de trânsito agrupados por pessoa, incluindo todas as causas e tipos de acidentes.",
                        className="card-text"
                    )
                ]),
                className="mb-4"
            ),
            width=12
        )
    ], className="mb-3 justify-content-center"),

    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H4("Formato", className="card-title"),
                    html.P("Arquivo CSV contendo colunas detalhadas sobre o acidente, condutor, veículo, local, data e fatores contribuintes.", className="card-text")
                ]),
                className="mb-4"
            ),
            width=12
        )
    ], className="mb-3 justify-content-center"),

    dbc.Row([
        dbc.Col([
            html.H4("Descrição", className="text-center"),
            html.P(
                "Este conjunto de dados registra acidentes de trânsito envolvendo pessoas, abrangendo todas as causas e tipos de acidentes. "
                "Inclui informações detalhadas sobre o condutor (idade, sexo, habilitação), veículo (tipo, categoria, estado de conservação), "
                "localização do acidente (latitude, longitude, município, estado), fatores contribuintes (condutor, veículo, ambiente) e resultado do incidente "
                "(ferimentos, mortes, envolvimento de terceiros). É ideal para análises estatísticas, visualizações geográficas, séries temporais e identificação de padrões de acidentes no Brasil.",
                className="text-center"
            )
        ], width=12)
    ], className="mb-4 justify-content-center"),

    dbc.Row([
        dbc.Col([
            html.H4("Observações / Limitações", className="text-center"),
            html.Ul([
                html.Li("Alguns registros podem estar incompletos ou conter inconsistências."),
                html.Li("Diferenças na notificação entre estados podem afetar comparações."),
                html.Li("Coordenadas ou informações de localização podem ser aproximadas."),
                html.Li("Algumas variáveis podem ter nomes padronizados apenas a partir de 2017."),
                html.Li("Dados sensíveis ou pessoais são anonimizados para proteger a privacidade.")
            ], className="text-center", style={"list-style-type": "none", "padding-left": "0"})
        ], width=12)
    ], className="mb-4 justify-content-center")

], fluid=True, className="p-4")