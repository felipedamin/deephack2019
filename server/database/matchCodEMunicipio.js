const iegm = require ('./iegm/2014iegm.json')
const fs = require('fs');

var resultado = '{'
for (i in iegm.cod_ibge) {
    const cidade = `"${iegm.cod_ibge[i].toString()}": "${iegm.Municipio[i]}",`
    resultado = resultado.concat(cidade)
}
resultado = resultado.substring(0, resultado.length - 1);
resultado = resultado.concat('}')

fs.writeFile("./codMunicipioIbge.json", resultado, function (err) {

    if (err) {
      return console.log(err);
    }

    console.log("The file was saved!");
});