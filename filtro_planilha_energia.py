# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 18:24:04 2019

@author: icaro
"""
import pandas as pd
import unidecode

df = pd.read_csv("C:/Users/icaro/Desktop/Hackaton/Dados tratados/Energia/energia_co2_empresas.csv", sep = ';')
cidades = pd.read_excel('C:/Users/icaro/Desktop/Hackaton/Dados tratados/cidades_sp.xls')

def remove_accents(a):
    return unidecode.unidecode(a)

columns_to_keep = [ 'Estado', 'Município', 'Ano',
       'Tipo de Fonte Energética', 'Quantidade Consumida', 'Unidade de Medida',
       'Energia', 'Emissões de CO2 ']

columns_to_drop= []
for column in df.columns:
    if column not in columns_to_keep:
        columns_to_drop.append(column)

df.drop(columns = columns_to_drop, inplace = True)

df = df[df['Estado'] == 'SAO PAULO']

#df = df[df['Município'] != 'SAO PAULO']

df['Quantidade Consumida'] = df['Quantidade Consumida'].str.replace('.','').str.replace(',','.')
df['Quantidade Consumida'] = pd.to_numeric(df['Quantidade Consumida'])
df['Energia'] = df['Energia'].str.replace('.','').str.replace(',','.')
df['Energia'] = pd.to_numeric(df['Energia'])
df['Emissões de CO2 '] = df['Emissões de CO2 '].str.replace('.','').str.replace(',','.')
df['Emissões de CO2 '] = pd.to_numeric(df['Emissões de CO2 '])


#df.to_excel("C:/Users/icaro/Desktop/Hackaton/Dados tratados/Energia/t_energia_co2_empresas_2.xls")


tipos_fonte = df['Tipo de Fonte Energética'].unique()

quant_consumida = {}
unid_medida = {}
for fonte in tipos_fonte:
    df_1 = df.copy()
    df_1 = df[df['Tipo de Fonte Energética'] == fonte]
    nb = sum(df_1['Quantidade Consumida'])
    df_1.reset_index(inplace = True)
    uni = df_1.loc[0,'Unidade de Medida']
    quant_consumida[fonte] = nb
    unid_medida[fonte] = uni

sorted_d = sorted(quant_consumida.items(), key=lambda x: x[1])

'''
df.replace(['Gás de Refinaria', 'Óleo de Xisto', 'Nafta', 'Ceras Parafínicas', 'Querosene de Aviação',
            'Gás de Forno de Aciária a Oxigênio', 'Orimulsão', 'Gás de Alto-forno', 
            'Turfa', 'Xisto Betuminoso e Areias Asfálticas', 'Outro Combustível Não-Renovável',
            'Gás Manufaturado', 'Matérias-Primas para Refinaria', 'Querosene Iluminante',
            'Gasolina de Aviação', 'Gás de Coqueria', 'Alcatrão'], 'Outros', inplace = True)

df.replace(['Carvão Mineral - Aglomerados', 'Coque de Carvão Mineral', 'Carvão Mineral - Metalúrgico', 
               'Carvão Mineral - Vapor'], 'Carvão Mineral e derivados', inplace = True)

df.replace('Etano', 'Etanol', inplace = True)

df.replace(['Biomassa - Lenha','Biomassa - Serragem/Resíduos de Madeira',
            'Biomassa - Casca de Arroz', 'Biomassa - Biodiesel B100', 'Biomassa - Lã morta de Algodão',
            'Biomassa - Lixívia','Biomassa - Outro Biogás','Biomassa - Carvão Vegetal',
            'Biomassa - Álcool Etílico Anidro', 'Biomassa - Bagaço de Cana', 'Biomassa - Gases de Aterro',
            'Biomassa - Outro Combustível Renovável',  'Etanol'], 'Biomassa e derivados', inplace = True)

df.replace(['Gás Liquefeito de Petróleo (GLP)', 'Petróleo Bruto', 'Coque de Petróleo', 'Gasolina', 
            'Lubrificantes','Óleo Diesel', 'Óleo Combustível'], 'Petróleo e derivados', inplace = True)

df.replace(['Gás Natural (Seco)', 'Líquidos de Gás Natural', 'Gás Natural Úmido'], 
            'Gás Natural e derivados', inplace = True)

df.replace(['Eletricidade - Autoprodução - Eólica', 'Eletricidade - Autoprodução - Hidrelétrica',
            'Eletricidade - Autoprodução - Fotovoltaica', 'Eletricidade - Autoprodução - Termoelétrica'], 
            'Autoprodução(Eólica, Hidrelétrica, Fotovoltaica, Termoelétrica)',
            inplace = True)

df.replace('Eletricidade -  Rede Pública', 'Rede pública', inplace = True)
'''
df.replace(['Querosene de Aviação',
            'Querosene Iluminante',
            'Gasolina de Aviação'], 'Outros - t/m3', inplace = True)

df.replace(['Gás de Refinaria', 'Óleo de Xisto', 'Nafta', 'Ceras Parafínicas',
            'Gás de Forno de Aciária a Oxigênio', 'Orimulsão', 'Gás de Alto-forno', 
            'Turfa', 'Xisto Betuminoso e Areias Asfálticas', 'Outro Combustível Não-Renovável',
            'Gás Manufaturado', 'Matérias-Primas para Refinaria', 
            'Gás de Coqueria', 'Alcatrão'], 'Outros - TON', inplace = True)

df.replace(['Carvão Mineral - Aglomerados', 'Coque de Carvão Mineral', 'Carvão Mineral - Metalúrgico', 
               'Carvão Mineral - Vapor'], 'Carvão Mineral e derivados', inplace = True)

df.replace('Etano', 'Etanol', inplace = True)

df.replace(['Biomassa - Lenha','Biomassa - Serragem/Resíduos de Madeira',
            'Biomassa - Casca de Arroz', 'Biomassa - Lã morta de Algodão',
            'Biomassa - Lixívia','Biomassa - Outro Biogás','Biomassa - Carvão Vegetal',
            'Biomassa - Bagaço de Cana', 'Biomassa - Gases de Aterro',
            'Biomassa - Outro Combustível Renovável',  'Etanol'], 'Biomassa e derivados - TON', inplace = True)

df.replace(['Biomassa - Biodiesel B100',
            'Biomassa - Álcool Etílico Anidro'], 'Biomassa e derivados - t/m3', inplace = True)

df.replace(['Gasolina', 'Lubrificantes','Óleo Diesel'], 'Petróleo e derivados - t/m3', inplace = True)

df.replace(['Gás Liquefeito de Petróleo (GLP)', 'Petróleo Bruto', 'Coque de Petróleo', 
            'Óleo Combustível'], 'Petróleo e derivados - TON', inplace = True)

df.replace(['Líquidos de Gás Natural', 'Gás Natural Úmido'], 
            'Gás Natural e derivados - TON', inplace = True)

df.replace(['Eletricidade - Autoprodução - Eólica', 'Eletricidade - Autoprodução - Hidrelétrica',
            'Eletricidade - Autoprodução - Fotovoltaica', 'Eletricidade - Autoprodução - Termoelétrica'], 
            'Autoprodução(Eólica, Hidrelétrica, Fotovoltaica, Termoelétrica)',
            inplace = True)

df.replace('Eletricidade -  Rede Pública', 'Rede pública', inplace = True)

df['Município']  = df['Município'].apply(lambda x: x.title())
cidades['Nome do município']  = cidades['Nome do município'].apply(lambda x: x.title())
cidades['Nome do município'] = cidades['Nome do município'].apply(remove_accents)
df.replace({'Moji Mirim': 'Mogi Mirim', 'Embu': 'Embu-Guacu'}, inplace = True)

for ind in df.index:
    cidade = df.loc[ind, 'Município']
    if cidade == 'Nova Alvorada - RS':
        continue
    index = cidades.index[cidades['Nome do município'] == cidade][0]    
    df.loc[ind, 'Código do município'] = cidades.loc[index, 'Código do município']
    

df.sort_values('Município', inplace = True)      
df.to_excel("C:/Users/icaro/Desktop/Hackaton/Dados tratados/Energia/energia_co2_filtrado.xls")
