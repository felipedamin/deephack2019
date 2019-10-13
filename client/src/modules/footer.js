/* eslint-disable jsx-a11y/alt-text */
import * as React from 'react';
import styled from 'styled-components';

import Grid from '@material-ui/core/Grid';

const LayoutFooter = () => (
  <Footer className="container" style={{ backgroundColor: '#494949', color: '#ffffff' }}>
    <Grid container direction="column" justify="space-between" alignItems="center">
      <div> Tribunal de Contas do Estado de São Paulo - Av: Rangel Pestana, 315 - Centro - CEP 01017-906 - São Paulo/SP - PABX: 3292-3266</div>
    </Grid>
  </Footer>
);

const Footer = styled.footer`
  display: block;
  padding-top: 20px;
  padding-bottom: 20px;
  background-color: #00FF00;
`;

export default LayoutFooter