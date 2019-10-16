import * as React from 'react';
import { NavLink } from 'react-router-dom';
import styled from 'styled-components';

import Button from '@material-ui/core/Button';
import AppBar from '@material-ui/core/AppBar';
import Grid from '@material-ui/core/Grid';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';


class LayoutHeader extends React.Component {
  constructor() {
    super()
    this.state = {
      open: false,
    }
  }

  parquesList = () => (
    <div
      style={{ width: "250px", backgroundColor: '#ff7b17' }}
      role="presentation"
      onClick={this.toggleDrawer(true)}
      onKeyDown={this.toggleDrawer(true)}
    >
      <List onClick={this.toggleDrawer(false)}>
        {['Parque A', 'Parque B', 'Parque C', 'Parque D'].map((text, index) => (
          <ListItem button key={text}>
            <ListItemText primary={text} />
          </ListItem>
        ))}
      </List>
    </div>
  );

  toggleDrawer = (open) => event => {
    if (event && event.type === 'keydown' && (event.key === 'Tab' || event.key === 'Shift')) {
      return;
    }

    this.setState({ open: open });
  };

  render() {
    return (
      //#b21635
      <AppBar position="static" style={{ backgroundColor: '#fdfdfd', color: '#000000' }} >
        <Header className="container">
          <Grid container direction="row" justify="center" alignItems="center">
            <img src='https://transparencia.tce.sp.gov.br/themes/custom/tcesp/images/logo_tcesp.png' alt='Logo do TCESP'/>
          </Grid>
          <Grid container direction="row" justify="space-around" alignItems="center">
            <div style={{ width: '0em' }} />
            <div>|</div>
            <NavLink to="/estado" >
              <Button size="small">
                Estado de SP </Button>
            </NavLink>
            <div>|</div>
            <NavLink to="/home" >
              <Button size="small">
                Municípios </Button>
            </NavLink>
            <div>|</div>
            <div style={{ width: '0em' }} />
          </Grid>
        </Header>
      </AppBar>
    );
  }
}

/*
<Button onClick={this.toggleDrawer(true)} size="small" style={{ color: '#ffffff', marginLeft: '3em' }}>
  dropEsquerda
</Button>
*/

const Header = styled.header`
  display: block;
  padding-top: 20px;
  padding-bottom: 20px;
  background-color:rgba(0, 0, 0, 0);
`;

export default LayoutHeader