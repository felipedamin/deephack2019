const atualizaMunicipios = require('./atualizaMunicipios')
const atualizaIegm = require('./atualizaIegm')
const atualizaSaneamentoResiduos = require('./atualizaSaneamentoResiduos')

async function main() {
    await atualizaMunicipios()
    await atualizaIegm()
    await atualizaSaneamentoResiduos()
    console.log("Fim")
}

main()