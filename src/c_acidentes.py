# Em src/c_acidentes.py

import pandas as pd 
from pathlib import Path 

datatran = pd.read_pickle(Path ('data','datatran.pkl'))

# IMPORTANTE: Substitua 'tipo_acidente' e 'tipo_veiculo' pelos nomes REAIS das colunas no seu arquivo.
datatran = datatran.groupby('id').agg({
    'pesid':lambda s: s.isna().any(),
    'data':'first',
    'ilesos':'sum',
    'feridos_leves':'sum',
    'feridos_graves':'sum',
    'mortos':'sum',
    'latitude':'first',
    'longitude':'first',
    'uf':'first',
    'causa_acidente': 'first',
    'tipo_acidente': 'first',          # <-- COLUNA ADICIONADA
    'condicao_metereologica': 'first',
    
})

datatran.to_pickle(Path('data','acidentes.pkl'))

print("Arquivo 'acidentes.pkl' atualizado com sucesso com os novos campos!")
