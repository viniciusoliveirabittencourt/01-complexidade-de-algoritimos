
def naval_game(ships_position, target):
    x, y = target
    if ships_position[x][y] == 1:
        return True

    else:
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