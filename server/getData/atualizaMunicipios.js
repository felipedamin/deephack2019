const Cidade = require('../database/models/cidade')
const cods = require('../database/codMunicipioIbge.json')
const municipios = require('../database/municipios.json')

async function atualizaMunicipios() {
  var salvos = 0;
  var erros = 0;
  try {
    for (mun in municipios) {
      if (Object.values(cods).includes(municipios[mun].municipio_extenso)) {
        var index = getIndex(municipios[mun].municipio_extenso)
        if (index != -1) {
          await new Cidade({
            municipio: municipios[mun].municipio,
            municipio_extenso: municipios[mun].municipio_extenso,
            cod_ibge: Object.keys(cods)[mun],
          }).save()
            .then(() => {
              salvos += 1;
            })
        }
      }
      else {
        erros += 1
      }
    }
    console.log(`Foram atualizados ${salvos} municipios, ${erros} não deram certo`);
  } catch (err) {
    console.log('erro ao atualizar os municipios e seus codigos no BD:', err)
  }
}

function getIndex(cidade) {
  for (i in cods) {
    if (cods[i] == cidade) {
      return i;
    }
  }
  return -1;
}

module.exports = atualizaMunicipios