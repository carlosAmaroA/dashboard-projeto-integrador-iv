import pandas as pd 
from pathlib import Path

data = pd.read_pickle(Path('data','acidentes.pkl'))
data = data[(data['latitude'].between(-90,90)) & (data['longitude'].between(-180,180))]
grid = 0.025
result = []

for year in range(2017,2025):
    ydata = data[data['data'].dt.year == year].copy()

    ydata['lat'] = (ydata['latitude']//grid)*grid 
    ydata['lon'] = (ydata['longitude']//grid)*grid 

    ydata = ydata.groupby(['lat','lon']).size().reset_index(name='points')

    ydata['lat'] = ydata['lat'] + grid/2
    ydata['lon'] = ydata['lon'] + grid/2
    ydata['year'] = year 
    result.append(ydata)

result = pd.concat(result)

result.to_pickle(Path('data','agg_points.pkl'))