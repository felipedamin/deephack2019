const Cidade = require('../database/models/cidade');

const iegm2014 = require('../database/iegm/2014iegm.json');
const iegm2015 = require('../database/iegm/2015iegm.json');
const iegm2016 = require('../database/iegm/2016iegm.json');
const iegm2017 = require('../database/iegm/2017iegm.json');
const iegm2018 = require('../database/iegm/2018iegm.json');

// Os municipios ja devem estar no BD com seus respectivos codigos
// Se nao estiverem, chamar a atualizaMunicipios
// é so acessar /database/municipios

const ANOS = [2014, 2015, 2016, 2017, 2018]
const iegms = [iegm2014, iegm2015, iegm2016, iegm2017, iegm2018]

async function atualizaIegm() {
  try {
    for (let iegmDoAno of iegms) {
      for (index in iegmDoAno.cod_ibge) {
        let cod_ibge = iegmDoAno["cod_ibge"][index]
        for (pergunta in iegmDoAno) {
          if (pergunta !== "cod_ibge" && pergunta !== "Municipio")
          await Cidade.findOneAndUpdate(
            { cod_ibge: cod_ibge }, {
            $push: {
              iegm:
              {
                ano: ANOS[iegms.indexOf(iegmDoAno)],
                pergunta: pergunta,
                resposta: iegmDoAno[pergunta][index]
              }
            }
          })
        }
      }
    }
    console.log('iegm atualizado');
  } catch (err) {
    console.log('Erro ao atulizar as perguntas do IEGM:', err)
  }
}

module.exports = atualizaIegm