import dash_bootstrap_components as dbc 
from dash import html,dcc

date_picker = \
dbc.Card(
    dbc.CardBody([
        html.Label('Escolha Intervalo'),
        dcc.DatePickerRange(
            id='date-pick',
            start_date = '2017-01-01',
            end_date = '2024-12-31',
            display_format = 'DD/MM/YY',
            min_date_allowed = '2017-01-01',
            max_date_allowed = '2024-12-31',
        )
    ])
,style={'border':'none'})

state_picker = \
dbc.Card(
    dbc.CardBody([
        html.Label('Escolha Estado'),
        dcc.Dropdown(
            id='state-dropdown',
            options=[
                {'label':'Todos','value':'all'},
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
            value='all'
            
        )
    ])
,style={'border':'none'})

radio_button = \
dbc.Card(
    dbc.CardBody([
        html.Label('Period: '),
        dbc.RadioItems(
            id='radio-button-period',
            options=[
                {'label':'7','value':'7'},
                {'label':'365','value':'365'},
            ],
            value = '365',
            inline=True,
        )
    ])
)

filters = \
dbc.Card(
    dbc.CardBody([
        html.H2('Filtros'),
        date_picker,
        state_picker,
        radio_button
    ])
)
