# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 20:20:47 2019

@author: icaro
"""

import pandas as pd
import string

df = pd.read_csv("C:/Users/icaro/Desktop/Hackaton/Dados abertos/painel-saneamento-brasil-2017.csv", sep=';', encoding = 'latin-1')
df['Estado'].replace({'SP, BR': 'SP'}, inplace=True)

df = df[df['Estado'] == 'SP']

columns_to_drop = ['Cód. Município\n6 dígitos', 'Latitude', 'Longitude', 'Capital', 'Estado 2', 
                   'Macrorregião', 'RM, RIDE ou Aglomeração Urbana', 'Norma Legal', 'Código do Prestador',
                   'AG012 - Volume de água macromedido', 'AG015 - Volume de água tratada por simples desinfecção',
                   'AG017 - Volume de água bruta exportado', 'AG018 - Volume de água tratada importado', 
                   'AG019 - Volume de água tratada exportado', 'AG020 - Volume micromedido nas economias residenciais ativas de água',
                   'AG022 - Quantidade de economias residenciais ativas de água micromedidas', 'AG022A - Quantidade de economias residenciais ativas de água micromedidas no ano anterior ao de referência.',
                   'ES009 - Quantidade de ligações totais de esgotos', 'ES009A - Quantidade de ligações totais de esgoto no ano anterior ao de referência.',
                   'ES012 - Volume de esgoto bruto exportado', 'ES013 - Volume de esgotos bruto importado', 'ES014 - Volume de esgoto importado tratado nas instalações do importador', 
                   'ES015 - Volume de esgoto bruto exportado tratado nas instalações do importador', 'FN038 - Receita operacional direta - esgoto bruto importado',  
                   'QD001 - Tipo de atendimento da portaria sobre qualidade da água', 'QD006 - Quantidade de amostras para cloro residual (analisadas)', 'QD007 - Quantidade de amostras para cloro residual com resultados fora do padrão',
                   'QD008 - Quantidade de amostras para turbidez (analisadas)', 'QD009 - Quantidade de amostras para turbidez fora do padrão', 'QD011 - Quantidades de extravasamentos de esgotos registrados', 
                   'QD019 - Quantidade mínima de amostras para turbidez (obrigatórias)', 'QD020 - Quantidade mínima de amostras para cloro residual (obrigatórias)', 'QD026 - Quantidade de amostras para coliformes totais (analisadas)', 
                   'QD027 - Quantidade de amostras para coliformes totais com resultados fora do padrão', 'QD028 - Quantidade mínima de amostras para coliformes totais (obrigatórias)', 'IN013 - Índice de perdas faturamento', 'IN015 - Índice de coleta de esgoto',
                   'IN028 - Índice de faturamento de água', 'IN046 - Índice de esgoto tratado referido à água consumida', 'IN049 - Índice de perdas na distribuição', 'IN050 - Índice bruto de perdas lineares', 'IN051 - Índice de perdas por ligação',
                   'IN057 - Índice de fluoretação de água', 'IN075 - Incidência das análises de cloro residual fora do padrão', 'IN076 - Incidência das análises de turbidez fora do padrão', 'IN077 - Duração média dos reparos de extravasamentos de esgotos', 
                   'IN079 - Índice de conformidade da quantidade de amostras - cloro residual', 'IN080 - Índice de conformidade da quantidade de amostras - turbidez', 'IN082 - Extravasamentos de esgotos por extensão de rede', 'IN084 - Incidência das análises de coliformes totais fora do padrão', 
                   'IN085 - Índice de conformidade da quantidade de amostras - coliformes totais', 'Codigo Estacao', 'Nome Estacao', 'Rio_Nome', 'Data2', 'Hora', 'Temp da Amostra', 'pH', 'Turbidez', 'DQO', 'DBO', 'OD', 'IQA', 'Solidos Totais', 'Solidos em Suspensao Totais', 'Solidos Dissolvidos Totais', 
                   'Nitrogenio Total', 'Fosforo Total']

df.drop(columns=columns_to_drop, inplace = True)

lines_to_drop = []
for ind in df.index:
    if (df['Situação SNIS - água'][ind] == 'Não declarante') :
        lines_to_drop.append(ind)

df.drop(lines_to_drop, inplace = True)
       
df.to_csv('C:/Users/icaro/Desktop/Hackaton/Dados tratados/t_saneamento_2017.csv')