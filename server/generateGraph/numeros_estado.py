# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 20:37:15 2019

@author: icaro
"""

import pandas as pd
from plotly.offline import plot
import plotly.graph_objs as go
import numpy as np

df_2017 = pd.read_json("./server/database/saneamentoResiduos/2017.json", orient = 'index')
df_2016 = pd.read_json("./server/database/saneamentoResiduos/2016.json", orient = 'index')
df_2015 = pd.read_json("./server/database/saneamentoResiduos/2015.json", orient = 'index')

anos = [2015,2016,2017]

#Gráfico Donut mostrando porcentagem de nan sobre o total em 2017
len_2017 = len(df_2017['Resíduos'])
nan_2017 = 0
for index in df_2017.index:
    if df_2017.loc[index, 'Resíduos']['Taxa de recuperação de recicláveis'] == None:
        nan_2017 += 1

labels = ['N° de cidades que apresentaram dados',
          'N° de cidades que não apresentaram dados']
values = [len_2017 - nan_2017, nan_2017]

trace1 = go.Pie(labels=labels, values=values, hole=.3)

layout1 = go.Layout(title={'text':'Percentual de cidades que forneceram dados sobre a Taxa de Recuperação de Recicláveis em 2017', 'font':{'family': "Times New Roman"},
                          })

fig1 = go.Figure(data=[trace1], layout = layout1)
#plot(fig1)
  
#Gráfico Donut mostrando porcentagem de nan sobre o total em 2016

len_2016 = len(df_2016['Resíduos'])
nan_2016 = 0
for index in df_2016.index:
    if df_2016.loc[index, 'Resíduos']['Taxa de recuperação de recicláveis'] == None:
        nan_2016 += 1


labels = ['N° de cidades que apresentaram dados',
          'N° de cidades que não apresentaram dados']
values = [len_2016 - nan_2016, nan_2016]

trace2 = go.Pie(labels=labels, values=values, hole=.3)

layout2 = go.Layout(title={'text':'Percentual de cidades que forneceram dados sobre a Taxa de Recuperação de Recicláveis em 2016', 'font':{'family': "Times New Roman"},
                          })

fig2 = go.Figure(data=[trace2], layout = layout2)
#plot(fig2)

#Gráfico Donut mostrando porcentagem de nan sobre o total em 2015

len_2015 = len(df_2015['Resíduos'])
nan_2015 = 0
for index in df_2015.index:
    if df_2015.loc[index, 'Resíduos']['Taxa de recuperação de recicláveis'] == None:
        nan_2015 += 1

labels = ['N° de cidades que apresentaram dados',
          'N° de cidades que não apresentaram dados']
values = [len_2015 - nan_2015, nan_2015]

trace3 = go.Pie(labels=labels, values=values, hole=.3)

layout3 = go.Layout(title={'text':'Percentual de cidades que forneceram dados sobre a Taxa de Recuperação de Recicláveis em 2015', 'font':{'family': "Times New Roman"},
                          })

fig3 = go.Figure(data=[trace3], layout = layout3)
#plot(fig3)

#Gráfico média da taxa de RDO em São Paulo 
total_2017 = 0
respondidos_2017 = 0

for index in df_2017.index:
    if df_2017.loc[index, 'Resíduos']['Taxa coleta RDO'] != None:
        total_2017 += df_2017.loc[index, 'Resíduos']['Taxa coleta RDO']
        respondidos_2017 += 1


total_2016 = 0
respondidos_2016 = 0

for index in df_2016.index:
    if df_2016.loc[index, 'Resíduos']['Taxa coleta RDO'] != None:
        total_2016 += df_2016.loc[index, 'Resíduos']['Taxa coleta RDO']
        respondidos_2016 += 1

total_2015 = 0
respondidos_2015 = 0

for index in df_2015.index:
    if df_2015.loc[index, 'Resíduos']['Taxa coleta RDO'] != None:
        total_2015 += df_2015.loc[index, 'Resíduos']['Taxa coleta RDO']
        respondidos_2015 += 1

rdo_y = [total_2015/respondidos_2015,
         total_2016/respondidos_2016,
         total_2017/respondidos_2017]

tx_rdo = go.Scatter(x = anos, y = rdo_y, mode = 'lines + markers')

layout_rdo = go.Layout(title={'text': 'Média da taxa de cobertura de coleta de resíduos domésticos no estado de São Paulo por ano', 
                           'font':{'family': "Times New Roman", "size": 30 },
                           'x': 0.5, 'y': 0.9}, 
                   yaxis={'title':'População atendida/População total (%)'},
                   xaxis={'title': 'Anos', 'tickmode': 'linear', 'dtick':1},
                       paper_bgcolor='rgba(0,0,0,0)',
                       font = dict(color = '#ecf0f1'))

fig4 = go.Figure(data = [tx_rdo], layout = layout_rdo)
#plot(fig4)

#Média massa coletada em São Paulo
total_2017 = 0
respondidos_2017 = 0

for index in df_2017.index:
    if df_2017.loc[index, 'Resíduos']['Massa coletada'] != None:
        total_2017 += df_2017.loc[index, 'Resíduos']['Massa coletada']
        respondidos_2017 += 1


total_2016 = 0
respondidos_2016 = 0

for index in df_2016.index:
    if df_2016.loc[index, 'Resíduos']['Massa coletada'] != None:
        total_2016 += df_2016.loc[index, 'Resíduos']['Massa coletada']
        respondidos_2016 += 1

total_2015 = 0
respondidos_2015 = 0

for index in df_2015.index:
    if df_2015.loc[index, 'Resíduos']['Massa coletada'] != None:
        total_2015 += df_2015.loc[index, 'Resíduos']['Massa coletada']
        respondidos_2015 += 1
        
coletada_y = [total_2015/respondidos_2015,
         total_2016/respondidos_2016,
         total_2017/respondidos_2017]

m_coletada = go.Scatter(x = anos, y = coletada_y, mode = 'lines + markers')

layout_coletada = go.Layout(title={'text': 'Média da massa coletada de resíduos domésticos + resíduos públicos per capita no estado de São Paulo', 
                           'font':{'family': "Times New Roman", "size": 25 },
                           'x': 0.5, 'y': 0.9},
                   yaxis={'title':'Quantidade total recolhida/ População urbana (kg/hab./dia)'},
                   xaxis={'title': 'Anos', 'tickmode': 'linear', 'dtick':1},
                       paper_bgcolor='rgba(0,0,0,0)',
                       font = dict(color = '#ecf0f1'))

fig5 = go.Figure(data = [m_coletada], layout = layout_coletada)
#plot(fig5)

# Gráfico Taxa de recuperação de recicláveis
total_2017 = 0
respondidos_2017 = 0

for index in df_2017.index:
    if df_2017.loc[index, 'Resíduos']['Taxa de recuperação de recicláveis'] != None:
        total_2017 += df_2017.loc[index, 'Resíduos']['Taxa de recuperação de recicláveis']
        respondidos_2017 += 1


total_2016 = 0
respondidos_2016 = 0

for index in df_2016.index:
    if df_2016.loc[index, 'Resíduos']['Taxa de recuperação de recicláveis'] != None:
        total_2016 += df_2016.loc[index, 'Resíduos']['Taxa de recuperação de recicláveis']
        respondidos_2016 += 1

total_2015 = 0
respondidos_2015 = 0

for index in df_2015.index:
    if df_2015.loc[index, 'Resíduos']['Taxa de recuperação de recicláveis'] != None:
        total_2015 += df_2015.loc[index, 'Resíduos']['Taxa de recuperação de recicláveis']
        respondidos_2015 += 1

tx_recup_y = [total_2015/respondidos_2015,
         total_2016/respondidos_2016,
         total_2017/respondidos_2017]

tx_recup = go.Scatter(x = anos, y = tx_recup_y, mode = 'lines+markers')

layout_recup = go.Layout(title={'text': 'Média da taxa de recuperação de materiais recicláveis em relação à quantidade total de resíduos coletados no estado de São Paulo', 
                           'font':{'family': "Times New Roman", "size": 25 },
                           'x': 0.5, 'y': 0.9}, 
                   yaxis={'title':'Quantidade de recicláveis recuperados/Quantidade total (%)'},
                   xaxis={'title': 'Anos', 'tickmode': 'linear', 'dtick':1},
                       paper_bgcolor='rgba(0,0,0,0)',
                       font = dict(color = '#ecf0f1'))
fig6 = go.Figure(data = [tx_recup], layout = layout_recup)
#plot(fig6)  
      
#Gráfico Massa recolhida via coleta seletiva
total_2017 = 0
respondidos_2017 = 0

for index in df_2017.index:
    if df_2017.loc[index, 'Resíduos']['Massa recolhida via coleta seletiva'] != None:
        total_2017 += df_2017.loc[index, 'Resíduos']['Massa recolhida via coleta seletiva']
        respondidos_2017 += 1


total_2016 = 0
respondidos_2016 = 0

for index in df_2016.index:
    if df_2016.loc[index, 'Resíduos']['Massa recolhida via coleta seletiva'] != None:
        total_2016 += df_2016.loc[index, 'Resíduos']['Massa recolhida via coleta seletiva']
        respondidos_2016 += 1

total_2015 = 0
respondidos_2015 = 0

for index in df_2015.index:
    if df_2015.loc[index, 'Resíduos']['Massa recolhida via coleta seletiva'] != None:
        total_2015 += df_2015.loc[index, 'Resíduos']['Massa recolhida via coleta seletiva']
        respondidos_2015 += 1

seletiva_y = [total_2015/respondidos_2015,
         total_2016/respondidos_2016,
         total_2017/respondidos_2017]

m_seletiva = go.Bar(x = anos, y = seletiva_y)

layout_selet = go.Layout(title={'text': 'Média da massa per capita recolhida via coleta seletiva no estado de São Paulo', 
                           'font':{'family': "Times New Roman", "size": 30 },
                           'x': 0.5, 'y': 0.9},
                   yaxis={'title':'Quantidade de recicláveis recolhidos/ Pop urbana (Kg/hab./ano)'},
                   xaxis={'title': 'Anos', 'tickmode': 'linear', 'dtick':1}, #'color' :'#ecf0f1'},
                       paper_bgcolor='rgba(0,0,0,0)',
                       font = dict(color = '#ecf0f1'),
                       )

fig7 = go.Figure(data = [m_seletiva], layout = layout_selet)
#plot(fig7)

#Gráfico Taxa população atendida com coleta em São Paulo

total_2017 = 0
respondidos_2017 = 0

for index in df_2017.index:
    if df_2017.loc[index, 'Resíduos']['Taxa pop atendida com coleta'] != None:
        total_2017 += df_2017.loc[index, 'Resíduos']['Taxa pop atendida com coleta']
        respondidos_2017 += 1


total_2016 = 0
respondidos_2016 = 0

for index in df_2016.index:
    if df_2016.loc[index, 'Resíduos']['Taxa pop atendida com coleta'] != None:
        total_2016 += df_2016.loc[index, 'Resíduos']['Taxa pop atendida com coleta']
        respondidos_2016 += 1

total_2015 = 0
respondidos_2015 = 0

for index in df_2015.index:
    if df_2015.loc[index, 'Resíduos']['Taxa pop atendida com coleta'] != None:
        total_2015 += df_2015.loc[index, 'Resíduos']['Taxa pop atendida com coleta']
        respondidos_2015 += 1

tx_pop_aten_y = [total_2015/respondidos_2015,
         total_2016/respondidos_2016,
         total_2017/respondidos_2017]

tx_pop = go.Scatter(x = anos, y = tx_pop_aten_y, mode = 'lines+markers')

layout_pop = go.Layout(title={'text': 'Média da taxa da população beneficiado pelo serviço de coleta de resíduos domiciliares no estado de São Paulo', 
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

fig8 = go.Figure(data = [tx_pop], layout = layout_pop)
#plot(fig8)

# Gráfico consumo médio estado de São Paulo

total_2017 = 0
respondidos_2017 = 0

for index in df_2017.index:
    if df_2017.loc[index, 'Saneamento']['Consumo médio per capita'] != None:
        total_2017 += df_2017.loc[index, 'Saneamento']['Consumo médio per capita']
        respondidos_2017 += 1


total_2016 = 0
respondidos_2016 = 0

for index in df_2016.index:
    if df_2016.loc[index, 'Saneamento']['Consumo médio per capita'] != None:
        total_2016 += df_2016.loc[index, 'Saneamento']['Consumo médio per capita']
        respondidos_2016 += 1

total_2015 = 0
respondidos_2015 = 0

for index in df_2015.index:
    if df_2015.loc[index, 'Saneamento']['Consumo médio per capita'] != None:
        total_2015 += df_2015.loc[index, 'Saneamento']['Consumo médio per capita']
        respondidos_2015 += 1
        
consumo_y = [total_2015/respondidos_2015,
         total_2016/respondidos_2016,
         total_2017/respondidos_2017]
    
consumo = go.Scatter(x = anos, y = consumo_y, mode = 'lines + markers')

layout_consumo = go.Layout(title={'text':'Consumo médio per capita de água por dia no estado de São Paulo', 
                           'font':{'family': "Times New Roman", "size": 30 },
                           'x': 0.5, 'y': 0.9},
                   yaxis={'title':'Consumo médio (l/hab./dia)'},
                   xaxis={'title': 'Anos', 'tickmode': 'linear', 'dtick':1},
                       paper_bgcolor='rgba(0,0,0,0)',
                       font = dict(color = '#ecf0f1'))

fig9 = go.Figure(data = [consumo], layout = layout_consumo)
#plot(fig9)

#Taxa pop atendida 
total_2017 = 0
respondidos_2017 = 0

for index in df_2017.index:
    if df_2017.loc[index, 'Saneamento']['Taxa de pop atendida'] != None:
        total_2017 += df_2017.loc[index, 'Saneamento']['Taxa de pop atendida']
        respondidos_2017 += 1


total_2016 = 0
respondidos_2016 = 0

for index in df_2016.index:
    if df_2016.loc[index, 'Saneamento']['Taxa de pop atendida'] != None:
        total_2016 += df_2016.loc[index, 'Saneamento']['Taxa de pop atendida']
        respondidos_2016 += 1

total_2015 = 0
respondidos_2015 = 0

for index in df_2015.index:
    if df_2015.loc[index, 'Saneamento']['Taxa de pop atendida'] != None:
        total_2015 += df_2015.loc[index, 'Saneamento']['Taxa de pop atendida']
        respondidos_2015 += 1

saneamento_y = [total_2015/respondidos_2015,
         total_2016/respondidos_2016,
         total_2017/respondidos_2017]

saneamento = go.Scatter(x = anos, y = saneamento_y, mode = 'lines + markers')

layout_saneamento = go.Layout(title={'text':'Média da taxa da população atendida com abastecimento de água no estado de São Paulo', 
                           'font':{'family': "Times New Roman", "size": 30 },
                           'x': 0.5, 'y': 0.9},
                   yaxis={'title':'Índice de atendimento total de água (%)'},
                   xaxis={'title': 'Anos', 'tickmode': 'linear', 'dtick':1},
                       paper_bgcolor='rgba(0,0,0,0)',
                       font = dict(color = '#ecf0f1'))

fig10 = go.Figure(data = [saneamento], layout = layout_saneamento)        
#plot(fig10)


fig1.write_image("./client/src/graphs/estado/donut_2017.png", width = 1500, height = 700, scale = 2)
fig2.write_image("./client/src/graphs/estado/donut_2016.png", width = 1500, height = 700, scale = 2)
fig3.write_image("./client/src/graphs/estado/donut_2015.png", width = 1000, height = 700, scale = 2)
fig4.write_image("./client/src/graphs/estado/coleta_rdo_sp.png", width = 1500, height = 700, scale = 2)
fig5.write_image("./client/src/graphs/estado/massa_coletada_sp.png", width = 1500, height = 700, scale = 2)
fig6.write_image("./client/src/graphs/estado/recup_reciclaveis_sp.png", width = 1000, height = 700, scale = 2)
fig7.write_image("./client/src/graphs/estado/massa_via_seletiva_sp.png", width = 1500, height = 700, scale = 2)
fig8.write_image("./client/src/graphs/estado/pop_beneficiada_sp.png", width = 1500, height = 700, scale = 2)
fig9.write_image("./client/src/graphs/estado/consumo_medio_sp.png", width = 1500, height = 700, scale = 2)
fig10.write_image("./client/src/graphs/estado/taxa_pop_atendida_sp.png", width = 1500, height = 700, scale = 2)


        