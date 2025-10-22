import pandas as pd 
import numpy as np
from pathlib import Path   

data = pd.read_pickle(Path('..','data','datatran.pkl'))
dados = data.copy()
dados['causa_principal'] = dados['causa_principal'].astype(str)
dados['tipo_acidente'] = dados['tipo_acidente'].astype(str)
dados['causa_principal'] = dados['causa_principal'].map({'sim':True,'nao':False})
dados['causa_principal'] = dados.apply(lambda r:[r['tipo_acidente'],r['causa_principal']],axis=1)

def get_causa_principal(s):
    return s[s.apply(lambda x:x[1])].apply(lambda x:x[0]).unique().tolist()

acidentes = dados.groupby('id').agg({
    'br':'first',
    'fase_dia':'first',
    'sentido_via':'first',
    'condicao_metereologica':'first',
    'tipo_pista':'first',
    'uso_solo':'first',
    'ilesos':'sum',
    'feridos_leves':'sum',
    'feridos_graves':'sum',
    'mortos':'sum',
    'pesid':lambda s:s.isna().any(),
    'latitude':'first',
    'longitude':'first',
    'data':'first',
    'causa_principal':lambda s:get_causa_principal(s),
    'tipo_veiculo':lambda s:s.unique().tolist(),
    'uf':'first'
})

acidentes.to_pickle(Path('..','data','acidentes_full.pkl'))