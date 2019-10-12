const mongoose = require('../../database');

const CidadeSchema = new mongoose.Schema({
    nome: {
        municipio: String,
        municipio_extenso: String,
    },
    iegm: [{
        type: mongoose.Schema.Types.ObjectId,
        ref: 'iegm',
    }],
});

const Cidade = mongoose.model('Cidade', CidadeSchema);

module.exports = Cidade;