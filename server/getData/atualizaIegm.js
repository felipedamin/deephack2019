const Cidade = require('../database/models/cidade');

const iegm2014 = require('../database/iegm2014.json');

// Os municipios ja devem estar no BD com seus respectivos codigos
// Se nao estiverem, chamar a atualizaMunicipios
// é so acessar /database/municipios

/*
var query = { name: 'borne' };
Model.findOneAndUpdate(query, { name: 'jason bourne' }, options, callback)
*/

const ANOS = [2014]
const iegms = [iegm2014]
const CODS_PERGUNTAS = ["M05Q00100", "M05Q00200", "M05Q00300", "M05Q00600", "M05Q00501", "M05Q00800", "M05Q00900"]

async function atualizaIegm() {
  try {
    for (let iegmDoAno of iegms) {
      for (let pergunta of CODS_PERGUNTAS) {
        for (i in iegmDoAno[pergunta]) {
          await Cidade.findOneAndUpdate(
            { cod_ibge: i }, {
            $push: {
              iegm:
              {
                ano: ANOS[iegms.indexOf(iegmDoAno)],
                pergunta: pergunta,
                resposta: iegmDoAno[pergunta][i]
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