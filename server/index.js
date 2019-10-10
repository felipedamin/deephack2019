const express = require('express');
const bodyParser = require('body-parser');

app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded());

require('./API/routes')(app)

app.listen(3000);