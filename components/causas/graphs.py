# Em components/causas/graphs.py

import pandas as pd
from pathlib import Path
import plotly.express as px
import plotly.colors as pc  

df = pd.read_pickle(Path('data', 'acidentes.pkl'))

# Dicionário de legendas que você completou
mapa_legendas = {
    'acessar a via sem observar a presenca dos outros veiculos': 'Acessar a via sem observar a presenca dos outros veiculos',
    'acesso irregular': 'Acesso irregular',
    'acostamento em desnivel': 'Acostamento em desnivel',
    'acumulo de agua sobre o pavimento': 'Acumulo de agua sobre o pavimento',
    'acumulo de areia ou detritos sobre o pavimento': 'Acumulo de areia ou detritos sobre o pavimento',
    'acumulo de oleo sobre o pavimento': 'Acumulo de oleo sobre o pavimento',
    'afundamento ou ondulacao no pavimento': 'Afundamento ou ondulacao no pavimento',
    'agressao externa': 'Agressao externa',
    'animais na pista': 'Animais na pista',
    'area urbana sem a presenca de local apropriado para a travessia de pedestres': 'Area urbana sem local apropriado para travessia de pedestres',
    'ausencia de reacao do condutor': 'Ausencia de reacao do condutor',
    'ausencia de sinalizacao': 'Ausencia de sinalizacao',
    'avarias e/ou desgaste excessivo no pneu': 'Avarias e/ou desgaste excessivo no pneu',
    'carga excessiva e/ou mal acondicionada': 'Carga excessiva e/ou mal acondicionada',
    'chuva': 'Chuva',
    'condutor deixou de manter distancia do veiculo da frente': 'Condutor deixou de manter distancia do veiculo da frente',
    'condutor desrespeitou a iluminacao vermelha do semaforo': 'Condutor desrespeitou a iluminacao vermelha do semaforo',
    'condutor dormindo': 'Condutor dormindo',
    'condutor nao acionou o farol baixo durante o dia em rodovias de pista simples': 'Condutor nao acionou o farol baixo durante o dia em rodovias de pista simples',
    'condutor usando celular': 'Condutor usando celular',
    'conversao proibida': 'Conversao proibida',
    'curva acentuada': 'Curva acentuada',
    'declive acentuado': 'Declive acentuado',
    'defeito mecanico no veiculo': 'Defeito mecanico no veiculo',
    'defeito na via': 'Defeito na via',
    'deficiencia do sistema de iluminacao/sinalizacao': 'Deficiencia do sistema de iluminacao/sinalizacao',
    'deficiencia ou nao acionamento do sistema de iluminacao/sinalizacao do veiculo': 'Deficiencia ou nao acionamento do sistema de iluminacao/sinalizacao do veiculo',
    'deixar de acionar o farol da motocicleta (ou similar)': 'Deixar de acionar o farol da motocicleta (ou similar)',
    'demais falhas mecanicas ou eletricas': 'Demais falhas mecanicas ou eletricas',
    'demais falhas na via': 'Demais falhas na via',
    'demais fenomenos da natureza': 'Demais fenomenos da natureza',
    'desobediencia as normas de transito pelo condutor': 'Desobediencia as normas de transito pelo condutor',
    'desobediencia as normas de transito pelo pedestre': 'Desobediencia as normas de transito pelo pedestre',
    'desrespeitar a preferencia no cruzamento': 'Desrespeitar a preferencia no cruzamento',
    'desvio temporario': 'Desvio temporario',
    'entrada inopinada do pedestre': 'Entrada inopinada do pedestre',
    'estacionar ou parar em local proibido': 'Estacionar ou parar em local proibido',
    'faixas de transito com largura insuficiente': 'Faixas de transito com largura insuficiente',
    'falta de acostamento': 'Falta de acostamento',
    'falta de atencao a conducao': 'Falta de atencao a conducao',
    'falta de atencao do pedestre': 'Falta de atencao do pedestre',
    'falta de elemento de contencao que evite a saida do leito carrocavel': 'Falta de elemento de contencao que evite a saida do leito carrocavel',
    'farois desregulados': 'Farois desregulados',
    'fenomenos da natureza': 'Fenomenos da natureza',
    'frear bruscamente': 'Frear bruscamente',
    'fumaca': 'Fumaca',
    'iluminacao deficiente': 'Iluminacao deficiente',
    'ingestao de alcool': 'Ingestao de alcool',
    'ingestao de alcool e/ou substancias psicoativas pelo pedestre': 'Ingestao de alcool e/ou substancias psicoativas pelo pedestre',
    'ingestao de alcool ou de substancias psicoativas pelo pedestre': 'Ingestao de alcool ou de substancias psicoativas pelo pedestre',
    'ingestao de alcool pelo condutor': 'Ingestao de alcool pelo condutor',
    'ingestao de substancias psicoativas': 'Ingestao de substancias psicoativas',
    'ingestao de substancias psicoativas pelo condutor': 'Ingestao de substancias psicoativas pelo condutor',
    'mal subito': 'Mal subito',
    'mal subito do condutor': 'Mal subito do condutor',
    'manobra de mudanca de faixa': 'Manobra de mudanca de faixa',
    'modificacao proibida': 'Modificacao proibida',
    'nao guardar distancia de seguranca': 'Nao guardar distancia de seguranca',
    'neblina': 'Neblina',
    'objeto estatico sobre o leito carrocavel': 'Objeto estatico sobre o leito carrocavel',
    'obras na pista': 'Obras na pista',
    'obstrucao na via': 'Obstrucao na via',
    'obstrucao via tentativa assalto': 'Obstrucao via tentativa assalto',
    'participar de racha': 'Participar de racha',
    'pedestre - ingestao de alcool/ substancias psicoativas': 'Pedestre - ingestao de alcool/ substancias psicoativas',
    'pedestre andava na pista': 'Pedestre andava na pista',
    'pedestre cruzava a pista fora da faixa': 'Pedestre cruzava a pista fora da faixa',
    'pista em desnivel': 'Pista em desnivel',
    'pista esburacada': 'Pista esburacada',
    'pista escorregadia': 'Pista escorregadia',
    'problema com o freio': 'Problema com o freio',
    'problema na suspensao': 'Problema na suspensao',
    'reacao tardia ou ineficiente do condutor': 'Reacao tardia ou ineficiente do condutor',
    'redutor de velocidade em desacordo': 'Redutor de velocidade em desacordo',
    'restricao de visibilidade': 'Restricao de visibilidade',
    'restricao de visibilidade em curvas horizontais': 'Restricao de visibilidade em curvas horizontais',
    'restricao de visibilidade em curvas verticais': 'Restricao de visibilidade em curvas verticais',
    'retorno proibido': 'Retorno proibido',
    'semaforo com defeito': 'Semaforo com defeito',
    'sinalizacao da via insuficiente ou inadequada': 'Sinalizacao da via insuficiente ou inadequada',
    'sinalizacao encoberta': 'Sinalizacao encoberta',
    'sinalizacao mal posicionada': 'Sinalizacao mal posicionada',
    'sistema de drenagem ineficiente': 'Sistema de drenagem ineficiente',
    'suicidio (presumido)': 'Suicidio (presumido)',
    'trafegar com motocicleta (ou similar) entre as faixas': 'Trafegar com motocicleta (ou similar) entre as faixas',
    'transitar na calcada': 'Transitar na calcada',
    'transitar na contramao': 'Transitar na contramao',
    'transitar no acostamento': 'Transitar no acostamento',
    'transtornos mentais (exceto suicidio)': 'Transtornos mentais (exceto suicidio)',
    'ultrapassagem indevida': 'Ultrapassagem indevida',
    'velocidade incompativel': 'Velocidade incompativel',
}

