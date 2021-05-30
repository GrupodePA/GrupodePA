# Nº PASSAGEIROS TRANSPORTADOS POR EMPRESAS FERROVIÁRIAS :steam_locomotive: 
## Recolha de dados
A base de dados utilizada pertence ao Instituto Nacional de Estatística (INE, https://www.ine.pt/xportal/xmain?xpgid=ine_main&xpid=INE), cuja missão é produzir a informação estatística oficial de qualidade, promovendo a coordenação, a análise, a inovação e a divulgação da atividade estatística nacional e europeia, garantindo o armazenamento integrado de dados. O INE segue uma linha com o Código de Conduta, com os seguintes valores: Profissionalismo, ética e respeito pela confidencialidade; Independência técnica, objetividade e imparcialidade; Valorização dos recursos humanos e desenvolvimento de novas competências; Compromisso para com a Qualidade; Criatividade, inovação e melhoria contínua dos processos; Respeito pelos detentores de fontes de dados; Sucesso nas parcerias com entidades externas; Satisfação das necessidades estatísticas diferenciadas.

## Contexto
Relativamente aos temas em análise, estes são: número de passageiros transportados pelas empresas exploradoras da ferroviária e número de viagens feitas por turistas com variáveis sexo e meio de transporte.
O primeiro tema vai de encontro a algo bastante importante e que deveria ter mais audiência, o uso de transportes públicos. Assim, a poluição diminuiria e os gastos nos equipamentos também. Nas grandes cidades existem bastantes transportes publicos, a população usufrui facilmente. Por vezes, é preferível do que andar no transito da estrada. Contrapondo, em aldeias e vilas, este facilitismo e acessibilidade é menor. Existem poucos transportes públicos, sejam autocarros ou comboios, os horários são escassos e muitas das vezes a deslocação é longa. Eticamente, estaríamos a respeitar a natureza e consequentemente a nós próprios.
Já no que que diz respeito ao segundo tema, pretendemos analisar em que épocas do ano existe um aumento no número de viagens efetuadas por turistas, em automóveis ferroviários. Isto visto que, em primeiro lugar, é super importante os turistas viagarem no nosso país. Em segundo, é interessante perceber se existem muitas viagens efetuadas em transportes ferrovoários.

## Estrutura
Passageiros-quilómetro transportados (N.º) pelas empresas exploradoras de sistema ferroviário pesado por Tipo de tráfego ; Mensal
(https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_indicadores&indOcorrCod=0000902&contexto=bd&selTab=tab2) - ao abrir o link é necessário selecionar o periodo de análise (decidimos analisar os ultimos dez anos disponiveis), a localização geográficas (Portugal) e o tipo de tráfego (total, suburbano nacional e internacional).

Viagens (N.º) feitas pelos turistas por Sexo e Meio de transporte utilizado; Mensal
(https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_indicadores&indOcorrCod=0007236&contexto=bd&selTab=tab2) - ao abrir o link é necessário selecionar o periodo de análise (decidimos analisar os ultimos dez anos disponiveis), a residência (Portugal), o tipo de tráfego (total) e o sexo(HM).

## Funções da aplicação
Com acesso ao Instituto Nacional de Estatistícas, realizamos duas análises de dois temas, com o intuito de chegar rapidamente a conclusões fidedignas. Pode consultar a documentação em análise no seguite endereço:
https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_main

## Dicionário dos dados

https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_indicadores&indOcorrCod=0000902&contexto=bd&selTab=tab2

N_passageiros_transportados_por_empresasferroviárias_anual.csv

| Nome do ficheiro  |  Função e contéudo  |  Possiveis Valores  |
| ------------------- | ------------------- | ----------------- |
|  Mês |  Mês | Janeiro a Dezembro |
|  Ano |  Ano | YYYY |
|  Suburbano |  Quantidade de pessoas que utilizaram este tipo de tráfego | >=0 |
|  Nacional |  Quantidade de pessoas que utilizaram este tipo de tráfego | >=0 |
|  Internacional |  Quantidade de pessoas que utilizaram este tipo de tráfego | >=0 |
|  Numero Total de Passageiros |  Numero Total de Passageiros em Portugal |  >=0  |




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

