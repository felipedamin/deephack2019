# deephack2019

# Instruções de Instalação (será necessário NodeJs, e Python3):
1 - Clone o repositório \
2 - Vá até a pasta raiz do projeto dentro execute *'npm install'*. Repita o processe dentro da pasta "client" \
3 - Use o pip para instalar o plotly e o orca, *"pip install plotly plotly-orca"*. (pandas e numpy tambem serão necessários) \
  3a - Para qualquer biblioteca que faltar ao executar algum dos arquivos python, basta rodar *"pip install {nome da biblioteca}"* \
4 - instale o mongoDB (essa instalação irá depender do seu sistema operacional, mais informaçoes podem ser encontradas no próprio site do mongo), esse será nosso banco de dados. \

# Instruções para iniciar pela primeira vez:
Esta etapa pode demorar \
1 - Execute o *mongodb*. Basta digitar mongod no terminal. \
2 - Agora precisaremos suprir o banco de dados, os arquivos json disponiveis no repositório serão suficientes para isso. Também é possível utilizar os códigos de busca em APIs que estão em server/API, pelo fato de nem todas as fontes que usamos terem APIs, aconselho a opção dos json's. \
  2a - na pasta server/getData, execute *"node atualizar.js"*. Aguarde terminar (será exibido "Fim" no terminal)\
3 - Precisamos gerar os graficos \
  3a - Pretendemos ter os gráficos já prontos no backend, assim ao solicitar as informações de uma cidade não é necessário que eles sejam feitos na hora, o que diminui o tempo de espera do usuário. \
  3b - Para gerar os gráficos execute os seguintes comandos na pasta raiz do projeto (ou seja, fora da pasta server): \
    3b.1 - *python3 server/generateGraph/generateAllGraphs.py* \
    3b.2 - *python3 server/generateGraph/numeros_estado.py* \
    obs: é necessário que as seguintes pastas existam dentro de client/src/graphs: "estado", "IEGM", "residuos", "saneamento" \

# Instruções para rodar o servidor e o client (site):
1 - Se já tiver instalado tudo, e já tiver realizado os procedimentos para alimentar o BD e gerar os gráficos, prossiga: \
2 - Assegure-se que o MongoDB está rodando (se não estiver, basta digitar *"mongod"* no terminal) \
3 - Executar o servidor: dentro da pasta "server" execute o comando *"node index.js"* \
4 - Executar o client: dentro da pasta "client" execute o comando *"npm start"* \
Após isso, o site será compilado e abrirá automaticamente. \

Aproveite o site :) \
Temos uma aba para a visão geral do estado e outra para busca de cidades. \
