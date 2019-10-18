import React from "react";
import { Grid } from "@material-ui/core"

class Graph extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      cidade: this.props.cidade || '',
      meta: this.props.meta || '',
      grafico: false,
      width: this.props.cidade ? '45%' : '48%',
      height: this.props.cidade ? '60%' : '100%'
      //quais graficos preciso aqui
    }
    this.getGraficos()
  }

  async getGraficos() {
    try {
      if (this.state.cidade !== '') {
        this.graficoS1 = await require(`../../graphs/saneamento/${this.state.cidade}-fig1.png`)
        this.graficoS2 = await require(`../../graphs/saneamento/${this.state.cidade}-fig2.png`)
        this.graficoR1 = await require(`../../graphs/residuos/${this.state.cidade}fig1.png`)
        this.graficoR2 = await require(`../../graphs/residuos/${this.state.cidade}fig2.png`)
        this.graficoR3 = await require(`../../graphs/residuos/${this.state.cidade}fig3.png`)
        this.graficoR4 = await require(`../../graphs/residuos/${this.state.cidade}fig4.png`)
        this.graficoR5 = await require(`../../graphs/residuos/${this.state.cidade}fig5.png`)
        this.setState({ grafico: true })
      }
      else {
        this.grafico1 = await require(`../../graphs/IEGM/fig1.png`)
        this.grafico2 = await require(`../../graphs/IEGM/fig2.png`)
        this.grafico3 = await require(`../../graphs/IEGM/fig3.png`)
        this.grafico4 = await require(`../../graphs/IEGM/fig4.png`)
        this.setState({ grafico: true })
      }
    }
    catch (err) {
      console.log(err)
    }
  }

  render() {
    return (
      <div style={{ color: '#ffffff' }}>
        
        {this.state.grafico &&
          <Grid row>
            {(this.state.meta==='12.2') &&
              <img src={this.graficoS1} style={{ height: this.state.height, width: this.state.width, margin: '1%' }} />
            }
            {(this.state.meta==='12.2') &&
              <img src={this.graficoS2} style={{ height: this.state.height, width: this.state.width, margin: '1%' }} />
            }
            {(this.state.meta==='12.2') &&
              <img src={this.graficoR1} style={{ height: this.state.height, width: this.state.width, margin: '1%' }} />
            }
            {(this.state.meta==='12.2') &&
              <img src={this.graficoR2} style={{ height: this.state.height, width: this.state.width, margin: '1%' }} />
            }
            {(this.state.meta==='12.4') &&
              <img src={this.graficoR3} style={{ height: this.state.height, width: this.state.width, margin: '1%' }} />
            }
            {(this.state.meta==='12.5') &&
              <img src={this.graficoR4} style={{ height: this.state.height, width: this.state.width, margin: '1%' }} />
            }
            {(this.state.meta==='12.5') &&
              <img src={this.graficoR5} style={{ height: this.state.height, width: this.state.width, margin: '1%' }} />
            }
            {(this.state.meta==='') &&
              <img src={this.grafico1} style={{ height: this.state.height, width: this.state.width, margin: '1%' }} />
            }
            {(this.state.meta==='') &&
              <img src={this.grafico2} style={{ height: this.state.height, width: this.state.width, margin: '1%' }} />
            }
            {(this.state.meta==='') &&
              <img src={this.grafico3} style={{ height: this.state.height, width: this.state.width, margin: '1%' }} />
            }
            {(this.state.meta==='') &&
              <img src={this.grafico4} style={{ height: this.state.height, width: this.state.width, margin: '1%' }} />
            }
          </Grid>
        }
        <Grid row>
          <div>{this.state.meta}</div>
        </Grid>
      </div>
    );
  }
}

export default Graph