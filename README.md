# Nº PASSAGEIROS TRANSPORTADOS POR EMPRESAS FERROVIÁRIAS :steam_locomotive: 
## Recolha de dados
A base de dados utilizada pertence ao Instituto Nacional de Estatística (INE, https://www.ine.pt/xportal/xmain?xpgid=ine_main&xpid=INE), cuja missão é produzir a informação estatística oficial de qualidade, promovendo a coordenação, a análise, a inovação e a divulgação da atividade estatística nacional e europeia, garantindo o armazenamento integrado de dados. O INE segue uma linha com o Código de Conduta, com os seguintes valores: Profissionalismo, ética e respeito pela confidencialidade; Independência técnica, objetividade e imparcialidade; Valorização dos recursos humanos e desenvolvimento de novas competências; Compromisso para com a Qualidade; Criatividade, inovação e melhoria contínua dos processos; Respeito pelos detentores de fontes de dados; Sucesso nas parcerias com entidades externas; Satisfação das necessidades estatísticas diferenciadas.

## 🤔 Contexto 🤔 
Relativamente ao tema, como já foi dito, este baseia-se no número de passageiros transportados pelas empresas exploradoras da ferroviária. O tema vai de encontro a algo bastante importante e que deveria ter mais audiência, o uso de transportes públicos. Assim, a poluição diminuiria e os gastos nos equipamentos também. Nas grandes cidades existem bastantes transportes publicos, a população usufrui facilmente, por vezes, é preferível do que andar no transito da estrada. Contrapondo, em aldeias e vilas, este facilitismo e acessibilidade é menor. Existem poucos transportes públicos, sejam autocarros ou comboios, os horários são escassos e muitas das vezes a deslocação é longa. Eticamente, estaríamos a respeitar a natureza e consequentemente a nós próprios.ds

## 🧱 Estrutura 🧱
Análise de mercado de cryptomoedas em relação a MarketShare:(https://github.com/cdm2021/Crypto_2020_2semestre/blob/main/An%C3%A1lise%20de%20mercado%20de%20cryptomoedas%20no%20geral.ipynb).

Preço, Volume e ROI Anual, de 30, 60 e 90 dias do par BTC-USD:(https://github.com/cdm2021/Crypto_2020_2semestre/blob/main/Pre%C3%A7o,%20Volume%20e%20ROI%20Anual,%20de%2030,%2060%20e%2090%20dias%20do%20par%20BTC-USD.ipynb).

Preço, Volume e ROI Anual, de 30, 60 e 90 dias do par ETH-USD:(https://github.com/cdm2021/Crypto_2020_2semestre/blob/main/Pre%C3%A7o,%20Volume%20e%20ROI%20Anual,%20de%2030,%2060%20e%2090%20dias%20do%20par%20ETH-USD.ipynb).

## 🚀 Funções das aplicações 🚀
Aviso Legal: Este trabalho nao tem como intuito de dar aconcelhamento financeiro, tem apenas o intuito de verificar dados de ação de preço ao longo dos anos.

Análise de mercado de cryptomoedas em relação a MarketShare - Representação gráfica e atualizada de partilha de mercado entre as 100 maiores Criptomoedas em 2020. O uso de "others" serve para simplificar o gráfico e obter uma melhor visualização sobre as moedas que com maior valor total de mercado.

Preço, Volume e ROI Anual, de 30, 60 e 90 dias do par BTC-USD - Preço e Volume de negócio da Bitcoin histórico desde 01/01/2014 até 01/03/2021. Foi necessário fazer request dos dados até ao mês de março para poder fazer o cálculo de ROI de 60 e 90 dias. O ROI foi calculado a partir do dia 1 de cada mês e acabando 30/60/90 dias depois. O cálculo e representação visual do ROI feito no nosso trabalho é uma ferramenta que pode ajudar em futuros investimentos, tendo em conta a ação de preço nos anos anteriores. 

Preço, Volume e ROI Anual, de 30, 60 e 90 dias do par ETH-USD - Preço e Volume de negócio da Ethereum histórico desde 01/01/2016 até 01/03/2021. Tal como no caso do Bitcoin, foi necessário fazer request dos dados até ao mês de março para poder fazer o cálculo de ROI de 60 e 90 dias. O ROI foi calculado a partir do dia 1 de cada mês e acabando 30/60/90 dias depois. O cálculo e representação visual do ROI feito no nosso trabalho é uma ferramenta que pode ajudar em futuros investimentos, tendo em conta a ação de preço nos anos anteriores. 

## 📔 Dicionário dos dados 📔

bitcoin_price_marketcap_volume_20140101_20210302.csv

| Nome do ficheiro  |  Função e contéudo  |  Possiveis Valores  |
| ------------------- | ------------------- | ----------------- |
|  data |  Data | DD-MM-YYYY h-m-s-ms |
|  BTCUSD |  Valor da Bitcoin em dólares | >=0 |
|  ETHUSD |  Valor da Ethereum em dólares | >=0 |
|  marketcap |  Valor total de mercado de uma moeda | >=0 |
|  ROI |  Retorno sobre o investimento |  <0<  |
|  volume |  Total de moedas trocadas num determinado período de tempo |  >=0  |
|  preço_inicial |  Preço inicial de uma moeda num determinado momento |  >=0  |
|  prices |  Preço da moeda |  >=0  |
|  Percentagem |  Percentagem de determinado valor |  >=0  |
|  MarketShare | Percentagem de cada moeda no mercado |  >=0  |


bitcoin_roi_30_dias_mensal.csv

| Nome do ficheiro  |  Função e contéudo  |  Possiveis Valores  |
| ------------------- | ------------------- | ----------------- |
|  Ano |  Ano  |  YYYY  |
|  Meses |  Meses do Ano  | Mes |
|  ROI 30 Dias 2014 | ROI tendo em conta a data de investimento inicial o dia 1 de cada mês e a venda do mesmo 30 dias depois no ano 2014  |0 <= x <= 100, com valor percentual   |
|  ROI 30 Dias 2015 |  ROI tendo em conta a data de investimento inicial o dia 1 de cada mês e a venda do mesmo 30 dias depois no ano 2015  |  0 <= x <= 100, com valor percentual  |
|  ROI 30 Dias 2016 |  ROI tendo em conta a data de investimento inicial o dia 1 de cada mês e a venda do mesmo 30 dias depois no ano 2016  | 0 <= x <= 100, com valor percentual  |
|  ROI 30 Dias 2017 |  ROI tendo em conta a data de investimento inicial o dia 1 de cada mês e a venda do mesmo 30 dias depois no ano 2017  |  0 <= x <= 100, com valor percentual  |
|  ROI 30 Dias 2018 |  ROI tendo em conta a data de investimento inicial o dia 1 de cada mês e a venda do mesmo 30 dias depois no ano 2018  |  0 <= x <= 100, com valor percentual  |
|  ROI 30 Dias 2019 |  ROI tendo em conta a data de investimento inicial o dia 1 de cada mês e a venda do mesmo 30 dias depois no ano 2019  |  0 <= x <= 100, com valor percentual  |
|  ROI 30 Dias 2020 | ROI tendo em conta a data de investimento inicial o dia 1 de cada mês e a venda do mesmo 30 dias depois no ano 2020  |  0 <= x <= 100, com valor percentual  |
|  ROI 30 Dias Médio |  Roi médio  |  0 <= x <= 100, com valor percentual  |

bitcoin_roi_60_dias_mensal.csv

| Nome do ficheiro  |  Função e contéudo  |  Possiveis Valores  |
| ------------------- | ------------------- | ----------------- |
|  Meses |  Meses do Ano  | Mes |
|  ROI 60 Dias 2014 | ROI tendo em conta a data de investimento inicial o dia 1 de cada mês e a venda do mesmo 30 dias depois no ano 2014  |  0 <= x <= 100, com valor percentual |
|  ROI 60 Dias 2015 |  ROI tendo em conta a data de investimento inicial o dia 1 de cada mês e a venda do mesmo 30 dias depois no ano 2015  |  0 <= x <= 100, com valor percentual  |
|  ROI 60 Dias 2016 |  ROI tendo em conta a data de investimento inicial o dia 1 de cada mês e a venda do mesmo 30 dias depois no ano 2016  |  0 <= x <= 100, com valor percentual |
|  ROI 60 Dias 2017 |  ROI tendo em conta a data de investimento inicial o dia 1 de cada mês e a venda do mesmo 30 dias depois no ano 2017  |  0 <= x <= 100, com valor percentual |
|  ROI 60 Dias 2018 |  ROI tendo em conta a data de investimento inicial o dia 1 de cada mês e a venda do mesmo 30 dias depois no ano 2018  |  0 <= x <= 100, com valor percentual  |
|  ROI 60 Dias 2019 |  ROI tendo em conta a data de investimento inicial o dia 1 de cada mês e a venda do mesmo 30 dias depois no ano 2019  |  0 <= x <= 100, com valor percentual |
|  ROI 60 Dias 2020 |  ROI tendo em conta a data de investimento inicial o dia 1 de cada mês e a venda do mesmo 30 dias depois no ano 2020  |  0 <= x <= 100, com valor percentual  |
|  ROI 60 Dias Médio |  Roi médio  |  0 <= x <= 100, com valor percentual  |


bitcoin_roi_90_dias_mensal.csv

| Nome do ficheiro  |  Função e contéudo  |  Possiveis Valores  |
| ------------------- | ------------------- | ----------------- |
|  Meses |  Meses do Ano  | Mes |
|  ROI 90 Dias 2014 |  ROI tendo em conta a data de investimento inicial o dia 1 de cada mês e a venda do mesmo 30 dias depois no ano 2014  |  0 <= x <= 100, com valor percentual |
|  ROI 90 Dias 2015 |  ROI tendo em conta a data de investimento inicial o dia 1 de cada mês e a venda do mesmo 30 dias depois no ano 2015  |  0 <= x <= 100, com valor percentual |
|  ROI 90 Dias 2016 | ROI tendo em conta a data de investimento inicial o dia 1 de cada mês e a venda do mesmo 30 dias depois no ano 2016  |  0 <= x <= 100, com valor percentual |
|  ROI 90 Dias 2017 |  ROI tendo em conta a data de investimento inicial o dia 1 de cada mês e a venda do mesmo 30 dias depois no ano 2017  |  0 <= x <= 100, com valor percentual  |
|  ROI 90 Dias 2018 |  ROI tendo em conta a data de investimento inicial o dia 1 de cada mês e a venda do mesmo 30 dias depois no ano 2018  |  0 <= x <= 100, com valor percentual  |
|  ROI 90 Dias 2019 | ROI tendo em conta a data de investimento inicial o dia 1 de cada mês e a venda do mesmo 30 dias depois no ano 2019  |  0 <= x <= 100, com valor percentual  |
|  ROI 90 Dias 2020 |  ROI tendo em conta a data de investimento inicial o dia 1 de cada mês e a venda do mesmo 30 dias depois no ano 2020  |  0 <= x <= 100, com valor percentual  |
|  ROI 90 Dias Médio |  Roi médio  |  0 <= x <= 100, com valor percentual  |



## 💡 Problemas, inconsistências e melhorias 💡 

