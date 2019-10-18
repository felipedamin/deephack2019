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
tx_rdo = go.Scatter(x = anos, y = rdo_y, mode = 'lines + markers')

layout_rdo = go.Layout(title={'text': 'Taxa de cobertura de coleta de resíduos domésticos em relação à população total de Lagoinha', 
                           'font':{'family': "Times New Roman", "size": 30 },
                           'x': 0.5, 'y': 0.9}, 
                   yaxis={'title':'População atendida/População total (%)'},
                   xaxis={'title': 'Anos', 'tickmode': 'linear', 'dtick':1},
                       paper_bgcolor='rgba(0,0,0,0)',
                       font = dict(color = '#ecf0f1'))
                                   
fig1 = go.Figure(data = [tx_rdo], layout = layout_rdo)
#plot(fig1)

#Massa coletada por cidade
coletada_y = [data_2015.loc['Lagoinha', 'Resíduos']['Massa coletada'],
         data_2016.loc['Lagoinha', 'Resíduos']['Massa coletada'],
         data_2017.loc['Lagoinha', 'Resíduos']['Massa coletada']]
m_coletada = go.Scatter(x = anos, y = coletada_y, mode = 'lines + markers')

layout_coletada = go.Layout(title={'text': 'Massa coletada de resíduos domésticos + resíduos públicos per capita em relação à população urbana de Lagoinha', 
                           'font':{'family': "Times New Roman", "size": 25 },
                           'x': 0.5, 'y': 0.9},
                   yaxis={'title':'Quantidade total recolhida/ População urbana (kg/hab./dia)'},
                   xaxis={'title': 'Anos', 'tickmode': 'linear', 'dtick':1},
                       paper_bgcolor='rgba(0,0,0,0)',
                       font = dict(color = '#ecf0f1'))

fig2 = go.Figure(data = [m_coletada], layout = layout_coletada)
#plot(fig2)

#Taxa de recuperação de recicláveis

tx_recup_y = [data_2015.loc['Cotia', 'Resíduos']['Taxa de recuperação de recicláveis'],
         data_2016.loc['Cotia', 'Resíduos']['Taxa de recuperação de recicláveis'],
         data_2017.loc['Cotia', 'Resíduos']['Taxa de recuperação de recicláveis']]
tx_recup = go.Scatter(x = anos, y = tx_recup_y, mode = 'lines+markers')

layout_recup = go.Layout(title={'text': 'Taxa de recuperação de materiais recicláveis em relação à quantidade total de resíduos coletados em Cotia', 
                           'font':{'family': "Times New Roman", "size": 25 },
                           'x': 0.5, 'y': 0.9}, 
                   yaxis={'title':'Quantidade de recicláveis recuperados/Quantidade total (%)'},
                   xaxis={'title': 'Anos', 'tickmode': 'linear', 'dtick':1},
                       paper_bgcolor='rgba(0,0,0,0)',
                       font = dict(color = '#ecf0f1'))
fig3 = go.Figure(data = [tx_recup], layout = layout_recup)
#plot(fig3)

# Massa recolhida via seletiva  
seletiva_y = [data_2015.loc['Cotia', 'Resíduos']['Massa recolhida via coleta seletiva'],
         data_2016.loc['Cotia', 'Resíduos']['Massa recolhida via coleta seletiva'],
         data_2017.loc['Cotia', 'Resíduos']['Massa recolhida via coleta seletiva']]
m_seletiva = go.Bar(x = anos, y = seletiva_y)

layout_selet = go.Layout(title={'text': 'Massa per capita recolhida via coleta seletiva em Cotia', 
                           'font':{'family': "Times New Roman", "size": 30 },
                           'x': 0.5, 'y': 0.9},
                   yaxis={'title':'Quantidade de recicláveis recolhidos/ Pop urbana (Kg/hab./ano)'},
                   xaxis={'title': 'Anos', 'tickmode': 'linear', 'dtick':1}, #'color' :'#ecf0f1'},
                       paper_bgcolor='rgba(0,0,0,0)',
                       font = dict(color = '#ecf0f1'),
                       )

fig4 = go.Figure(data = [m_seletiva], layout = layout_selet)
#plot(fig4)

#Taxa população atendida com coleta

tx_pop_aten_y = [data_2015.loc['Cotia', 'Resíduos']['Taxa pop atendida com coleta'],
         data_2016.loc['Cotia', 'Resíduos']['Taxa pop atendida com coleta'],
         data_2017.loc['Cotia', 'Resíduos']['Taxa pop atendida com coleta']]
tx_pop = go.Scatter(x = anos, y = tx_pop_aten_y, mode = 'lines+markers')

layout_pop = go.Layout(title={'text': 'Taxa da população beneficiado pelo serviço de coleta de resíduos domiciliares em Cotia', 
                           'font':{'family': "Times New Roman", "size": 30,
                                   'color': '#ecf0f1'},
                           'x': 0.5, 'y': 0.9},
                   yaxis={'title':'População atendida/ População total (%)',
                          #'color': '#ecf0f1'
                          },
                          
                   xaxis={'title': 'Anos', 'tickmode': 'linear', 'dtick':1}, #'color' :'#ecf0f1'},
                       paper_bgcolor='rgba(0,0,0,0)',
                       font = dict(color = '#ecf0f1'),
                       )

fig5 = go.Figure(data = [tx_pop], layout = layout_pop)
#plot(fig5)

fig1.write_image("C:/Users/icaro/Desktop/Hackaton/Dados tratados/Json/coleta_rdo.png", width = 1500, height = 700, scale = 2)
fig2.write_image("C:/Users/icaro/Desktop/Hackaton/Dados tratados/Json/massa_coletada.png", width = 1500, height = 700, scale = 2)
fig3.write_image("C:/Users/icaro/Desktop/Hackaton/Dados tratados/Json/recup_reciclaveis.png", width = 1000, height = 700, scale = 2)
fig4.write_image("C:/Users/icaro/Desktop/Hackaton/Dados tratados/Json/massa_via_seletiva.png", width = 1500, height = 700, scale = 2)
fig5.write_image("C:/Users/icaro/Desktop/Hackaton/Dados tratados/Json/pop_beneficiada.png", width = 1500, height = 700, scale = 2)
