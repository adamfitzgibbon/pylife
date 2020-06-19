from random import random
from os import system
from time import sleep
from functools import reduce
from copy import deepcopy
from patterns import Patterns

def print_board(game, step):
    system('clear')
    print(f"Step {step}")
    for row in game:
        print(row)


def get_neighbor_indices(game, x, y):
    up = y - 1 if y > 0 else len(game) - 1
    down = y + 1 if y < len(game) - 1 else 0
    left = x - 1 if x > 0 else len(game[0]) - 1
    right = x + 1 if x < len(game[0]) - 1 else 0

    return [(left, up), (x, up), (right, up), (left, y), (right, y),
            (left, down), (x, down), (right, down)]


def get_living_neighbor_count(game, x, y):
    neighbors = get_neighbor_indices(game, x, y)
    return reduce(
        lambda accumulator, item: accumulator + game[item[1]][item[0]],
        neighbors,
        0)


def progress(game):
    new_state = deepcopy(game)
    for (y, row) in enumerate(game):
        for (x, cell) in enumerate(row):
            living_neighbors = get_living_neighbor_count(game, x, y)
            if cell and living_neighbors not in (2, 3):
                new_state[y][x] = 0
            if not cell and living_neighbors == 3:
                new_state[y][x] = 1
    return new_state


def play():
    # game = [[1 if random() > .3 else 0 for x in range(10)] for y in range(10)]
    patterns = Patterns()
    game = patterns.toad()
    for step in range(100):
        print_board(game, step)
        sleep(.5)
        game = progress(game)


play()
