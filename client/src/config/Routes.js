import * as React from 'react';
import {
  BrowserRouter as Router,
  Route,
  Switch,
  Redirect
} from 'react-router-dom';
import Grid from '@material-ui/core/Grid';
import Home from '../modules/views/Home';
import Estado from '../modules/views/Estado';
import LayoutHeader from '../modules/header'
import LayoutFooter from '../modules/footer'


export class Routes extends React.Component {
  render() {
    return (
      <Router>
        <LayoutHeader />

        <Grid
          direction="column"
          justify="space-between"
          alignItems="center"
          style={{ minHeight: '100vh', overflow: 'hidden' }}
        >
          <Switch>
            <Route path="/home" component={Home} />
            <Route path="/estado" component={Estado} />
            <Redirect from="/" to="/home" />
          </Switch>
        </Grid>
        <LayoutFooter />
      </Router>
    )
  }
}
// <Route path="/users" component={UsersRoutes} />


export default Routes