import pandas as pd 
from pathlib import Path 

def kpi_acidentes_update(year):
    data = pd.read_pickle(Path('data','acidentes.pkl'))
    data = data[data['data'].dt.year == year]
    data = data[data['pesid'] == 0] 
    return len(data)

def kpi_feridos_levels_update(year):
    data = pd.read_pickle(Path('data','acidentes.pkl'))
    data = data[data['data'].dt.year == year]
    data = data[data['pesid'] == 0] 
    return data['feridos_leves'].sum()

def kpi_feridos_graves_update(year):
    data = pd.read_pickle(Path('data','acidentes.pkl'))
    data = data[data['data'].dt.year == year]
    data = data[data['pesid'] == 0] 
    return data['feridos_graves'].sum()

def kpi_mortos_update(year):
    data = pd.read_pickle(Path('data','acidentes.pkl'))
    data = data[data['data'].dt.year == year]
    data = data[data['pesid'] == 0] 
    return data['mortos'].sum()

def kpi_registros_incompletos_update(year):
    data = pd.read_pickle(Path('data','acidentes.pkl'))
    data = data[data['data'].dt.year == year]
    return data['pesid'].sum()
