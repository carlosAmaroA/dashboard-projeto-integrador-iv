from pathlib import Path 
import pandas as pd 
import geopandas as gpd 
from shapely.geometry import Point
import plotly.express as px
import json
import numpy as np

coords = {
    "AC": [4.5, {"lat": -9.0238, "lon": -70.8120}],
    "AL": [6.2, {"lat": -9.5713, "lon": -36.7820}],
    "AP": [5.0, {"lat": 1.4142, "lon": -51.6022}],
    "AM": [3.5, {"lat": -3.4168, "lon": -65.8561}],
    "BA": [5.0, {"lat": -12.5797, "lon": -41.7007}],
    "CE": [5.8, {"lat": -5.4984, "lon": -39.3206}],
    "DF": [7.2, {"lat": -15.8267, "lon": -47.9218}],
    "ES": [6.2, {"lat": -19.1834, "lon": -40.3089}],
    "GO": [5.5, {"lat": -15.8270, "lon": -49.8362}],
    "MA": [5.0, {"lat": -4.9609, "lon": -45.2744}],
    "MT": [4.0, {"lat": -12.6819, "lon": -55.4230}],
    "MS": [5.0, {"lat": -20.7722, "lon": -54.7852}],
    "MG": [5.0, {"lat": -18.5122, "lon": -44.5550}],
    "PA": [4.5, {"lat": -3.7970, "lon": -52.4780}],
    "PB": [6.0, {"lat": -7.2399, "lon": -36.7819}],
    "PR": [5.2, {"lat": -25.2521, "lon": -52.0215}],
    "PE": [5.8, {"lat": -8.8137, "lon": -36.9541}],
    "PI": [5.0, {"lat": -7.7183, "lon": -42.7289}],
    "RJ": [6.5, {"lat": -22.9068, "lon": -43.1729}],
    "RN": [6.2, {"lat": -5.4026, "lon": -36.9541}],
    "RS": [5.0, {"lat": -30.0346, "lon": -53.2309}],
    "RO": [5.0, {"lat": -10.8333, "lon": -63.3333}],
    "RR": [4.8, {"lat": 2.7376, "lon": -62.0751}],
    "SC": [5.5, {"lat": -27.2423, "lon": -50.2189}],
    "SP": [6.0, {"lat": -22.3519, "lon": -48.2294}],
    "SE": [6.5, {"lat": -10.5741, "lon": -37.3857}],
    "TO": [5.0, {"lat": -10.1753, "lon": -48.2982}]
}


def data_filter(year,state,data='acidentes.pkl'):
    data = pd.read_pickle(Path('data',data))
    data = data[data['uf'] == state]
    data = data[data['data'].dt.year == year]
    data = data[(data['latitude'].between(-90,90)) & (data['longitude'].between(-180,180))]
    return data

def state_map(year,state,maptype):
    data = data_filter(year,state)
    geomap = gpd.read_file(Path('assets','geojson','microregions',f'{state.lower()}.json'))
    geometry = [Point(xy) for xy in zip(data['longitude'],data['latitude'])]
    geodata = gpd.GeoDataFrame(data,geometry=geometry,crs='EPSG:4674')
    result = gpd.sjoin(geodata,geomap,how='left',predicate='within')
    result = result.groupby('codarea',as_index=False).size()
    codareas = pd.DataFrame({'codarea':geomap['codarea'].tolist()})
    result = codareas.merge(result,on='codarea',how='left')
    result['size'] = result['size'].fillna(0)

    if maptype == 'choropleth':
        
        fig = px.choropleth_mapbox(
            result,
            geojson=geomap,
            locations='codarea',
            featureidkey = 'properties.codarea',
            color='size',
            mapbox_style='carto-darkmatter',
            center=coords[state][1],
            zoom=coords[state][0],
            opacity=0.6,
            color_continuous_scale="Blues"
        )

        fig.update_layout(
            paper_bgcolor = '#060606',
        )

        return fig
    elif maptype == 'heatmap':
        fig = px.density_mapbox(
            data, 
            lat='latitude',
            lon='longitude',
            radius=2, 
            center=coords[state][1],
            zoom=coords[state][0],
            mapbox_style="carto-darkmatter",
            color_continuous_scale="Blues"
        )

        fig.update_layout(
            mapbox_layers=[
                {
                    "sourcetype": "geojson",
                    "source": json.loads(geomap.to_json()),
                    "type": "line",
                    "color": "white",
                    "line": {"width": 1}
                }
            ],
            paper_bgcolor = '#060606',
        )
        return fig