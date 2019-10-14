import * as React from 'react';
import SearchBox from '../components/searchBox'

import GeralMunicipio from './GeralMunicipio'

export default class Home extends React.Component {
  constructor() {
    super()
    this.state = {
      cidade: '',
      valido: false
    }
  }

  handleChange = (value, valido) => {
    this.setState({ cidade: value, valido: valido });
  }

  render() {
    return (
      <div>
        <div style={{
          width: '50%', marginLeft: '25%', marginTop: '10px', padding: '2px', backgroundColor: '#ffffff',
          borderRadius: '3px'
        }}>
          <div>Digite e selecione uma cidade:</div>
          <SearchBox
            onChange={this.handleChange.bind(this)}
            cidade={this.state.cidade}
          />
        </div>
        {this.state.valido &&
          <div style={{ fontFamily: 'Raleway', fontSize: '1.3em' }}>
            <GeralMunicipio cidade={this.state.cidade} />
          </div>
        }
      </div>
    )
  }
}