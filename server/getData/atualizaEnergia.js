const Cidade = require('../database/models/cidade');

const energiaCO2 = require('../database/energia_co2.json');

// Os municipios ja devem estar no BD com seus respectivos codigos
// Se nao estiverem, chamar a atualizaMunicipios
// basta GET em {link}/database/municipios

async function atualizaSaneamentoResiduos() {
  try {
    for (cidade in energiaCO2) {
        console.log(cidade)
      for (ano in energiaCO2[cidade]) {
          
        for (pergunta in energiaCO2[cidade][ano]) {
          /*await Cidade.findOneAndUpdate(
            { municipio_extenso: index }, {
            $push: {
              Saneamento:
              {
                ano: ANOS[S_Rs.indexOf(s_rDoAno)],
                pergunta: pergunta,
                resposta: cidade.Saneamento[pergunta]
              }
            }
          })*/
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