from traverse_tree import *
from players import *


def comp_vs_comp():
    game_node = node(NOUGHT)
    computer1 = minimax_player(game_node)
    computer1.random_move()

    while True:
        computer1.make_move()

        tmp = game_node.symbol
        game_node.symbol = game_node.opposite_symbol
        game_node.opposite_symbol = tmp


def play():
    game_node = node(NOUGHT)

    computer = random_player(game_node)
    # computer = minimax_player(game_node)
    human = human_player(game_node)

    # Computer plays first
    # computer.random_move()

    game_node.print_position()
    while True:
        human.make_move()
        computer.make_move()


if __name__ == '__main__':
    play()

    # comp_vs_comp()
