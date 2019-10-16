# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 01:42:06 2019

@author: icaro
"""
import pandas as pd
from plotly.offline import plot
import plotly.graph_objs as go

data_2017 = pd.read_json("C:/Users/icaro/Desktop/Hackaton/Dados tratados/Json/2017.json", orient = 'index')
data_2016 = pd.read_json("C:/Users/icaro/Desktop/Hackaton/Dados tratados/Json/2016.json", orient = 'index')
data_2015 = pd.read_json("C:/Users/icaro/Desktop/Hackaton/Dados tratados/Json/2015.json", orient = 'index')

anos = [2015,2016,2017]

#Taxa coleta RDO por cidade

rdo_y = [data_2015.loc['Lagoinha', 'Resíduos']['Taxa coleta RDO'],
         data_2016.loc['Lagoinha', 'Resíduos']['Taxa coleta RDO'],
         data_2017.loc['Lagoinha', 'Resíduos']['Taxa coleta RDO']]
tx_rdo = go.Scatter(x = anos, y = rdo_y, mode = 'lines')

layout_rdo = go.Layout(title = 'Taxa de resíduos domésticos recolhidos por ano em Lagoinha', 
                   yaxis={'title':'Taxa de RDO'},
                   xaxis={'title': 'Anos', 'tickmode': 'linear', 'dtick':1})
                   #paper_bgcolor = '#ff7f0e'
                   #colorway = ('#d62728','#1f77b4'))

fig1 = go.Figure(data = [tx_rdo], layout = layout_rdo)
plot(fig1)

#Massa coletada por cidade
coletada_y = [data_2015.loc['Lagoinha', 'Resíduos']['Massa coletada'],
         data_2016.loc['Lagoinha', 'Resíduos']['Massa coletada'],
         data_2017.loc['Lagoinha', 'Resíduos']['Massa coletada']]
m_coletada = go.Scatter(x = anos, y = coletada_y, mode = 'lines')

layout_coletada = go.Layout(title = 'Massa total recolhida por ano em Lagoinha', 
                   yaxis={'title':'Massa'},
                   xaxis={'title': 'Anos', 'tickmode': 'linear', 'dtick':1})
                   #paper_bgcolor = '#ff7f0e'
                   #colorway = ('#d62728','#1f77b4'))

fig2 = go.Figure(data = [m_coletada], layout = layout_coletada)
plot(fig2)

#Taxa de recuperação de recicláveis

tx_recup_y = [data_2015.loc['Cotia', 'Resíduos']['Taxa de recuperação de recicláveis'],
         data_2016.loc['Cotia', 'Resíduos']['Taxa de recuperação de recicláveis'],
         data_2017.loc['Cotia', 'Resíduos']['Taxa de recuperação de recicláveis']]
tx_recup = go.Scatter(x = anos, y = tx_recup_y, mode = 'lines+markers')

layout_recup = go.Layout(title = 'Taxa de recuperação em Cotia', 
                   yaxis={'title':'Taxa'},
                   xaxis={'title': 'Anos', 'tickmode': 'linear', 'dtick':1})
                   #paper_bgcolor = '#ff7f0e'
                   #colorway = ('#d62728','#1f77b4'))

fig3 = go.Figure(data = [tx_recup], layout = layout_recup)
plot(fig3)

# Massa recolhida via seletiva  
seletiva_y = [data_2015.loc['Cotia', 'Resíduos']['Massa recolhida via coleta seletiva'],
         data_2016.loc['Cotia', 'Resíduos']['Massa recolhida via coleta seletiva'],
         data_2017.loc['Cotia', 'Resíduos']['Massa recolhida via coleta seletiva']]
m_seletiva = go.Bar(x = anos, y = seletiva_y)

layout_selet = go.Layout(title = 'Massa recolhida via coleta seletiva em Cotia', 
                   yaxis={'title':'massa'},
                   xaxis={'title': 'Anos', 'tickmode': 'linear', 'dtick':1})
                   #paper_bgcolor = '#ff7f0e'
                   #colorway = ('#d62728','#1f77b4'))

fig4 = go.Figure(data = [m_seletiva], layout = layout_selet)
plot(fig4)

#Taxa população atendida com coleta

tx_pop_aten_y = [data_2015.loc['Cotia', 'Resíduos']['Taxa pop atendida com coleta'],
         data_2016.loc['Cotia', 'Resíduos']['Taxa pop atendida com coleta'],
         data_2017.loc['Cotia', 'Resíduos']['Taxa pop atendida com coleta']]
tx_pop = go.Scatter(x = anos, y = tx_pop_aten_y, mode = 'lines+markers')

layout_pop = go.Layout(title = 'Taxa de população atendida com coleta em Cotia', 
                   yaxis={'title':'Taxa'},
                   xaxis={'title': 'Anos', 'tickmode': 'linear', 'dtick':1})
                   #paper_bgcolor = '#ff7f0e'
                   #colorway = ('#d62728','#1f77b4'))

fig5 = go.Figure(data = [tx_pop], layout = layout_pop)
plot(fig5)