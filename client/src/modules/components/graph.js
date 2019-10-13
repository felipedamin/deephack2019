import React from "react";
// import Plot from "react-plotly.js";
import Plotly from "plotly.js-basic-dist";
// import Graphs from '../../../graphs'

import createPlotlyComponent from "react-plotly.js/factory";
const Plot = createPlotlyComponent(Plotly);



class Graph extends React.Component {
  render() {
    return (
      // <Plot data={Graphs.TurbinaA16.data} layout={Graphs.TurbinaA16.layout} width='100%' />
      <div>
        Grafico
      </div>
    );
  }
}

export default Graph