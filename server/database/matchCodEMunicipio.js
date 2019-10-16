const iegm = require ('./iegm2014.json')

var resultado = ''
for (i in iegm.cod_ibge) {
    const cidade = `"${iegm.cod_ibge[i].toString()}": "${iegm.Municipio[i]}",`
    resultado = resultado.concat(cidade)
}

console.log(resultado)