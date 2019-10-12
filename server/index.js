const express = require('express');
const bodyParser = require('body-parser');

app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded());

require('./API/routes')(app)

const port = 3000
app.listen(port, () => {
    console.log(`server listening on port ${port}`);
});