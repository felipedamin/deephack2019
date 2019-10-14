const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors')

app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded());
// app.use(cors());
app.use(function (req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

require('./API/routes')(app)

const port = 3000
app.listen(port, () => {
    console.log(`server listening on port ${port}`);
});