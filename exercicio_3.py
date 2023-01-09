# Exercício 3
# Utilize o módulo random da linguagem Python para gerar um array com 100 num.
# Cada um desses números deve ser a média de n números gerados aleatoriamente.
# Qual é a ordem de complexidade de tempo e de espaço deste programa?

import random


def exercise(n):
    final_arr = []

    for _ in range(100):
        avarage = 0
        for _ in range(n):
            avarage += random.randrange(1, n)

        avarage = avarage / n
        final_arr.append(avarage)

    return final_arr


print(exercise())

# Complexidade de tempo linear, O(n), pois ele aumenta a quantidade
# de operações proporcional a quantidade de dados na entrada

# Complexidade de espaço constante, O(1), pois o teu valor final
# independe do numero de dados colocados na entrada
