const express = require('express');

const router = express.Router();

router.get('/caminhoDaRequisiçao', async (req, res) => {
    // procura no banco de dados
    // Se achar, devolve

    // Se nao achar, chama o getData, depois salva no BD e devolve (?)
});

module.exports = app => app.use('/database', router) // '/database' é o caminho para esse router