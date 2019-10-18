const https = require('https');
const fs = require('fs');

module.exports = function getDespesas(municipio, ano, mes) {
  const options = {
    host: 'transparencia.tce.sp.gov.br',
    path: `/api/json/despesas/${municipio}/${ano}/${mes}`
  };

  var req = https.get(options, function (res) {
    console.log('STATUS: ' + res.statusCode);
    console.log('HEADERS: ' + JSON.stringify(res.headers));

    // Buffer the body entirely for processing as a whole.
    var bodyChunks = [];
    res.on('data', function (chunk) {
      // You can process streamed parts here...
      bodyChunks.push(chunk);
    }).on('end', function () {
      var body = Buffer.concat(bodyChunks);
      fs.writeFile(`../database/despesas/${municipio}_${ano}_${mes}.json`, body, function (err) {

        if (err) {
          return console.log(err);
        }

        console.log("The file was saved!");
      });

    })
  });

  req.on('error', function (e) {
    console.log('ERROR: ' + e.message);
  });
}

// getDespesas('balsamo', 2015, 1)