import graficos_iegm
import graficos_residuos
import graficos_saneamento
import json

municipios = json.load(open('./server/database/municipios.json', 'r'))

graficos_iegm.newGraficoIegm()

gerados = 0
erros = 0

for i in range(len(municipios)):
    print(municipios[i]['municipio_extenso'])
    try:
        graficos_residuos.newGraficoResiduos(municipios[i]['municipio_extenso'])
        graficos_saneamento.newGraficoSaneamento(municipios[i]['municipio_extenso'])
        gerados += 1
    except:
        print('error')
        erros += 1

print('Geramos graficos para '+gerados+' cidades! Outras '+erros+' deram erro.')