def data_filter(year,state):
    data = pd.read_pickle(Path('data','acidentes.pkl'))
    data = data[data['data'].dt.year == year]
    if state != 'all':
        data = data[data['uf'] == state]
    return data



def bar_chart_causas(year,state):
    """
    Cria um gráfico de barras aprimorado com legendas corrigidas e layout automático.
    As cores dos números do gráfico se adaptam automaticamente à luminosidade da barra.
    """
    df_filtered = data_filter(year,state)
    causas_count = df_filtered['causa_acidente'].value_counts().nlargest(10).sort_values(ascending=True)
    y_labels_corrigidos = causas_count.index.map(lambda causa: mapa_legendas.get(causa, causa))

    fig = px.bar(
        x=causas_count.values,
        y=y_labels_corrigidos,
        orientation='h',
        title=f'Top 10 Causas de Acidentes em {year}',
        labels={'x': 'Número de Acidentes', 'y': 'Causa do Acidente'},
        text=causas_count.values,
        color=causas_count.values,
        color_continuous_scale=px.colors.sequential.Teal
    )

    fig.update_layout(
        template="plotly_dark",
        title_x=0.5,
        height=600,
        coloraxis_showscale=False,
        margin=dict(t=50, b=40, r=40)
    )
    
    fig.update_yaxes(automargin=True)

    # === Ajuste dinâmico da cor do texto conforme o brilho da barra ===
    scale = px.colors.sequential.Teal

    def parse_color(c):
        """Converte cor (hex ou rgb) para tupla (r, g, b)"""
        if c.startswith("#"):
            return pc.hex_to_rgb(c)
        elif c.startswith("rgb"):
            nums = c.strip("rgb() ").split(",")
            return tuple(map(int, nums))
        else:
            raise ValueError(f"Formato de cor inesperado: {c}")

    rgb_colors = [parse_color(c) for c in scale]
    brightness = [0.299*r + 0.587*g + 0.114*b for r, g, b in rgb_colors]
    cutoff = sum(brightness)/len(brightness)

    colors = fig.data[0].marker.color
    text_colors = []
    for c in colors:
        norm = (c - min(colors)) / (max(colors) - min(colors)) if max(colors) != min(colors) else 0
        r, g, b = rgb_colors[int(norm*(len(rgb_colors)-1))]
        bright = 0.299*r + 0.587*g + 0.114*b
        text_colors.append('black' if bright > cutoff else 'white')

    fig.update_traces(
        textposition='inside',
        textfont_size=12,
        textfont_color=text_colors,
        insidetextanchor='middle',
        hovertemplate="<b>Causa:</b> %{y}<br><b>Nº de Acidentes:</b> %{x}<extra></extra>"
    )

    return fig


