import pandas as pd

## db = pd.read_csv('./portofeliz/despesas-porto-feliz-2018(2).csv', sep=';', encoding='latin-1')

db = pd.read_csv('iegm.csv', sep=';', encoding='latin-1', low_memory=False)

for i in db.head():
    print(i, end=', ')
print('\n')


perguntas = {}
'''
for (pergunta, resposta) in (db['texto_pergunta_genérica'], db['valor_resposta']):
    perguntas.add(pergunta, [])
    if resposta not in perguntas[pergunta]:
        perguntas[pergunta].value.append(resposta)
'''

'''
for i in range(len(db['texto_pergunta_genérica'])):
    pergunta = db['texto_pergunta_genérica'][i]
    resposta = db['rotulo_resposta'][i]
    
    if pergunta not in perguntas:
        perguntas[pergunta] =  []
    if resposta not in perguntas[pergunta]:
        perguntas[pergunta].append(resposta)
           
print(perguntas.keys())
'''

lista = []
for i in range(len(db['municipio'])):
    if db['municipio'][i] == 'Porto Feliz':
        if db['texto_pergunta_genérica'][i] not in lista:
            lista.append(db['texto_pergunta_genérica'][i])

for i in lista:
    print(i)    

## print(perguntas)
## print(perguntas)
## ['ano_exercicio', 'ds_municipio', 'ds_orgao', 'mes_referencia', 'tp_despesa', 'vl_despesa', 'ds_funcao_governo', 'ds_subfuncao_governo', 'cd_programa', 'cd_acao', 'ds_fonte_recurso', 'ds_cd_aplicacao_fixo', 'ds_modalidade_lic']