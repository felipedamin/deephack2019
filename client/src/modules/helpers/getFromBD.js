async function getMunicipios() {
    try {
        const municipios = await fetch('http://localhost:3000/database/municipios');
        return await Promise.resolve(municipios.json())
    } catch (error) {
        console.error('error, ', error);
        return Promise.reject(error)
    }
}

async function getIegm(municipio) {
    try {
        const dados = await fetch(`http://localhost:3000/database/municipio/${municipio}`);
        return await Promise.resolve(await dados.json())
    } catch (error) {
        console.error('error, ', error);
    }
}

module.exports = { getMunicipios, getIegm }