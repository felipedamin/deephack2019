const mongoose = require('mongoose');

const dbName = 'deephack2019'

mongoose.connect(`mongodb://localhost/${dbName}`, {useNewUrlParser: true, useUnifiedTopology: true})
.then( () => {
    console.log(`Mongoose conectado ao DB: ${dbName}`)
}).catch( (err) => {
    console.log('Erro ao conectar o mongoose: ', err)
});

mongoose.Promise = global.Promise;

module.exports = mongoose