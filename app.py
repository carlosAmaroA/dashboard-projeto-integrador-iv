from dash import Dash, dcc, html
import pandas as pd
from tabs import overview, temporal, geographic, general, datainfo, causas # <-- Adicionado 'causas'
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from components.overview.graphs import *
from components.overview.callbacks import *

from components.temporal.graphs import *
from components.temporal.callbacks import *

from components.geographic.graphs import *
from components.geographic.callbacks import *

# Importe os novos componentes da aba de causas
from components.causas.graphs import bar_chart_causas,treemap_vehicles

app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG], suppress_callback_exceptions=True)

# Pagina principal que contém todos os tabs
app.layout = \
dbc.Container([
    html.Div([
        dbc.Tabs([
            dbc.Tab(label='Visão Geral', tab_id='overview'),
            dbc.Tab(label='Visão Temporal', tab_id='temporal'),
            dbc.Tab(label='Visão Geográfica', tab_id='geographic'),
            dbc.Tab(label='Causas e Fatores', tab_id='causas'),
            dbc.Tab(label='Sobre os Dados', tab_id='info'),
        ], id='tabs', active_tab='overview',
        style={
            'display': 'flex',
            'justifyContent': 'center' 
        },)
    ], className="mx-auto", style={"maxWidth": "1200px"},
    ),
    html.Div(id='tab-content', className='mt-4')
], fluid=True)


@app.callback(Output('tab-content', 'children'), Input('tabs', 'active_tab'))
def render_tab(active_tab):
    if active_tab == 'overview':
        return overview.layout
    elif active_tab == 'temporal':
        return temporal.layout
    elif active_tab == 'geographic':
        return geographic.layout
    elif active_tab == 'causas':  # <-- LÓGICA PARA RENDERIZAR A NOVA ABA
        return causas.layout
    elif active_tab == 'type':
        return general.layout
    elif active_tab == 'info':
        return datainfo.layout

# --- Callbacks da Aba Overview ---
@app.callback(Output('kpi-acident','children'),Input('overview-select-year','value'))
def kpi_acidentes_callback(year):
    return kpi_acidentes_update(int(year))
@app.callback(Output('kpi-feridos-leves','children'),Input('overview-select-year','value'))
def kpi_feridos_leves_callback(year):
    return kpi_feridos_levels_update(int(year))
@app.callback(Output('kpi-feridos-graves','children'),Input('overview-select-year','value'))
def kpi_acidentes_callback(year):
    return kpi_feridos_graves_update(int(year))
@app.callback(Output('kpi-mortos','children'),Input('overview-select-year','value'))
def kpi_acidentes_callback(year):
    return kpi_mortos_update(int(year))
@app.callback(Output('kpi-registros-imcompletos','children'),Input('overview-select-year','value'))
def kpi_registros_imcompletos_callback(year):
    return kpi_registros_incompletos_update(int(year))
@app.callback(Output('overview-choropleth','figure'),Input('overview-select-year','value'))
def choropleth_overview_callback(year):
    return overview_choropleth(int(year))
@app.callback(Output('overview-piechart-acidentes','figure'),Input('overview-select-year','value'))
def overview_piechart_acidentes_callback(year):
    return overview_piechart_acidentes(int(year))
@app.callback(Output('overview-piechart-values','figure'),Input('overview-select-year','value'))
def overview_piechart_values_callback(year):
    return overview_piechart_values(int(year))
@app.callback(Output('overview-bar-rank','figure'),Input('overview-select-year','value'))
def overview_bar_rank_callback(year):
    return overview_bar_rank(int(year))
@app.callback(Output('overview-stackedbar-month','figure'),Input('overview-select-year','value'))
def overview_stackedbar_month_callback(year):
    return overview_stackedbar_month(int(year))
@app.callback(Output('overview-histogram-days','figure'),Input('overview-select-year','value'))
def overview_histogram_days_callback(year):
    return overview_histogram_days(int(year))

# --- Callbacks da Aba Temporal ---
@app.callback(
    Output('radio-button-period', 'value'),
    Input('date-pick', 'start_date'),
    Input('date-pick', 'end_date'),
)
def radio_adjust(sdate,edate):
    t1 = pd.to_datetime(sdate)
    t2 = pd.to_datetime(edate)
    diff = (t2-t1).days
    if diff<2*365:
        return '7'
    return '365'
@app.callback(
    Output('temporal-line-day','figure'),
    Input('date-pick','start_date'),
    Input('date-pick','end_date'),
    Input('state-dropdown','value')
)
def temporal_line_callback(sdata,edata,state):
    return temporal_line(sdata,edata,state)
@app.callback(
    Output('temporal-line-media','figure'),
    Input('date-pick','start_date'),
    Input('date-pick','end_date'),
    Input('state-dropdown','value')
)
def temporal_line__media_callback(sdata,edata,state):
    return temporal_line_media(sdata,edata,state)
@app.callback(
    Output('tsa-additive','figure'),
    Input('date-pick','start_date'),
    Input('date-pick','end_date'),
    Input('state-dropdown','value'),
    Input('radio-button-period','value')
)
def temporal_tsa_callback(sdata,edata,state,period):
    return tsa_additive_lines(sdata,edata,state,int(period))
@app.callback(
    Output('temporal-heatmap','figure'),
    Input('date-pick','start_date'),
    Input('date-pick','end_date'),
    Input('state-dropdown','value'),
)
def temporal_heatmap_callback(sdata,edata,state):
    return temporal_heatmap(sdata,edata,state)

# --- Callbacks da Aba Geographic ---
@app.callback(
    Output('state-map','figure'),
    Input('geo-year-dropdown','value'),
    Input('geo-state-dropdown','value'),
    Input('geo-map-dropdown','value')
)
def state_map_callback(year,state,maptype):
    return state_map(int(year),state,maptype)

# --- CALLBACK DA NOVA ABA DE CAUSAS ---
@app.callback(
    Output('causas-bar-chart', 'figure'),
    Input('types-year-dropdown', 'value'),
    Input('types-state-dropdown', 'value')
)
def update_causas_chart(year,state):
    return bar_chart_causas(int(year),state)

@app.callback(
    Output('treemap-vehicles', 'figure'),
    Input('types-year-dropdown', 'value'),
    Input('types-state-dropdown', 'value')
)
def update_causas_chart(year,state):
    return treemap_vehicles(int(year),state)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8050)
