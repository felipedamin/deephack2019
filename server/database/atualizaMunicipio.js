const client = require('./mongoConnect');
const getData = require('../getData/index');


class atualizaMunicipio {
    constructor(municipio, ano) {
        this.municipio = municipio;
        this.ano = ano;

        this.check = verificaMunicipio()
    };

    async verificaMunicipio() {
        const listaMunicipios = await getData.getMunicipios();
        this.check = listaMunicipios.includes(this.municipio);
    };
    
    async atualizaIegm() {
        this.iegm = getData.getIegm();
        
        // TODO tratar arquivo recebido e selecionar dados do municipio

        // TODO update Database
    }

    async atualizaDespesas() {
        // TODO:
        // Buscarei todos os meses? ou apenas um mes especifico?
        // Todos os meses implica em 12 requisiçoes (realizar paralelamente)
    }

    atualizaBD() {
        // TODO:
        // tratarDespesas.py

        // const db = client.db(deephack2019);
        // db.collection('????').insertOne({a:1}, function(err, r) {
    }
}
