const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost/deephack2019', {useNewUrlParser: true});
mongoose.Promise = global.Promise;

module.exports = mongoose