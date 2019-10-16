# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 23:52:51 2019

@author: icaro
"""

import pandas as pd
import numpy as np


energia_co2 = pd.read_excel("C:/Users/icaro/Desktop/Hackaton/Dados tratados/Energia/energia_co2_filtrado.xls")

df = energia_co2
df.drop(columns = ['Unnamed: 0', 'Estado'], inplace = True)

df.set_index('Município', inplace = True)

#line_mode = {'Petróleo e derivados': 0, 'Biomassa e derivados':0, 'Rede pública':0,
#       'Gás Natural e derivados':0,
#       'Autoprodução(Eólica, Hidrelétrica, Fotovoltaica, Termoelétrica)':0,
#       'Outros':0, 'Carvão Mineral e derivados':0}

lines = []
anos = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
    
df2 = pd.DataFrame({'Município': df.index.unique()})
df2.set_index('Município', inplace = True)

for ano in anos:
    lines = []    
    for i in df.index.unique():
        dic =  {'Petróleo e derivados - t/m3': 0, 'Biomassa e derivados - TON': 0,
       'Rede pública': 0, 'Petróleo e derivados - TON': 0, 'Gás Natural (Seco)': 0,
       'Autoprodução(Eólica, Hidrelétrica, Fotovoltaica, Termoelétrica)': 0,
       'Gás Natural e derivados - TON': 0, 'Biomassa e derivados - t/m3': 0,
       'Outros - TON': 0, 'Carvão Mineral e derivados': 0, 'Outros - t/m3': 0, 
       'Emissão de CO2': 0}
        lines.append(dic)
    df2[ano] = lines

#emissao = [0 for x in range(len(df.index.unique()))]
#df2['Emissão de CO2'] = emissao
  
for cidade in df.index.unique():
    df_copy = df.copy()
    df_copy = df_copy[df_copy.index == cidade]
    #df2.loc[cidade, 'Emissão de CO2'] = np.nansum(df_copy['Emissões de CO2 '])
    for tipo in df['Tipo de Fonte Energética'].unique():    
        df_copy2 = df_copy[df_copy['Tipo de Fonte Energética'] == tipo]
        for ano in df_copy2['Ano'].unique():
            df_copy3 = df_copy2[df_copy2['Ano'] == ano]
            nb_quant = np.nansum(df_copy3['Quantidade Consumida'])
            df2.loc[cidade, ano][tipo] = nb_quant
            

for cidade in df.index.unique():
    df_copy = df.copy()
    df_copy = df_copy[df_copy.index == cidade]
    #df2.loc[cidade, 'Emissão de CO2'] = np.nansum(df_copy['Emissões de CO2 '])
    for ano in df_copy['Ano'].unique():
        df_copy2 = df_copy[df_copy['Ano'] == ano]
        nb_emis= np.nansum(df_copy2['Emissões de CO2 '])
        df2.loc[cidade, ano]['Emissão de CO2'] = nb_emis


df2.to_json("C:/Users/icaro/Desktop/Hackaton/Dados tratados/Energia/energia_co2.json", orient = 'index')