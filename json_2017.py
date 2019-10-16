# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 15:59:30 2019

@author: icaro
"""

import pandas as pd
import numpy as np 

indicadores_2017 = pd.read_excel("C:/Users/icaro/Desktop/Hackaton/Dados tratados/Residuos/Indicadores/t_indicadores_2017.xls")
informacoes_2017 = pd.read_excel("C:/Users/icaro/Desktop/Hackaton/Dados tratados/Residuos/Informações/t_planilha_informacoes_2017.xls")
saneamento_2017 = pd.read_excel("C:/Users/icaro/Desktop/Hackaton/Dados tratados/Saneamento - SNIS/t_saneamento_2017.xls")

#já estão todas como float
columns_to_keep_ind = ['Código do município', 'Município', 'UF','Tx cobertura da coleta RDO em relação à pop. total(%)',
                   'Massa [RDO+RPU] coletada per capita em relação à população total atendida (Kg/(hab.x dia))',
                   'Taxa de recuperação de recicláveis em relação à quantidade de RDO e RPU(%)',
                   'Massa per capita recolhida via coleta seletiva(Kg/(hab. x ano))']

columns_to_drop_ind = []

columns_to_keep_saneamento = ['Código do município', 'Município',
                              'População total do município do ano de referência\nSNIS 2017',
                              'AG001 - População total atendida com abastecimento de água',
                              'IN022 - Consumo médio percapita de água',
                              'IN055 - Índice de atendimento total de água']
columns_to_drop_saneamento = []

#excluindo colunas desnecessárias em saneamento e indicadores
for column in indicadores_2017.columns:
    if column not in columns_to_keep_ind:
        columns_to_drop_ind.append(column)

for column in saneamento_2017.columns:
    if column not in columns_to_keep_saneamento:
        columns_to_drop_saneamento.append(column)

indicadores_2017.drop(columns = columns_to_drop_ind, inplace = True)
saneamento_2017.drop(columns = columns_to_drop_saneamento, inplace = True)

'''
#tamanho saneamento > tamanho indicadores=informacoes
df_2017 = pd.DataFrame({'Código do município':saneamento_2017['Código do município'], 
                        'Município': saneamento_2017['Município'], 
                        'Resíduos': [0 for x in range(len(saneamento_2017))],
                        'Saneamento': [0 for x in range(len(saneamento_2017))]})
'''

#indexando as tabelas pelo código do município
indicadores_2017['Código do município'].astype(int)
informacoes_2017['Código do município'].astype(int)
saneamento_2017['Código do município'].astype(int)    
#df_2017['Código do município'].astype(int)
indicadores_2017.set_index('Código do município', inplace = True)
informacoes_2017.set_index('Código do município', inplace = True)
saneamento_2017.set_index('Código do município', inplace = True)
#df_2017.set_index('Código do município', inplace = True)

#convertendo as strings de saneamento em floats
for ind in saneamento_2017.index:
    nb1 = saneamento_2017.loc[ind, 'IN022 - Consumo médio percapita de água']
    nb2 = saneamento_2017.loc[ind, 'IN055 - Índice de atendimento total de água']
    saneamento_2017.loc[ind, 'IN022 - Consumo médio percapita de água'] = float(nb1.replace(',','.'))
    saneamento_2017.loc[ind, 'IN055 - Índice de atendimento total de água'] = float(nb2.replace(',','.'))

#saneamento_2017['IN022 - Consumo médio percapita de água'].astype(float)
#saneamento_2017['IN055 - Índice de atendimento total de água'].astype(float)

#gerando a tabela ao modo de leitura json
#se a cidade nao está em alguma das tabelas, é gerando um NaN
#OBS: Como há mais cidades na planilha de saneamento, colocamos ela como base para iteração
lines_residuos = []
lines_saneamento = []
for codigo in list(saneamento_2017.index):
    if(codigo in list(indicadores_2017.index)):
        dic1 = {'Taxa coleta RDO': indicadores_2017.loc[codigo,'Tx cobertura da coleta RDO em relação à pop. total(%)'],
                               'Massa coletada': indicadores_2017.loc[codigo, 'Massa [RDO+RPU] coletada per capita em relação à população total atendida (Kg/(hab.x dia))'],
                               'Taxa de recuperação de recicláveis': indicadores_2017.loc[codigo, 'Taxa de recuperação de recicláveis em relação à quantidade de RDO e RPU(%)'],
                               'Massa recolhida via coleta seletiva':indicadores_2017.loc[codigo, 'Massa per capita recolhida via coleta seletiva(Kg/(hab. x ano))'], 
                               'Taxa pop atendida com coleta': informacoes_2017.loc[codigo, 'População atendida declarada']/informacoes_2017.loc[codigo, 'Total População']}
        
        lines_residuos.append(dic1)
    else:
        dic1 = {'Taxa coleta RDO': np.nan,
                               'Massa coletada': np.nan,
                               'Taxa de recuperação de recicláveis': np.nan,
                               'Massa recolhida via coleta seletiva':np.nan, 
                               'Taxa pop atendida com coleta': np.nan}
        lines_residuos.append(dic1)

        
    dic2 = {'Consumo médio per capita': saneamento_2017.loc[codigo, 'IN022 - Consumo médio percapita de água'],
                                              'Taxa de pop atendida': saneamento_2017.loc[codigo, 'IN055 - Índice de atendimento total de água']}
    lines_saneamento.append(dic2)
    

df_2017 = pd.DataFrame({'Resíduos': lines_residuos,
                        'Saneamento': lines_saneamento, 
                         'Município': saneamento_2017['Município']})

df_2017.set_index("Município", inplace = True)

#df_2017.to_excel("C:/Users/icaro/Desktop/Hackaton/Dados tratados/Json/2017.xls")
#df_2017.to_json("C:/Users/icaro/Desktop/Hackaton/Dados tratados/Json/2017.json", orient = 'index')

