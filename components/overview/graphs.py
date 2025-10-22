import pandas as pd 
import plotly.express as px 
from pathlib import Path 
import geopandas as gpd
from shapely.geometry import Point
import numpy as np

def overview_choropleth(year):
    geo = gpd.read_file(Path('assets','geojson','br.json'))
    data = pd.read_pickle(Path('data','agg_points.pkl'))
    data = data[data['year'] == year]
    geometry = [Point(xy) for xy in zip(data['lon'],data['lat'])]
    gdata = gpd.GeoDataFrame(data,geometry=geometry,crs='EPSG:4326')
    geo = geo.set_crs('EPSG:4326')
    gdata = gpd.sjoin(gdata,geo,how='right',predicate='within')
    gdata = gdata.groupby('id').agg({'points':'sum'}).reset_index()
    fig = px.choropleth_mapbox(
        gdata,
        geojson=geo,
        locations='id',
        featureidkey='properties.id',
        color='points',
        color_continuous_scale='Blues',
        mapbox_style='carto-darkmatter', 
        zoom=3.2,
        center={"lat": -14.2, "lon": -51.9},
        labels={'points':'Acidentes'},
        range_color = (0,10000)
    )
    fig.update_layout(
        paper_bgcolor='#060606',
        margin={'l':0},
        font = dict(
            color='white'
        )
    )
    return fig

def overview_piechart_acidentes(year):
    data = pd.read_pickle(Path('data','acidentes.pkl'))
    data = data[data['data'].dt.year == year] 
    data['fatal'] = data['mortos'].apply(lambda x: 1 if x>0 else 0)
    labels = ['Fatais','Não Fatais']
    values = [(data['fatal']==1).sum(),(data['fatal']==0).sum()]

    df = {"labels": labels, "values": values}
    fig = px.pie(
        df,
        names='labels',
        values='values',
        hole=0.4,
        color_discrete_sequence=['#1f77b4', 'white']
    )
    fig.update_layout(
        paper_bgcolor='#060606',
        margin = {'t':0,'b':0,'r':0,'l':0},
        font=dict(
            color='white'
        ),
        legend = dict(
            x=0.9,
            y=0.9
        )
    )
    return fig

def overview_piechart_values(year):
    data = pd.read_pickle(Path('data','acidentes.pkl'))
    data = data[data['data'].dt.year==year]
    data = data[data['pesid'] == 0] 
    labels = ['ilesos','feridos leves','feridos graves','mortos']
    values = [data['ilesos'].sum(),data['feridos_leves'].sum(),data['feridos_graves'].sum(),data['mortos'].sum()]
    df = {'labels':labels,'values':values}

    fig = px.pie(
        df,
        names = 'labels',
        values = 'values',
        hole=0.4,
        color_discrete_sequence=['#1f3b73', '#3a69ad', '#7ea6e0', '#ffffff']
    )
    fig.update_layout(
        paper_bgcolor='#060606',
        margin = {'t':0,'b':0,'r':0,'l':0},
        font=dict(
            color='white'
        ),
        legend = dict(
            x=0.9,
            y=0.9
        )
    )
    return fig

def overview_bar_rank(year):
    data = pd.read_pickle(Path('data','acidentes.pkl'))
    data = data[data['data'].dt.year == year]
    data = data[data['pesid'] == 0] 
    df = data.groupby('uf').size().reset_index(name='count')
    df = df.sort_values('count')
    df = df.tail(10)

    fig = px.bar(
        df,
        x='count',
        y='uf',
        title='Top 10 Estados',
        color='count',
        color_continuous_scale=['#1f3b73', '#7ea6e0'],
        orientation='h'
    )

    fig.update_layout(
        paper_bgcolor = '#060606',
        plot_bgcolor = '#060606',
        font = dict(
            color = 'white'
        ),
        margin = {'t':25,'b':0,'l':0,'r':0}
    )
    return fig

def overview_stackedbar_month(year):
    data = pd.read_pickle(Path('data','acidentes.pkl'))
    data = data[data['data'].dt.year == year]
    data = data[data['pesid'] == 0] 
    data['month'] = data['data'].dt.strftime('%b')

    df = data.melt(
        id_vars = 'month',
        value_vars = ['ilesos','feridos_leves','feridos_graves','mortos'],
        var_name = 'category',
        value_name = 'qtd'
    )

    df = df.groupby(['month','category'],as_index=False)['qtd'].sum()

    fig = px.bar(
        df,
        x='month',
        y='qtd',
        color='category',
        color_discrete_sequence=['#1f3b73','#3a69ad','#7ea6e0','white'],
        category_orders={'category': ['ilesos', 'feridos_leves', 'feridos_graves', 'mortos']}
    )
    fig.update_layout(
        paper_bgcolor = '#060606',
        plot_bgcolor = '#060606',
        xaxis=dict(categoryorder='array', categoryarray=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']),
        font = dict(
            color='white'
        )
    )

    return fig

def overview_histogram_days(year):
    data = pd.read_pickle(Path('data','acidentes.pkl'))
    data = data[data['data'].dt.year == year]
    data['day'] = data['data'].dt.date
    data = data.groupby('day',as_index=False)['data'].count()
    data['day'] = pd.to_datetime(data['day'])
    data['weekday'] = data['day'].dt.day_name()
    fig = px.bar(
        data,
        x='day',
        y='data',
        color = 'weekday',
        color_discrete_sequence = ['#85C1E9', '#5DADE2', '#3498DB', '#2E86C1', '#1B4F72', '#154360', '#0B3D91'],
        category_orders = {'weekday': ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']},

    )
    
    fig.update_layout(
        paper_bgcolor = '#060606',
        plot_bgcolor = '#060606',
        yaxis_title = 'Acidentes',
        margin = {'t':0,'r':0},
        font = dict(
            color = 'white'
        )
    )
   
    fig.update_traces(
        marker_line_width = 0,
    )
    return fig

def overview_pie_data(year):
    data = pd.read_pickle(Path('data','acidentes.pkl'))
    data = data[data['data'].dt.year == year]
    i = data['pesid'].sum()
    labels = ['Completos','Incompletos']
    values = [len(data)-i,i]

    fig = px.pie(
        names = labels,
        values = values,
        color_discrete_sequence=['#1f3b73', '#ffffff'],
        hole=0.4,
    )
    
    fig.update_layout(
        paper_bgcolor = '#060606',
        margin = {'t':0,'b':0,'r':0,'l':0},
        font = dict(
            color='white'
        )
    )

    return fig