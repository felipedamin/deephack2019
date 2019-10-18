import * as React from 'react';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
// import Grid from '@material-ui/core/Grid';
import Graph from '../components/graph';

export default class Estado extends React.Component {
  render() {
    return (
      <div>
        <Card style={{ margin: 20, backgroundColor: '#b21635', fontFamily: 'Raleway' }}>
        <CardContent style={{ fontFamily: 'Raleway', fontSize: '1em' }}>
          <p style={{ color: '#ffffff', fontSize: '1.3em', margin: '0.2em' }}>
            Visão geral do Estado de São Paulo
          </p>
          <Graph />
        </CardContent>
      </Card>
      </div>
    )
  }
}
