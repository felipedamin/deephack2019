const Cidade = require('../database/models/cidade');

const s_r2015 = require('../database/saneamentoResiduos/2015.json');
const s_r2016 = require('../database/saneamentoResiduos/2016.json');
const s_r2017 = require('../database/saneamentoResiduos/2017.json');

// Os municipios ja devem estar no BD com seus respectivos codigos
// Se nao estiverem, chamar a atualizaMunicipios
// basta GET em {link}/database/municipios

/*
var query = { name: 'borne' };
Model.findOneAndUpdate(query, { name: 'jason bourne' }, options, callback)
*/

const ANOS = [2015, 2016, 2017]
const S_Rs = [s_r2015, s_r2016, s_r2017]

async function atualizaSaneamentoResiduos() {
  try {
    for (let s_rDoAno of S_Rs) {
      //Atualiza saneamento
      for (index in s_rDoAno) {
        let cidade = s_rDoAno[index]
        for (pergunta in cidade.Saneamento) {
          await Cidade.findOneAndUpdate(
            { municipio_extenso: index }, {
            $push: {
              Saneamento:
              {
                ano: ANOS[S_Rs.indexOf(s_rDoAno)],
                pergunta: pergunta,
                resposta: cidade.Saneamento[pergunta]
              }
            }
          })
        }
        //Atualiza residuos
        for (pergunta in cidade["Resíduos"]) {
          await Cidade.findOneAndUpdate(
            { municipio_extenso: index }, {
            $push: {
              'Residuos':
              {
                ano: ANOS[S_Rs.indexOf(s_rDoAno)],
                pergunta: pergunta,
                resposta: cidade['Resíduos'][pergunta]
              }
            }
          })
        }
      }
    }

    console.log('Saneamento e residuos atualizados');
  } catch (err) {
    console.log('Erro ao atulizar Saneamento e residuos:', err)
  }
}

module.exports = atualizaSaneamentoResiduos