const mongoose = require('../../database');

const iegmSchema = new mongoose.Schema({
    texto_pergunta: {type: String},
    reposta: {type: String},
});

const iegm = mongoose.model('iegm', iegmSchema);

module.exports = iegm;