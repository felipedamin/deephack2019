async function getMunicipios() {
    try {
        const municipios = await fetch('http://localhost:3000/database/municipios');
        return await Promise.resolve(municipios.json())
    } catch (error) {
        console.error('error, ', error);
        return Promise.reject(error)
    }
}

async function getDadosMunicipio(municipio) {
    try {
        let dados = await fetch(`http://localhost:3000/database/municipio/${municipio}`);
        // console.log('get', link, 'FromBD:', await Promise.resolve(await dados.json()))
        //dados = await Promise.resolve(await dados.json())
        // console.log('dados', await Promise.resolve(dados.json()))
        dados = await Promise.resolve(dados.json())

        const iegm = await dados['iegm']
        const saneamento = await dados['saneamento']
        const residuos = await dados['residuos']

        return await Promise.resolve({iegm, saneamento, residuos })
    } catch (error) {
        console.error('error, ', error);
    }
}

module.exports = { getMunicipios, getDadosMunicipio }