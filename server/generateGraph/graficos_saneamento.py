# -*- coding: utf-8 -*-:
"""
Created on Tue Oct 15 02:21:51 2019

@author: icaro
"""

import pandas as pd
from plotly.offline import plot
import plotly.graph_objs as go

data_2017 = pd.read_json("./server/database/saneamentoResiduos/2017.json", orient = 'index')
data_2016 = pd.read_json("./server/database/saneamentoResiduos/2016.json", orient = 'index')
data_2015 = pd.read_json("./server/database/saneamentoResiduos/2015.json", orient = 'index')

anos = [2015,2016,2017]


def newGraficoSaneamento(cidade):
    #Consumo médio per capita por cidade
    consumo_y = [data_2015.loc[cidade, 'Saneamento']['Consumo médio per capita'],
            data_2016.loc[cidade, 'Saneamento']['Consumo médio per capita'],
            data_2017.loc[cidade, 'Saneamento']['Consumo médio per capita']]
    consumo = go.Scatter(x = anos, y = consumo_y, mode = 'lines + markers')
    
    layout_consumo = go.Layout(title={'text':str('Consumo médio per capita de água por dia em '+cidade), 
                           'font':{'family': "Times New Roman", "size": 14 },
                           'x': 0.5, 'y': 0.9},
                        yaxis={'title':'Consumo médio (l/hab./dia)'},
                        xaxis={'title': 'Anos', 'tickmode': 'linear', 'dtick':1},
                        paper_bgcolor='rgba(0,0,0,0)',
                        font = dict(color = '#ecf0f1'))

    fig1 = go.Figure(data = [consumo], layout = layout_consumo)
    #plot(fig1)

    #Taxa pop atendida com saneamento
    saneamento_y = [data_2015.loc[cidade, 'Saneamento']['Taxa de pop atendida'],
            data_2016.loc[cidade, 'Saneamento']['Taxa de pop atendida'],
            data_2017.loc[cidade, 'Saneamento']['Taxa de pop atendida']]
    saneamento = go.Scatter(x = anos, y = saneamento_y, mode = 'lines + markers')

    layout_saneamento = go.Layout(title={'text':str('Taxa da população atendida em relação à população residente em '+cidade), 
                           'font':{'family': "Times New Roman", "size": 14 },
                           'x': 0.5, 'y': 0.9},
                        yaxis={'title':'Índice de atendimento total de água (%)'},
                        xaxis={'title': 'Anos', 'tickmode': 'linear', 'dtick':1},
                        paper_bgcolor='rgba(0,0,0,0)',
                        font = dict(color = '#ecf0f1'))

    fig2 = go.Figure(data = [saneamento], layout = layout_saneamento)
    #plot(fig2)

    fig1.write_image(str("./client/src/graphs/saneamento/"+cidade+"-fig1.png"), width = 600, height = 450, scale = 2)
    fig2.write_image(str("./client/src/graphs/saneamento/"+cidade+"-fig2.png"), width = 600, height = 450, scale = 2)
