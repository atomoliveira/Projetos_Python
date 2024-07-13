#O jogo da megasena consiste em acertar seis dos sessenta números disponíveis em um volante. 
# Fazer um programa para calcular a quantidade de jogos que temos que fazer, 
# para com certeza acertar o resultado da megasena. 
# Admitindo que faremos jogos de seis números por volante, 
# o programa deverá exibir quais seriam estes números em cada volante, 
# ou seja, exibir todos os resultados possíveis.

from itertools import combinations

# Total de números disponíveis no volante
total_numeros = 60

# Quantidade de números a serem escolhidos em cada jogo
numeros_por_jogo = 6

# Gerando todas as combinações possíveis
combinacoes = combinations(range(1, total_numeros + 1), numeros_por_jogo)

# Calculando o número total de combinações
total_combinacoes = sum(1 for _ in combinacoes)

print(f"Total de combinações possíveis: {total_combinacoes}")
