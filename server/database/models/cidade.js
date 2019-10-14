const mongoose = require('../../database');

const CidadeSchema = new mongoose.Schema({
  municipio: { type: String, require: true },
  municipio_extenso: { type: String, require: true },
  cod_ibge: { type: Number, require: true },
  iegm: [{
    ano: Number,  
    pergunta: { type: String, required: true },
    resposta: { type: String, required: true }
    /*perguntas: [{
      texto_pergunta: { type: String, require: true },
      reposta: { type: String, require: true }
    }],*/
  }],
  buff: Buffer
});

const Cidade = mongoose.model('Cidade', CidadeSchema);

module.exports = Cidade;