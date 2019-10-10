const https = require('https');
const fs = require('fs');

module.exports = function getIegm() {

  const options = {
    host: 'transparencia.tce.sp.gov.br',
    path: '/iegm-deephack2019'
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
      fs.writeFile("./iegmData", body, function (err) {

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
