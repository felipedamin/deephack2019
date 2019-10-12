const express = require('express');
const getData = require('../getData/index');
const Cidade = require('../database/models/cidade')

const router = express.Router();

// rota para buscar nomes dos municipios
router.get('/municipios', async (req, res) => {
    try {
        // procura no banco de dados
        const cidade = await Cidade.findOne({ municipio: 'adamantina' });

        // Se nao achar, chama o getData,
        if (cidade == '') {
            await getData.getMunicipios();
            var municipios = require('../database/municipios.json')

            for (mun in municipios) {
                await Cidade.create({ municipio: mun.municipio, municipio_extenso: mun.municipio_extenso })
            }
            return res.status(200).send('atualizado')
            return res.status(200).send(`<p>${JSON.stringify(municipios)}</p>`)
        }
        // depois salva no BD e devolve (?)
        return res.send({ cidade });
    } catch (err) {
        return res.status(400).send(err)
    }
});


// rota para buscar IEGM do municipio
router.get('/iegm/:ano/:municipio', async (req, res) => {
    try {
        const cidade = await Cidade.findOne({ ...req.params.municipio });

        //findOne().populate('iegm')
        /*
        const iegm = await "iegm".concat(req.params.ano)
        // query database
        const db = await client.db('deephack2019');
        return res.send(test);
        const result = await db.find({ 'a': req.params.municipio });
        // return iegm
        */
        return res.send(cidade);
    } catch (err) {
        return res.status(400).send(err)
    }
});

// rota para buscar despesas do municipio

// rota para buscar saneamento do municipio

// rota para buscar residuos do municipio

module.exports = app => app.use('/database', router) // '/database' é o caminho para esse router