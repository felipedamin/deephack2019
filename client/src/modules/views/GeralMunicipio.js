import * as React from 'react';

/*
import Card from '@material-ui/core/Card';
import FormControl from '@material-ui/core/FormControl';
import FormGroup from '@material-ui/core/FormGroup';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Divider from '@material-ui/core/Divider';
import Switch from '@material-ui/core/Switch';
*/
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

/*
var canvas = document.getElementById('background')
var ctx = canvas.getContext('2d');
var gradient = ctx.createRadialGradient( );
gradient.addColorStop(0, (30, 39, 73));
gradient.addColorStop(1, (16, 18, 37));
*/