# Dashboard de Acidentes Rodoviários (Datatran)

## Descrição
Projeto de **dashboard interativo** para análise de acidentes rodoviários no Brasil, utilizando dados do **Datatran** da Polícia Rodoviária Federal (PRF). A ferramenta permite identificar padrões, tendências e fatores de risco associados aos acidentes, oferecendo suporte a gestores públicos e pesquisadores na tomada de decisões estratégicas para melhorar a segurança viária.

## Funcionalidades
- **Visualização de acidentes por região:** mapas de densidade mostrando a distribuição por estado, rodovia e microrregião.
- **Análise temporal:** gráficos de séries temporais e sazonalidade para tendências semanais, mensais e anuais.
- **Filtragem interativa:** seleção por rodovia, tipo de acidente e período.
- **Pré-processamento de dados:** limpeza, normalização e tipagem para garantir consistência e eficiência.
- **Preparação para aprendizado de máquina:** estrutura de dados organizada para futuras análises preditivas e detecção de anomalias.
- **Protótipo funcional:** desenvolvido com **Dash** e **Plotly**, com visualizações interativas.

## Tecnologias Utilizadas
- **Python:** Dash, Plotly, Pandas, GeoPandas, NumPy, Scikit-learn, Statsmodels, Seaborn, Matplotlib
- **Bibliotecas auxiliares:** ydata_profiling, Folium, Dash-bootstrap-framework, Pathlib, datetime

## Resultados Preliminares
- Identificação de padrões temporais e espaciais dos acidentes.
- Maior ocorrência de acidentes às sextas, sábados e domingos, e aumento em dezembro.
- Protótipo interativo com visualização rápida de dados consolidados.

## Objetivo Final
Desenvolver um **painel de controle completo** para análise de acidentes rodoviários, integrando aprendizado de máquina, detecção de anomalias e agrupamento de acidentes, apoiando políticas públicas e estratégias de prevenção mais eficazes.


## Instalação

#### Windows

   - python -m venv venv
   - venv\Scripts\activate
   - pip install -r requirements.txt

#### MacOs/Linux

   - python -m venv venv
   - source venv/bin/activate
   - pip install -r requirements.txt
   

 **Observação:** Execute o codigo **a partir da raiz do projeto**, onde está localizado o arquivo `requirements.txt`

