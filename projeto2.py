import pandas as pd
import plotly.express as px

# Leitura do arquivo JSON
dados = pd.read_json('brasileirao-2019.json')

# Dicionário para armazenar a pontuação de cada time
pontuacao = {}

# Iteração sobre as rodadas e partidas
for rodada, partidas in dados.items():
    for partida in partidas:
        time_casa = partida['clubs']['home']
        time_fora = partida['clubs']['away']
        gols_casa = int(partida['goals']['home'])
        gols_fora = int(partida['goals']['away'])

        if gols_casa > gols_fora:
            pontuacao[time_casa] = pontuacao.get(time_casa, 0) + 3
        elif gols_casa < gols_fora:
            pontuacao[time_fora] = pontuacao.get(time_fora, 0) + 3
        else:
            pontuacao[time_casa] = pontuacao.get(time_casa, 0) + 1
            pontuacao[time_fora] = pontuacao.get(time_fora, 0) + 1

# Ordenação dos times por pontuação
times_ordenados = sorted(pontuacao.items(), key=lambda x: x[1], reverse=True)

# Impressão dos resultados
print("Classificação dos Times:")
for posicao, (time, pontos) in enumerate(times_ordenados, start=1):
    print(f"{posicao}. {time}: {pontos} pontos")


        # Atribuição de pontos
soma_rodadas = {}

for rodada_num, jogos in dados.items():
    for jogo in jogos:

        time_casa = jogo['clubs']['home']
        time_fora = jogo['clubs']['away']
        treinador_casa = jogo['coach']['home']
        treinador_fora = jogo['coach']['away']

        if time_casa not in soma_rodadas:
            soma_rodadas[time_casa] = {}
        if treinador_casa not in soma_rodadas[time_casa]:
            soma_rodadas[time_casa][treinador_casa] = 1
        else:
            soma_rodadas[time_casa][treinador_casa] += 1

        if time_fora not in soma_rodadas:
            soma_rodadas[time_fora] = {}
        if treinador_fora not in soma_rodadas[time_fora]:
            soma_rodadas[time_fora][treinador_fora] = 1
        else:
            soma_rodadas[time_fora][treinador_fora] += 1


# Criar uma lista de treinadores ordenadas decrescentemente pelo número de rodadas jogadas
treinadores_rodadas_ordenado = sorted(
    ((time, max(treinadores, key=treinadores.get), treinadores[max(treinadores, key=treinadores.get)]) for time, treinadores in soma_rodadas.items()),
    key=lambda x: x[2], reverse=True
)
# Imprimir os resultados
print("Dicionário Ordenado de Treinadores e Rodadas Jogadas:")
for time, treinador, rodadas in treinadores_rodadas_ordenado:
    print(f"Time: {time}, Treinador: {treinador}, Rodadas: {rodadas}")

dados = pd.read_json('brasileirao-2019.json')


pontuacao = {}

for rodada, partidas in dados.items():
    for partida in partidas:
        time_casa = partida['clubs']['home']
        time_fora = partida['clubs']['away']
        gols_casa = int(partida['goals']['home'])
        gols_fora = int(partida['goals']['away'])


        if time_casa not in pontuacao:
            pontuacao[time_casa] = {'pontos': 0, 'classificacao': 0, 'tecnico': None, 'rodadas': 0}
        if time_fora not in pontuacao:
            pontuacao[time_fora] = {'pontos': 0, 'classificacao': 0, 'tecnico': None, 'rodadas': 0}


        if gols_casa > gols_fora:
            pontuacao[time_casa]['pontos'] += 3
        elif gols_casa < gols_fora:
            pontuacao[time_fora]['pontos'] += 3
        else:
            pontuacao[time_casa]['pontos'] += 1
            pontuacao[time_fora]['pontos'] += 1


        tecnico_casa = partida['coach']['home']
        tecnico_fora = partida['coach']['away']


        if pontuacao[time_casa]['tecnico'] != tecnico_casa:
            pontuacao[time_casa]['rodadas'] += 1
            pontuacao[time_casa]['tecnico'] = tecnico_casa

        if pontuacao[time_fora]['tecnico'] != tecnico_fora:
            pontuacao[time_fora]['rodadas'] += 1
            pontuacao[time_fora]['tecnico'] = tecnico_fora


for posicao, (time, dados_time) in enumerate(times_ordenados, start=1):
    pontuacao[time]['classificacao'] = posicao


df = pd.DataFrame({
    'Times': [time for time, _ in times_ordenados],
    'Pontuação': [dados['pontos'] for _, dados in times_ordenados],
    'Classificação': [dados['classificacao'] for _, dados in times_ordenados],
    'Técnico': [dados['tecnico'] for _, dados in times_ordenados],
    'Rodadas com Técnico': [dados['rodadas'] for _, dados in times_ordenados]
})


fig = px.bar(df, x='Times', y='Pontuação', color='Classificação', text='Times',
             labels={'Pontuação': 'Pontuação', 'Times': 'Times'},
             title='Classificação dos Times - Campeonato Brasileiro 2019',
             height=600)


fig.update_traces(hovertemplate='<b>%{text}</b><br>Pontuação: %{y}<br>Classificação: %{color}' +
                  '<br>Técnico: %{customdata[0]}<br>Rodadas com Técnico: %{customdata[1]}',
                  customdata=df[['Técnico', 'Rodadas com Técnico']].values)


fig.update_layout(
    xaxis_title='Times',
    yaxis_title='Pontuação',
    legend_title='Classificação',
    xaxis_tickangle=45,
    showlegend=True
)


fig.show()

# Dicionário para armazenar a posição dos times na classificação
posicao_times = {time: posicao for posicao, (time, _) in enumerate(times_ordenados, start=1)}

# Criar uma lista de treinadores ordenadas decrescentemente pelo número de rodadas jogadas
treinadores_rodadas_ordenado = sorted(
    ((time, max(treinadores, key=treinadores.get), treinadores[max(treinadores, key=treinadores.get)]) for time, treinadores in soma_rodadas.items()),
    key=lambda x: x[2], reverse=True
)

# Preparar os dados para o gráfico de dispersão
posicoes = []
rodadas_treinador_longevo = []
for time, treinador, rodadas in treinadores_rodadas_ordenado:
    posicoes.append(int(posicao_times[time]))  # Converter para inteiro
    rodadas_treinador_longevo.append(rodadas)

# Criar o gráfico de dispersão
plt.scatter(posicoes, rodadas_treinador_longevo)
plt.xlabel('Posição do Time na Classificação')
plt.ylabel('Tempo do Técnico (Rodadas)')
plt.title('Posição do Time X Tempo do Técnico\n')

# Definir os valores e rótulos do eixo x como inteiros
plt.xticks(range(1, len(posicoes) + 1), range(1, len(posicoes) + 1))

# Exibe os nomes dos técnicos e times
for i, txt in enumerate(treinadores_rodadas_ordenado):
    plt.annotate(f' {txt[0]}', (posicoes[i], rodadas_treinador_longevo[i]), xytext=(5, 0), textcoords='offset points')

plt.show()