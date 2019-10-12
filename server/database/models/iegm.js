const mongoose = require('../../database');

const iegmSchema = new mongoose.Schema({
    texto_pergunta: String,
    reposta: String,
});

const iegm = mongoose.model('iegm', iegmSchema);

module.exports = iegm;