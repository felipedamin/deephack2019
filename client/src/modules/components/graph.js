import React from "react";
import { Grid } from "@material-ui/core"


const anos = [2014, 2015, 2016, 2017, 2018]

const listaPerguntas122 = ["A prefeitura municipal estimula entre seus órgãos e entidades de sua responsabilidade projetos e/ou ações que promovam o uso racional de recursos naturais?",
  "A prefeitura possui ou participa de algum programa ou ação que promovam a melhoria contínua da qualidade ambiental no município?",
  "A prefeitura possui alguma estrutura organizacional para tratar de assuntos ligados ao Meio Ambiente Municipal?"
]

const listaPerguntas124 = ["A prefeitura possui Plano de Gestão de Resíduos da Construção Civil elaborado e implantado de acordo com a resolução CONAMA 307/2002 e suas alterações?",
"O município já parou de lançar, a céu aberto (lixões), seus resíduos sólidos?",
"Não há mais catadores de materiais recicláveis no aterro municipal.",
"Existe licença de operação da CETESB para a área de aterro?",
"Antes de aterrar o lixo, o município realiza algum tipo de processamento de resíduos?"
]

const listaPerguntas125 = ["O plano municipal de Gestão Municipal de Resíduos Sólidos já está em vigor?",
"A prefeitura municipal realiza a coleta seletiva de resíduos sólidos?",
"A prefeitura possui Plano de Gestão de Resíduos da Construção Civil elaborado e implantado de acordo com a resolução CONAMA 307/2002 e suas alterações?",
"Não há mais catadores de materiais recicláveis no aterro municipal.",
"Antes de aterrar o lixo, o município realiza algum tipo de processamento de resíduos?"
]

