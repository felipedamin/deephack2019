const express = require('express');
const getData = require('../getData/index');
const Cidade = require('../database/models/cidade')

const router = express.Router();

// rota para buscar nomes dos municipios
router.get('/municipios', async (req, res) => {
  console.log("GET request on '/municipios'")
  try {
    const cidades = await Cidade.find();

    if (cidades == '') {
      await getData.getMunicipios();
      await getData.atualizaMunicipios();
      await getData.atualizaIegm();

      return res.status(200).send('atualizado')
    }

    var resultado = [];
    for (i in cidades) {
      resultado = await resultado.concat([cidades[i]['municipio_extenso']])
    }
    return res.status(200).send(JSON.stringify(resultado));
  } catch (err) {
    return res.status(400).send(`rota /municipios: ${err}`)
  }
});

// Busca todos os dados de determinado municipio
router.get('/municipio/:municipio', async (req, res) => {
  try {
    const cidade = await Cidade.find({ municipio_extenso: req.params.municipio });
    if (cidade == '') {
      return res.status(400).send('Essa cidade nao consta aqui, tente atualizar o BD ou verificar se digitou corretamente')
    }
    let iegm = cidade[0]['iegm']
    let saneamento = cidade[0]['Saneamento']
    let residuos = cidade[0]['Residuos']
    console.log(saneamento)
    let resultado = await JSON.stringify({ iegm, saneamento, residuos })
    console.log(resultado)

    return res.status(200).send(resultado);
  } catch (err) {
    return res.status(400).send('rota: /municipios/:municipio', err)
  }
});

module.exports = app => app.use('/database', router) // '/database' é o caminho para esse router