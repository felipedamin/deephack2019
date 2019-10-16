# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 23:06:58 2019

@author: icaro
"""

import pandas as pd
from plotly.offline import plot
import plotly.graph_objs as go
import numpy as np

energia_co2 = pd.read_excel("C:/Users/icaro/Desktop/Hackaton/Dados tratados/Energia/energia_co2_filtrado.xls")

energia_co2.drop(columns = ['Unnamed: 0', 'Estado'], inplace = True)
energia_co2.set_index('Código do município', inplace = True)

df_2017 = energia_co2[energia_co2['Ano'] == 2017]
# Gráfico Estado de São Paulo em 2017

tipo_quant = {}
for tipo in df_2017['Tipo de Fonte Energética'].unique():
    copy = df_2017.copy()
    copy = copy[copy['Tipo de Fonte Energética'] == tipo]
    quant = sum(copy['Quantidade Consumida'])
    tipo_quant[tipo] = quant

trace1 = go.Pie(values=list(tipo_quant.values()), labels=list(tipo_quant.keys()))

layout1 = go.Layout(title={'text':'Quantidade consumida por Fonte Energética em 2017', 'font':{'family': "Balto"},
                          })
                   #yaxis={'title':'Preço da casa'},
                   #xaxis={'title': 'Ano de construção', 'tickmode': 'linear', 'dtick':1},
                   #paper_bgcolor = '#ff7f0e'
                   #colorway = ('#d62728','#1f77b4'))

fig1 = go.Figure(data = [trace1], layout = layout1)
plot(fig1)

# Gráfico 2017 por cidade

df_ameri_2017 = df_2017[df_2017['Município'] == 'Americana']
tipo_quant2 = {}
for tipo in df_ameri_2017['Tipo de Fonte Energética'].unique():
    copy = df_ameri_2017.copy()
    copy = copy[copy['Tipo de Fonte Energética'] == tipo]
    quant = sum(copy['Quantidade Consumida'])
    tipo_quant2[tipo] = quant

trace2 = go.Pie(values=list(tipo_quant2.values()), labels=list(tipo_quant2.keys()))

layout2 = go.Layout(title={'text':'Quantidade consumida por Fonte Energética em Americana 2017', 'font':{'family': "Balto"},
                          })
                   #yaxis={'title':'Preço da casa'},
                   #xaxis={'title': 'Ano de construção', 'tickmode': 'linear', 'dtick':1},
                   #paper_bgcolor = '#ff7f0e'
                   #colorway = ('#d62728','#1f77b4'))

fig2 = go.Figure(data = [trace2], layout = layout2)
plot(fig2)


# Quantidade de C02 por cidade por ano
co2_cid = energia_co2[energia_co2['Município'] == 'Campinas']

co2_ano = {}

for ano in co2_cid['Ano'].unique():
    copy = co2_cid.copy()
    copy = copy[copy['Ano'] == ano]
    emis = sum(copy['Emissões de CO2 '])
    co2_ano[ano] = emis
  
co2_ano[2012] = 0
trace3 = go.Bar(x=list(co2_ano.keys()), y=list(co2_ano.values()))

layout3 = go.Layout(title= 'Quantidade de CO2 emitida por ano em Campinas',
                   yaxis={'title':'Quantidade emitida'},
                   xaxis={'title': 'Ano', 'tickmode': 'linear', 'dtick':1})
                   #paper_bgcolor = '#ff7f0e'
                   #colorway = ('#d62728','#1f77b4'))

fig3 = go.Figure(data = [trace3], layout = layout3)
plot(fig3)

#Quantidade de C02 no estado por ano

co2_estado = {}

for ano in energia_co2['Ano'].unique():
    copy = energia_co2.copy()
    copy = copy[copy['Ano'] == ano]
    emis = np.nansum(copy['Emissões de CO2 '])
    co2_estado[ano] = emis

co2_estado[2015] = 0
trace4 = go.Bar(x=list(co2_estado.keys()), y=list(co2_estado.values()))

layout4 = go.Layout(title= 'Quantidade de CO2 emitida por ano no estado de SP',
                   yaxis={'title':'Quantidade emitida'},
                   xaxis={'title': 'Ano', 'tickmode': 'linear', 'dtick':1})
                   #paper_bgcolor = '#ff7f0e'
                   #colorway = ('#d62728','#1f77b4'))

fig4 = go.Figure(data = [trace4], layout = layout4)
plot(fig4)