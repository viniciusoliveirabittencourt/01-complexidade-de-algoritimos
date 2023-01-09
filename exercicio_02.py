# Exercício 2
# Suponha que se está escrevendo uma função para um jogo de
# batalha naval.
# Dado um array bidimensional com n linhas e m colunas,
# e um par de coordenadas x para linhas e y para colunas,
# o algoritmo verifica se há um navio na coordenada alvo.
# Por exemplo:

# entrada = [ 0 0 0 0 1
#            0 0 0 0 1
#            1 1 1 1 1
#            0 0 0 1 0 ]

# resultado para (0, 4) = True
# resultado para (1, 1) = False

# Qual seria a ordem de complexidade da solução para este problema?
# E a complexidade de espaço?


def naval_game(ships_position, target):
    x, y = target
    if ships_position[x][y] == 1:
        return True

    return False


print(
    naval_game(
        [[0, 0, 0, 0, 1], [0, 0, 0, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 1, 0]],
        (1, 1),
    )
)

print(
    naval_game(
        [[0, 0, 0, 0, 1], [0, 0, 0, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 1, 0]],
        (0, 4),
    )
)

# Para minha surpresa, ao criar o código, percebi que se trata
# de um algoritimo linar, O(1), pois a quantidade de ações do código
# será a mesma, independente do tamanho do array.
# A complexidade de espaço também será O(1), pois o retorno não depende
# do tamanho do array.
