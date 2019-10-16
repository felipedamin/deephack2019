const mongoose = require('../../database');

const CidadeSchema = new mongoose.Schema({
  municipio: { type: String, require: true },
  municipio_extenso: { type: String, require: true },
  cod_ibge: { type: String, require: true },
  iegm: [{
    ano: Number,
    pergunta: { type: String, required: true },
    resposta: { type: String, required: true }
  }],
  Residuos: [{
    ano: Number,
    pergunta: { type: String, required: true },
    resposta: { type: String, required: true }
  }],
  Saneamento: [{
    ano: Number,
    pergunta: { type: String, required: true },
    resposta: { type: String, required: true }
  }],
  buff: Buffer
});

const Cidade = mongoose.model('Cidade', CidadeSchema);

module.exports = Cidade;