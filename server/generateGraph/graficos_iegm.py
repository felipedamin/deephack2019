# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 20:58:15 2019

@author: icaro
"""
import pandas as pd
from plotly.offline import plot
import plotly.graph_objs as go

df_2018 = pd.read_json("./server/database/iegm/2018iegm.json")
df_2017 = pd.read_json("./server/database/iegm/2017iegm.json")
df_2016 = pd.read_json("./server/database/iegm/2016iegm.json")
df_2015 = pd.read_json("./server/database/iegm/2015iegm.json")


p_estruturais = ['A prefeitura possui Plano de Gestão de Resíduos da Construção Civil elaborado e implantado de acordo com a resolução CONAMA 307/2002 e suas alterações?',
                 'A prefeitura possui alguma estrutura organizacional para tratar de assuntos ligados ao Meio Ambiente Municipal?',
                 'Não há mais catadores de materiais recicláveis no aterro municipal.']
p_residuos = ['O plano municipal de Gestão Municipal de Resíduos Sólidos já está em vigor?',
              'A prefeitura municipal realiza a coleta seletiva de resíduos sólidos?',
              'O município já parou de lançar, a céu aberto (lixões), seus resíduos sólidos?',
              'Antes de aterrar o lixo, o município realiza algum tipo de processamento de resíduos?']
p_cetesb = ['Existe licença de operação da CETESB para a área de aterro?']
p_educativo = ['A prefeitura municipal estimula entre seus órgãos e entidades de sua responsabilidade projetos e/ou ações que promovam o uso racional de recursos naturais?',
               'A prefeitura possui ou participa de algum programa ou ação que promovam a melhoria contínua da qualidade ambiental no município?']

anos = [2015, 2016, 2017, 2018]
#Estrutural 

estr_2018 = {}
estr_2017 = {}
estr_2016 = {}
estr_2015 = {}

def newGraficoIegm():
    for pergunta in p_estruturais:
        v_2018 = sum(df_2018[pergunta]) if pergunta in df_2018.columns else 0
        v_2017 = sum(df_2017[pergunta]) if pergunta in df_2017.columns else 0
        v_2016 = sum(df_2016[pergunta]) if pergunta in df_2016.columns else 0
        v_2015 = sum(df_2015[pergunta]) if pergunta in df_2015.columns else 0
        estr_2018[pergunta] = v_2018
        estr_2017[pergunta] = v_2017
        estr_2016[pergunta] = v_2016
        estr_2015[pergunta] = v_2015


    trace1 = go.Bar(x = anos,
                    y = [estr_2015[p_estruturais[0]], estr_2016[p_estruturais[0]], estr_2017[p_estruturais[0]], estr_2018[p_estruturais[0]]],
                    name = 'A prefeitura possui Plano de Gestão de Resíduos da Construção Civil elaborado e implantado de acordo com a resolução CONAMA 307/2002?',
                    marker = {'color': '#1f77b4'})

    trace2 = go.Bar(x = anos,
                    y = [estr_2015[p_estruturais[1]], estr_2016[p_estruturais[1]], estr_2017[p_estruturais[1]], estr_2018[p_estruturais[1]]],
                    name = p_estruturais[1],
                    marker = {'color': '#d62728'})
                            
    trace3 = go.Bar(x = anos,
                    y = [estr_2015[p_estruturais[2]], estr_2016[p_estruturais[2]], estr_2017[p_estruturais[2]], estr_2018[p_estruturais[2]]],
                    name = p_estruturais[2],
                    marker = {'color': '#9467bd'})

    layout1 = go.Layout(title={'text':'Iegm - Estruturais', 
                            'font':{'family': "Times New Roman", "size": 40 },
                            'x': 0.5, 'y': 0.9},
                        legend=dict(
                                x=0,
                                y=-0.3,
                                traceorder="normal",
                                font=dict(
                                    family="sans-serif",
                                    size=20,
                                    color="black"
                                ),
                                bordercolor="Black",
                                borderwidth=2))

    fig1 = go.Figure(data = [trace1, trace2, trace3], layout = layout1)
    #plot(fig1)


    #Residuos

    res_2018 = {}
    res_2017 = {}
    res_2016 = {}
    res_2015 = {}

    for pergunta in p_residuos:
        v_2018 = sum(df_2018[pergunta]) if pergunta in df_2018.columns else 0
        v_2017 = sum(df_2017[pergunta]) if pergunta in df_2017.columns else 0
        v_2016 = sum(df_2016[pergunta]) if pergunta in df_2016.columns else 0
        v_2015 = sum(df_2015[pergunta]) if pergunta in df_2015.columns else 0
        res_2018[pergunta] = v_2018
        res_2017[pergunta] = v_2017
        res_2016[pergunta] = v_2016
        res_2015[pergunta] = v_2015


    trace1 = go.Bar(x = anos,
                    y = [res_2015[p_residuos[0]], res_2016[p_residuos[0]], res_2017[p_residuos[0]], res_2018[p_residuos[0]]],
                    name = p_residuos[0],
                    marker = {'color': '#1f77b4'})

    trace2 = go.Bar(x = anos,
                    y = [res_2015[p_residuos[1]], res_2016[p_residuos[1]], res_2017[p_residuos[1]], res_2018[p_residuos[1]]],
                    name = p_residuos[1],
                    marker = {'color': '#d62728'})
                            
    trace3 = go.Bar(x = anos,
                    y = [res_2015[p_residuos[2]], res_2016[p_residuos[2]], res_2017[p_residuos[2]], res_2018[p_residuos[2]]],
                    name = p_residuos[2],
                    marker = {'color': '#9467bd'})
                                
    trace4 = go.Bar(x = anos,
                    y = [res_2015[p_residuos[3]], res_2016[p_residuos[3]], res_2017[p_residuos[3]], res_2018[p_residuos[3]]],
                    name = p_residuos[3],
                    marker = {'color': '#17becf'})

    layout2 = go.Layout(title={'text':'Iegm - Resíduos', 
                            'font':{'family': "Times New Roman", "size": 40 },
                            'x': 0.5, 'y': 1},
                        legend=dict(x = 0.04, y= 1,
                                traceorder="normal",
                                font=dict(
                                    family="sans-serif",
                                    size=19,
                                    color="black"
                                ),
                                bordercolor="Black",
                                borderwidth=2))

    fig2 = go.Figure(data = [trace1, trace2, trace3, trace4], layout = layout2)
    #plot(fig2)

    #CETESB
    cetesb_2018 = sum(df_2018[p_cetesb[0]]) if p_cetesb[0] in df_2018.columns else 0
    cetesb_2017 = sum(df_2017[p_cetesb[0]]) if p_cetesb[0] in df_2017.columns else 0
    cetesb_2016 = sum(df_2016[p_cetesb[0]]) if p_cetesb[0] in df_2016.columns else 0
    cetesb_2015 = sum(df_2015[p_cetesb[0]]) if p_cetesb[0] in df_2015.columns else 0


    trace1 = go.Bar(x = [2017, 2018],
                    y = [cetesb_2017, cetesb_2018],
                    name = p_cetesb[0], width = 0.25,
                    marker = {'color': '#d62728'})
                            
    layout3 = go.Layout(title={'text':'Existe licença de operação da CETESB para a área de aterro?', 
                            'font':{'family': "Times New Roman", "size": 20 },
                            'x': 0.5, 'y': 0.9},
                        legend=dict(x = 0, y= 0,
                                traceorder="normal",
                                font=dict(
                                    family="sans-serif",
                                    size=12,
                                    color="black"
                                ),
                                bordercolor="Black",
                                borderwidth=2),
                        xaxis={'dtick':1},
                        width = 900)                          
    fig3 = go.Figure(data = [trace1], layout = layout3)
    #plot(fig3)


    # Educativo

    educ_2018 = {}
    educ_2017 = {}
    educ_2016 = {}
    educ_2015 = {}

    for pergunta in p_educativo:
        v_2018 = sum(df_2018[pergunta]) if pergunta in df_2018.columns else 0
        v_2017 = sum(df_2017[pergunta]) if pergunta in df_2017.columns else 0
        v_2016 = sum(df_2016[pergunta]) if pergunta in df_2016.columns else 0
        v_2015 = sum(df_2015[pergunta]) if pergunta in df_2015.columns else 0
        educ_2018[pergunta] = v_2018
        educ_2017[pergunta] = v_2017
        educ_2016[pergunta] = v_2016
        educ_2015[pergunta] = v_2015


    trace1 = go.Bar(x = anos,
                    y = [educ_2015[p_educativo[0]], educ_2016[p_educativo[0]], educ_2017[p_educativo[0]], educ_2018[p_educativo[0]]],
                    name = 'A prefeitura municipal estimula entre seus órgãos de sua responsabilidade ações que promovam o uso racional de recursos naturais?',
                    marker = {'color': '#1f77b4'})


    trace2 = go.Bar(x = anos,
                    y = [educ_2015[p_educativo[1]], educ_2016[p_educativo[1]], educ_2017[p_educativo[1]], educ_2018[p_educativo[1]]],
                    name = p_educativo[1],
                    marker = {'color': '#bcbd22'})
                            
    layout4 = go.Layout(title={'text':'Iegm - Educação', 
                            'font':{'family': "Times New Roman", "size": 40 },
                            'x': 0.5, 'y': 0.9},
                        legend=dict(x = 0, y = -0.2,
                                traceorder="normal",
                                font=dict(
                                    family="sans-serif",
                                    size=20,
                                    color="black"
                                ),
                                bordercolor="Black",
                                borderwidth=2))

    fig4 = go.Figure(data = [trace1, trace2], layout = layout4)
    #plot(fig4)

    fig1.write_image("./client/src/graphs/IEGM/fig1.png", width = 1600, height = 900)
    fig2.write_image("./client/src/graphs/IEGM/fig2.png", width = 1600, height = 900)
    fig3.write_image("./client/src/graphs/IEGM/fig3.png", width = 1600, height = 900)
    fig4.write_image("./client/src/graphs/IEGM/fig4.png", width = 1600, height = 900)

newGraficoIegm()