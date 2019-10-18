import * as React from 'react';

import { BoxCidade } from '../components/boxCidade'

export default class GeralMunicipio extends React.Component {
  handleCheckbox = (event) => {
    const checked = event.target.checked;
    this.setState({ [event.target.value]: checked });
  }

  logState() {
    console.log(this.state)
  }

  render() {
    return (
      <div>
        <BoxCidade
          cidade={this.props.cidade}
        ></BoxCidade>
      </div>
    )
  }
}
