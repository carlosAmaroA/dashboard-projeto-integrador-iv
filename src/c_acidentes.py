import pandas as pd 
from pathlib import Path 

datatran = pd.read_pickle(Path ('data','datatran.pkl'))
datatran = datatran.groupby('id').agg({
    'pesid':lambda s: s.isna().any(),
    'data':'first',
    'ilesos':'sum',
    'feridos_leves':'sum',
    'feridos_graves':'sum',
    'mortos':'sum',
    'latitude':'first',
    'longitude':'first',
    'uf':'first'
})

datatran.to_pickle(Path('data','acidentes.pkl'))