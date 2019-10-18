# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 22:57:44 2019

@author: icaro
"""

import pandas as pd
from plotly.offline import plot
import plotly.graph_objs as go
import numpy as np

df = pd.read_json("C:/Users/icaro/Desktop/Hackaton/Dados tratados/Energia/energia_co2.json", orient = 'index')

tipos = ['Petróleo e derivados - t/m3', 'Biomassa e derivados - TON',
 'Rede pública','Petróleo e derivados - TON', 'Gás Natural (Seco)',
 'Autoprodução(Eólica, Hidrelétrica, Fotovoltaica, Termoelétrica)',
 'Gás Natural e derivados - TON', 'Biomassa e derivados - t/m3',
 'Outros - TON','Carvão Mineral e derivados', 'Outros - t/m3']

# Gráfico tipos de fonte estado de São Paulo em 2017

quant_2017= {'Petróleo e derivados - t/m3': 0,
 'Biomassa e derivados - TON': 0,
 'Rede pública': 0,
 'Petróleo e derivados - TON': 0,
 'Gás Natural (Seco)': 0,
 'Autoprodução(Eólica, Hidrelétrica, Fotovoltaica, Termoelétrica)': 0,
 'Gás Natural e derivados - TON': 0,
 'Biomassa e derivados - t/m3': 0,
 'Outros - TON': 0,
 'Carvão Mineral e derivados': 0,
 'Outros - t/m3': 0}

for energia in tipos:
    quant = 0
    for cidade in df.index:
        quant += df.loc[cidade, 2017][energia]
    quant_2017[energia] = quant
    
trace1 = go.Pie(values=list(quant_2017.values()), labels=list(quant_2017.keys()))

layout1 = go.Layout(title={'text':'Quantidade consumida por Fonte Energética em 2017', 'font':{'family': "Times New Roman"},
                          })
                   #yaxis={'title':'Preço da casa'},
                   #xaxis={'title': 'Ano de construção', 'tickmode': 'linear', 'dtick':1},
                   #paper_bgcolor = '#ff7f0e'
                   #colorway = ('#d62728','#1f77b4'))

fig1 = go.Figure(data = [trace1], layout = layout1)
#plot(fig1)

#Quantidade consumida por cidade(Americana)

quant_cidade_2017= df.loc['Americana', 2017].copy()

del quant_cidade_2017['Emissão de CO2']

trace2 = go.Pie(values=list(quant_cidade_2017.values()), labels=list(quant_cidade_2017.keys()))

layout2 = go.Layout(title={'text':'Quantidade consumida por Fonte Energética em Americana 2017', 'font':{'family': "Balto"},
                          })
                   #yaxis={'title':'Preço da casa'},
                   #xaxis={'title': 'Ano de construção', 'tickmode': 'linear', 'dtick':1},
                   #paper_bgcolor = '#ff7f0e'
                   #colorway = ('#d62728','#1f77b4'))

fig2 = go.Figure(data = [trace2], layout = layout2)
#plot(fig2)

#Gráfico quantidade de CO2 emitido por cidade por ano(Americana)

co2_cid = []
anos = [2011,2012,2013,2014,2015,2016,2017,2018]

for ano in df.columns:
    co2_cid.append(df.loc['Americana', ano]['Emissão de CO2'])

trace3 = go.Bar(x=anos, y=co2_cid)

layout3 = go.Layout(title= 'Quantidade de CO2 emitida por ano em Americana',
                   yaxis={'title':'Quantidade emitida'},
                   xaxis={'title': 'Ano', 'tickmode': 'linear', 'dtick':1})
                   #paper_bgcolor = '#ff7f0e'
                   #colorway = ('#d62728','#1f77b4'))

fig3 = go.Figure(data = [trace3], layout = layout3)
#plot(fig3)
    

fig1.write_image("C:/Users/icaro/Desktop/Hackaton/Dados tratados/Energia/consumo_fonte_estado.png", width = 1500, height = 700, scale = 2)
fig2.write_image("C:/Users/icaro/Desktop/Hackaton/Dados tratados/Energia/consumo_fonte_cidade.png", width = 1500, height = 700, scale = 2)
fig3.write_image("C:/Users/icaro/Desktop/Hackaton/Dados tratados/Energia/co2_cidade.png", width = 1000, height = 700, scale = 2)

    