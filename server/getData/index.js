const getDespesas = require('./getDespesas');
const getIegm = require('./getIegm');
const getMunicipios = require('./getMunicipios');
const atualizaMunicipios = require('./atualizaMunicipios')
const atualizaIegm = require('./atualizaIegm')

// getDespesas('balsamo', 2015, 1)
module.exports = { getDespesas, getIegm, getMunicipios, atualizaMunicipios, atualizaIegm }