def data_filter_2(year,state):
    data = pd.read_pickle(Path('data','acidentes_full.pkl'))
    data = data[data['data'].dt.year == year]
    if state != 'all':
        data = data[data['uf'] == state]
    return data

def treemap_vehicles(year,state):
    data = data_filter_2(year,state)
    data = data.explode('tipo_veiculo')
    data = data.explode('causa_principal')
    data['gravidade'] = data.apply(
    lambda row: 'fatal' if row['mortos'] > 0 else ('grave' if row['feridos_graves'] > 0 else 'leve'),
    axis=1)
    data = data.groupby(['tipo_veiculo','gravidade','causa_principal'],as_index=False).count()[['tipo_veiculo','gravidade','causa_principal','br']]    
    df = data
    df['causa_principal'] = df['causa_principal'].str.capitalize()
    df['gravidade'] = df['gravidade'].str.capitalize()
    df['nivel'] = df['gravidade']+'-'+df['causa_principal']
    df['nivel'] = df['nivel'].str.capitalize()
    df['tipo_veiculo'] = df['tipo_veiculo'].str.capitalize()


    fig = px.treemap(
        df,
        path=['tipo_veiculo', 'gravidade','causa_principal'],  
        values='br',                  
        title='Acidentes por Tipo de Veículo e Gravidade',
        color_discrete_sequence=px.colors.qualitative.Set3
    )

    fig.update_layout(
        paper_bgcolor='#060606',
        font = dict(
            color='white'
        )
    )

    return fig