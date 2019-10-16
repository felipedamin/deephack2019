# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 02:21:51 2019

@author: icaro
"""

import pandas as pd
from plotly.offline import plot
import plotly.graph_objs as go

data_2017 = pd.read_json("C:/Users/icaro/Desktop/Hackaton/Dados tratados/Json/2017.json", orient = 'index')
data_2016 = pd.read_json("C:/Users/icaro/Desktop/Hackaton/Dados tratados/Json/2016.json", orient = 'index')
data_2015 = pd.read_json("C:/Users/icaro/Desktop/Hackaton/Dados tratados/Json/2015.json", orient = 'index')

anos = [2015,2016,2017]

#Consumo médio per capita por cidade

consumo_y = [data_2015.loc['Lagoinha', 'Saneamento']['Consumo médio per capita'],
         data_2016.loc['Lagoinha', 'Saneamento']['Consumo médio per capita'],
         data_2017.loc['Lagoinha', 'Saneamento']['Consumo médio per capita']]
consumo = go.Scatter(x = anos, y = consumo_y, mode = 'lines')

layout_consumo = go.Layout(title = 'Consumo médio per capita em Lagoinha', 
                   yaxis={'title':'Consumo médio'},
                   xaxis={'title': 'Anos', 'tickmode': 'linear', 'dtick':1})
                   #paper_bgcolor = '#ff7f0e'
                   #colorway = ('#d62728','#1f77b4'))

fig1 = go.Figure(data = [consumo], layout = layout_consumo)
plot(fig1)

#Taxa pop atendida com saneamento
saneamento_y = [data_2015.loc['Lagoinha', 'Saneamento']['Taxa de pop atendida'],
         data_2016.loc['Lagoinha', 'Saneamento']['Taxa de pop atendida'],
         data_2017.loc['Lagoinha', 'Saneamento']['Taxa de pop atendida']]
saneamento = go.Scatter(x = anos, y = saneamento_y, mode = 'lines + markers')

layout_saneamento = go.Layout(title = 'Porcentagem da população com saneamento em Lagoinha', 
                   yaxis={'title':'Porcentagem'},
                   xaxis={'title': 'Anos', 'tickmode': 'linear', 'dtick':1})
                   #paper_bgcolor = '#ff7f0e'
                   #colorway = ('#d62728','#1f77b4'))

fig2 = go.Figure(data = [saneamento], layout = layout_saneamento)
plot(fig2)