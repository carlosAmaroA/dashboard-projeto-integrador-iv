import plotly.express as px 
from pathlib import Path 
import pandas as pd 


def data_filter(year,state,data='acidentes_full.pkl'):
    data = pd.read_pickle(Path('data',data))
    data = data[data['uf'] == state]
    data = data[data['data'].dt.year == year]
    return data


def stacked_bar100(year,state):
    data = data_filter(year,state)