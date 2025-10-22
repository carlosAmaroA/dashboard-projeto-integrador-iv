import plotly.express as px 
import pandas as pd 
import numpy as np 
from pathlib import Path

def data_filter(year,state):
    data = pd.read_pickle(Path('data','acidentes_full.pkl'))
    data = data[data['data'].dt.year == year]
    if state != 'all':
        data = data[data['uf'] == state]
    return data

def treemap_vehicles(year,state):
    data = data_filter(year,state)
    data = data.explode('tipo_veiculo')
    data = data.explode('causa_principal')
    data['gravidade'] = data.apply(
    lambda row: 'fatal' if row['mortos'] > 0 else ('grave' if row['feridos_graves'] > 0 else 'leve'),
    axis=1)
    data = data.groupby(['tipo_veiculo','gravidade','causa_principal'],as_index=False).count()[['tipo_veiculo','gravidade','causa_principal','br']]    
    df = data
    df['nivel'] = df['gravidade']+'-'+df['causa_principal']

    fig = px.treemap(
        df,
        path=['tipo_veiculo', 'gravidade','causa_principal'],  
        values='br',                  
        title='Acidentes por Tipo de Veículo e Gravidade',
    )

    fig.update_layout(
        paper_bgcolor='#060606',
        font = dict(
            color='white'
        )
    )

    return fig