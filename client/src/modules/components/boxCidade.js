import * as React from 'react';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import ExpansionPanel from '@material-ui/core/ExpansionPanel';
import ExpansionPanelSummary from '@material-ui/core/ExpansionPanelSummary';
import ExpansionPanelDetails from '@material-ui/core/ExpansionPanelDetails'
import Grid from '@material-ui/core/Grid';

//eslint-disable-next-line
import { NavLink } from 'react-router-dom';

import Graph from './graph'
import { ODS12 } from '../../config/ods'
//eslint-disable-next-line
import { Button } from '@material-ui/core';

export class BoxCidade extends React.Component {

  render() {
    return (
      //#e3e3e3
      <Card style={{ margin: 20, backgroundColor: '#b21635', fontFamily: 'Raleway'}}>
        <CardContent style={{ fontFamily: 'Raleway', fontSize: '1em' }}>
          <p style={{ color: '#ffffff', fontSize: '1.3em', margin: '0.2em' }}>
            {`${this.props.cidade}`}
          </p>
        </CardContent>
        <CardActions>
          <Grid column style={{ width: '100%' }}>
            {
              ODS12.map((item, key) => {
                return (
                  <ExpansionPanel style={{ backgroundColor: 'rgba(0, 0, 0, 0.0)', alignItems: "center", border: '1px solid rgba(0, 0, 0, .125)', width: '98%', marginLeft: '1%' }}>
                    <ExpansionPanelSummary margin='0.2em' >
                      <p style={{ color: '#ffffff', margin: '0.2em' }}>Meta {item.number}</p>
                    </ExpansionPanelSummary>
                    <ExpansionPanelDetails style={{ backgroundColor: 'rgba(0, 0, 0, .1)', align: 'center' }}>
                      <Grid column style={{ width: '100%' }}>
                        <h6>{item.texto}</h6>
                        <Graph width='100%'></Graph>
                      </Grid>
                    </ExpansionPanelDetails>
                  </ExpansionPanel>
                )
              })
            }

          </Grid>
        </CardActions>
      </Card>
    )
  }
}