const listaPerguntas127 = ["A prefeitura municipal estimula entre seus órgãos e entidades de sua responsabilidade projetos e/ou ações que promovam o uso racional de recursos naturais?"]
const listaPerguntas128 = ["A prefeitura adota na rede escolar municipal algum programa ou ação de educação ambiental?"]


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
    this.iegm = this.props.iegm
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
        this.grafico5 = await require(`../../graphs/estado/coleta_rdo_sp.png`)
        this.grafico6 = await require(`../../graphs/estado/consumo_medio_sp.png`)
        this.grafico7 = await require(`../../graphs/estado/donut_2015.png`)
        this.grafico8 = await require(`../../graphs/estado/donut_2016.png`)
        this.grafico9 = await require(`../../graphs/estado/donut_2017.png`)
        this.grafico10 = await require(`../../graphs/estado/massa_coletada_sp.png`)
        this.grafico11 = await require(`../../graphs/estado/massa_via_seletiva_sp.png`)
        this.grafico12 = await require(`../../graphs/estado/pop_beneficiada_sp.png`)
        this.grafico13 = await require(`../../graphs/estado/recup_reciclaveis_sp.png`)
        this.grafico14 = await require(`../../graphs/estado/taxa_pop_atendida_sp.png`)
        this.setState({ grafico: true })
      }
      console.log(this.iegm)
    }
    catch (err) {
      console.log(err)
    }
  }

  render() {
    return (
      <div style={{ color: '#ffffff' }}>

        {this.state.grafico &&
          <div>
            <Grid row>
              {(this.state.meta === '12.2') &&
                <img src={this.graficoS1} style={{ height: this.state.height, width: this.state.width, margin: '1%' }}
                  alt={'Se esta mensagem está aparecendo, ou a cidade não possui os dados para esse gráfico, ou tente recarregar a página'} />
              }
              {(this.state.meta === '12.2') &&
                <img src={this.graficoS2} style={{ height: this.state.height, width: this.state.width, margin: '1%' }}
                  alt={'Se esta mensagem está aparecendo, ou a cidade não possui os dados para esse gráfico, ou tente recarregar a página'} />
              }
              {(this.state.meta === '12.2') &&
                <img src={this.graficoR1} style={{ height: this.state.height, width: this.state.width, margin: '1%' }}
                  alt={'Se esta mensagem está aparecendo, ou a cidade não possui os dados para esse gráfico, ou tente recarregar a página'} />
              }
              {(this.state.meta === '12.2') &&
                <img src={this.graficoR2} style={{ height: this.state.height, width: this.state.width, margin: '1%' }}
                  alt={'Se esta mensagem está aparecendo, ou a cidade não possui os dados para esse gráfico, ou tente recarregar a página'} />
              }

              {(this.state.meta === '12.4') &&
                <img src={this.graficoR3} style={{ height: this.state.height, width: this.state.width, margin: '1%' }}
                  alt={'Se esta mensagem está aparecendo, ou a cidade não possui os dados para esse gráfico, ou tente recarregar a página'} />
              }
              {(this.state.meta === '12.5') &&
                <img src={this.graficoR4} style={{ height: this.state.height, width: this.state.width, margin: '1%' }}
                  alt={'Se esta mensagem está aparecendo, ou a cidade não possui os dados para esse gráfico, ou tente recarregar a página'} />
              }
              {(this.state.meta === '12.5') &&
                <img src={this.graficoR5} style={{ height: this.state.height, width: this.state.width, margin: '1%' }}
                  alt={'Se esta mensagem está aparecendo, ou a cidade não possui os dados para esse gráfico, ou tente recarregar a página'} />
              }
              {(this.state.meta === '') &&
                <img src={this.grafico1} style={{ height: this.state.height, width: this.state.width, margin: '1%' }}
                  alt={'Se esta mensagem está aparecendo, ou o estado não possui os dados para esse gráfico, ou tente recarregar a página'} />
              }
              {(this.state.meta === '') &&
                <img src={this.grafico2} style={{ height: this.state.height, width: this.state.width, margin: '1%' }}
                  alt={'Se esta mensagem está aparecendo, ou o estado não possui os dados para esse gráfico, ou tente recarregar a página'} />
              }
              {(this.state.meta === '') &&
                <img src={this.grafico3} style={{ height: this.state.height, width: this.state.width, margin: '1%' }}
                  alt={'Se esta mensagem está aparecendo, ou o estado não possui os dados para esse gráfico, ou tente recarregar a página'} />
              }
              {(this.state.meta === '') &&
                <img src={this.grafico4} style={{ height: this.state.height, width: this.state.width, margin: '1%' }}
                  alt={'Se esta mensagem está aparecendo, ou o estado não possui os dados para esse gráfico, ou tente recarregar a página'} />
              }
              {(this.state.meta === '') &&
                <img src={this.grafico5} style={{ height: this.state.height, width: this.state.width, margin: '1%' }}
                  alt={'Se esta mensagem está aparecendo, ou o estado não possui os dados para esse gráfico, ou tente recarregar a página'} />
              }
              {(this.state.meta === '') &&
                <img src={this.grafico6} style={{ height: this.state.height, width: this.state.width, margin: '1%' }}
                  alt={'Se esta mensagem está aparecendo, ou o estado não possui os dados para esse gráfico, ou tente recarregar a página'} />
              }
              {(this.state.meta === '') &&
                <img src={this.grafico7} style={{ height: this.state.height, width: this.state.width, margin: '1%' }}
                  alt={'Se esta mensagem está aparecendo, ou o estado não possui os dados para esse gráfico, ou tente recarregar a página'} />
              }
              {(this.state.meta === '') &&
                <img src={this.grafico8} style={{ height: this.state.height, width: this.state.width, margin: '1%' }}
                  alt={'Se esta mensagem está aparecendo, ou o estado não possui os dados para esse gráfico, ou tente recarregar a página'} />
              }
              {(this.state.meta === '') &&
                <img src={this.grafico9} style={{ height: this.state.height, width: this.state.width, margin: '1%' }}
                  alt={'Se esta mensagem está aparecendo, ou o estado não possui os dados para esse gráfico, ou tente recarregar a página'} />
              }
              {(this.state.meta === '') &&
                <img src={this.grafico10} style={{ height: this.state.height, width: this.state.width, margin: '1%' }}
                  alt={'Se esta mensagem está aparecendo, ou o estado não possui os dados para esse gráfico, ou tente recarregar a página'} />
              }
              {(this.state.meta === '') &&
                <img src={this.grafico11} style={{ height: this.state.height, width: this.state.width, margin: '1%' }}
                  alt={'Se esta mensagem está aparecendo, ou o estado não possui os dados para esse gráfico, ou tente recarregar a página'} />
              }
              {(this.state.meta === '') &&
                <img src={this.grafico12} style={{ height: this.state.height, width: this.state.width, margin: '1%' }}
                  alt={'Se esta mensagem está aparecendo, ou o estado não possui os dados para esse gráfico, ou tente recarregar a página'} />
              }
              {(this.state.meta === '') &&
                <img src={this.grafico13} style={{ height: this.state.height, width: this.state.width, margin: '1%' }}
                  alt={'Se esta mensagem está aparecendo, ou o estado não possui os dados para esse gráfico, ou tente recarregar a página'} />
              }
              {(this.state.meta === '') &&
                <img src={this.grafico14} style={{ height: this.state.height, width: this.state.width, margin: '1%' }}
                  alt={'Se esta mensagem está aparecendo, ou o estado não possui os dados para esse gráfico, ou tente recarregar a página'} />
              }

            </Grid>

            {
              (this.state.meta === '12.2') &&
              <Grid container direction="row" justify="center" alignItems="center">
                {
                  listaPerguntas122.map((pergunta, key) => {
                    return (
                      <div justify='space-evenly'>
                        {pergunta}
                        {
                          this.iegm[pergunta]
                          && anos.map((ano, key) => {
                            return (
                              <div>
                                {
                                  this.iegm[pergunta][ano]
                                  &&
                                  <p>{ano}: {this.iegm[pergunta][ano] == 1 ? 'sim' : 'não'}</p>
                                }
                              </div>
                            )
                          })
                        }
                      </div>
                    )
                  })
                }
              </Grid>
            }

            {(this.state.meta === '12.4') &&
              <Grid container direction="row" justify="center" alignItems="center">
              {
                listaPerguntas124.map((pergunta, key) => {
                  return (
                    <div justify='space-evenly'>
                      {pergunta}
                      {
                        this.iegm[pergunta]
                        && anos.map((ano, key) => {
                          return (
                            <div>
                              {
                                this.iegm[pergunta][ano]
                                &&
                                <p>{ano}: {this.iegm[pergunta][ano] == 1 ? 'sim' : 'não'}</p>
                              }
                            </div>
                          )
                        })
                      }
                    </div>
                  )
                })
              }
            </Grid>}
            {(this.state.meta === '12.5') &&
              <Grid container direction="row" justify="center" alignItems="center">
              {
                listaPerguntas125.map((pergunta, key) => {
                  return (
                    <div justify='space-evenly'>
                      {pergunta}
                      {
                        this.iegm[pergunta]
                        && anos.map((ano, key) => {
                          return (
                            <div>
                              {
                                this.iegm[pergunta][ano]
                                &&
                                <p>{ano}: {this.iegm[pergunta][ano] == 1 ? 'sim' : 'não'}</p>
                              }
                            </div>
                          )
                        })
                      }
                    </div>
                  )
                })
              }
            </Grid>}
            {(this.state.meta === '12.7') &&
              <Grid container direction="row" justify="center" alignItems="center">
              {
                listaPerguntas127.map((pergunta, key) => {
                  return (
                    <div justify='space-evenly'>
                      {pergunta}
                      {
                        this.iegm[pergunta]
                        && anos.map((ano, key) => {
                          return (
                            <div>
                              {
                                this.iegm[pergunta][ano]
                                &&
                                <p>{ano}: {this.iegm[pergunta][ano] == 1 ? 'sim' : 'não'}</p>
                              }
                            </div>
                          )
                        })
                      }
                    </div>
                  )
                })
              }
            </Grid>}
            {(this.state.meta === '12.8') &&
             <Grid container direction="row" justify="center" alignItems="center">
             {
               listaPerguntas128.map((pergunta, key) => {
                 return (
                   <div justify='space-evenly'>
                     {pergunta}
                     {
                       this.iegm[pergunta]
                       && anos.map((ano, key) => {
                         return (
                           <div>
                             {
                               this.iegm[pergunta][ano]
                               &&
                               <p>{ano}: {this.iegm[pergunta][ano] == 1 ? 'sim' : 'não'}</p>
                             }
                           </div>
                         )
                       })
                     }
                   </div>
                 )
               })
             }
           </Grid>}
          </div>
        }
      </div>
    );
  }
}

export default Graph