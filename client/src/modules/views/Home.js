import * as React from 'react';
import Divider from '@material-ui/core/Divider';
import { FormGroup, FormControlLabel, Checkbox, TextField } from '@material-ui/core';
import Select from 'react-select'
import makeAnimated from 'react-select/animated';

import GeralMunicipio from './GeralMunicipio'


export default function Home() {
  const [cidade, setCidade] = React.useState('');
  /*
  const handleSubmit = async (event) => {
    event.preventDefault();
    this.setState({ loading: true })
    // busca os nomes das cidades no BD
    // se a cidade existe:
    // setState({ dados: dadosBD})
    this.setState({ dados: 'a' })
  }

  const handleInputChange = (event) => {
    const name = event.target.name;
    const value = event.target.value;

    this.setState({ [name]: value, loading: 'no', dados: '' });
  }
  */

  /*
  <form onSubmit={handleSubmit.bind(this)} style={{
        width: '50%', marginLeft: '25%', marginTop: '10px', padding: '2px', backgroundColor: '#ffffff',
        borderRadius: '3px'
      }}>
        <TextField
          fullWidth
          disabled={false}
          name="cidade"
          label="Pesquisar pelo munícipio"
          onChange={handleInputChange}
          onSubmit={handleSubmit.bind(this)}
        />
      </form>
  */

  const handleSearchBar = async value => {
    console.log(value)
    setCidade(value)
  };

  return (
    <div>
      <div style={{
        width: '50%', marginLeft: '25%', marginTop: '10px', padding: '2px', backgroundColor: '#ffffff',
        borderRadius: '3px'
      }}>
        <Select
          closeMenuOnSelect={true}
          components={makeAnimated()}
          options={[{ value: 'adamantina', label: 'Adamantina' },
          { value: 'portoFeliz', label: 'Porto Feliz' },
          { value: 'campinas', label: 'Campinas' }]}
          onChange={handleSearchBar}
        />
      </div>
      <p>{cidade.label}</p>
      {cidade &&
        <div style={{ fontFamily: 'Raleway', fontSize: '1.3em' }}>
          <GeralMunicipio cidade={cidade.label} dados={cidade.label} />
        </div>
      }
    </div>
  )
}