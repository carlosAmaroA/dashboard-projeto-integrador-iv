import pandas as pd 
from pathlib import Path 
import plotly.express as px 
from statsmodels.tsa.seasonal import seasonal_decompose
import numpy as np

def data_filter(sdate,edate,state,data='acidentes.pkl'):
    data = pd.read_pickle(Path('data',data))
    if state != 'all':
        data = data[data['uf'] == state]
    data = data[data['data'].between(sdate,edate)]
    return data

def temporal_line(sdate,edate,state):
    data = data_filter(sdate,edate,state)
    data['day'] = data['data'].dt.date
    data = data.groupby('day',as_index=False).size()
    
    fig = px.line(
        data,
        x='day',
        y='size',
        title = 'Acidentes por Dia',
        color_discrete_sequence = ['#4da6ff'],
    )

    fig.update_layout(
        paper_bgcolor = '#060606',
        plot_bgcolor = '#060606',
        margin = {'l':0,'r':0,'b':0},
        font = dict(
            color='white'
        )
    )

    return fig

def temporal_line_media(sdate,edate,state):
    data = data_filter(sdate,edate,state)
    data['day'] = data['data'].dt.date
    data = data.groupby('day',as_index=False).size()
    data['media_movel'] = data['size'].rolling(window=7,min_periods=1).mean()
    
    fig = px.line(
        data,
        x='day',
        y='media_movel',
        title = 'Acidentes por Dia - Media movel 7 dias',
        color_discrete_sequence = ['#4da6ff'],
    )

    fig.update_layout(
        paper_bgcolor = '#060606',
        plot_bgcolor = '#060606',
        margin = {'l':0,'r':0,'b':0},
        font = dict(
            color='white'
        )
    )

    return fig

def tsa_additive_lines(sdate,edate,state,period):
    data = data_filter(sdate,edate,state)
    data['day'] = data['data'].dt.date
    data = data.groupby('day').size()
    diff = (pd.to_datetime(edate)-pd.to_datetime(sdate)).days

    if diff>=14 or (diff<=(2*365) and period==365):
        ts = seasonal_decompose(data,model='additive',period=period)
        plot_data = pd.DataFrame({
            "data": data.index,
            "trend": ts.trend,
            "seasonal": ts.seasonal,
            "resid": ts.resid
        })
    else:
        plot_data = pd.DataFrame({"data": [], "trend": [], "seasonal": [], "resid": []})
    
    fig = px.line(
        plot_data,
        x='data',
        y=['trend','seasonal','resid'],
        title='Decomposição aditiva'
    )

    fig.update_layout(
        paper_bgcolor = '#060606',
        plot_bgcolor = '#060606',
        margin = dict(b=0,l=0,r=0),
        font = dict(
            color = 'white'
        )
    )

    fig.update_traces(selector=dict(name="resid"), visible="legendonly")

    return fig
    

def temporal_heatmap(sdate,edate,state):
    data = data_filter(sdate,edate,state)
    data['hour'] = data['data'].dt.hour
    data['day'] = data['data'].dt.date
    heatmap_data = data.pivot_table(
        index='hour',
        columns='day',
        values='data',
        aggfunc='count',
        fill_value=0
    )

    fig=px.imshow(
        heatmap_data,
        origin='lower',
        color_continuous_scale='Viridis',
        labels=dict(
            x='Data',
            y='Hora'
        ),
        zmax=np.percentile(heatmap_data.values, 95)
    )

    fig.update_layout(
        paper_bgcolor = '#060606',
        plot_bgcolor = '#060606',
        font = dict(
            color='white'
        )
    )

    return fig