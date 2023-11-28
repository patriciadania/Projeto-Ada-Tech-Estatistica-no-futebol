# Análise da Longevidade dos Técnicos no Campeonato Brasileiro de 2019

O objetivo era responder à pergunta: Em geral, times com técnicos mais longevos ficam em uma posição melhor na tabela, no fim do campeonato?<br>

1 - Para realizar essa análise, utilizamos um arquivo JSON contendo os dados do campeonato.<br>

2 - Utilizamos a biblioteca Pandas para ler o arquivo JSON e transformá-lo em um DataFrame. Em seguida, percorremos as rodadas e partidas do campeonato para calcular a pontuação de cada time. Armazenamos o número de rodadas em que cada técnico permaneceu no cargo para cada time. <br>

3 - Criamos um dicionário chamado soma_rodadas, onde a chave era o nome do time e o valor era outro dicionário contendo o nome do técnico e o número de rodadas em que ele ficou no cargo.<br>

## Colaboradores

        Giorggia Talynska Malheiros
        Helouise Dayane Dos Santos Silva
        Juliana Lima
        Leonardo Luiz
        Patricia Adania De Oliveira
        Rafael Assis Esteves Dos Santos
        Vanderlândio Zeferino Da Rocha
        
## Com base nesses dados, pudemos responder à pergunta proposta. A seguir, apresentamos os resultados obtidos:
- Classificação dos Times: Imprimimos a classificação final dos times, ordenados pela pontuação. Essa classificação nos permite visualizar quais times obtiveram melhor desempenho no campeonato.<br>

- Dicionário Ordenado de Técnico e Rodadas Jogadas: Apresentamos um dicionário ordenado dos técnicos e o número de rodadas jogadas por cada um. Isso nos permite identificar o técnico que permaneceu por mais tempo no cargo em cada time.

- Gráfico de Dispersão: Construímos um gráfico de dispersão que relaciona a posição do time na classificação com o tempo do técnico mais longevo. Cada ponto no gráfico representa um time, onde o eixo x representa a posição do time na classificação e o eixo y representa o número de rodadas em que o técnico mais longevo permaneceu no cargo. Esse gráfico nos ajuda a visualizar se existe uma tendência entre a longevidade do técnico e a posição final do time.

##  Após a análise dos resultados, podemos fazer algumas observações:

Não há uma relação direta entre a longevidade dos técnicos e a posição final dos times na tabela. Existem casos em que times com técnicos mais longevos obtiveram um bom desempenho e ficaram em posições altas, enquanto outros times com técnicos menos longevos também alcançaram boas posições.

A classificação final dos times reflete mais o desempenho das equipes como um todo do que a longevidade dos técnicos. Outros fatores, como a qualidade do elenco, estratégias táticas, lesões de jogadores e outros aspectos, também influenciam no resultado final.

O gráfico de dispersão nos mostra que não há uma tendência clara entre a posição do time e o tempo do treinador mais longevo. Os pontos estão dispersos ao longo do gráfico, indicando que não há uma relação linear entre essas variáveis.

## 
