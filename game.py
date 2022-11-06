from traverse_tree import *
from players import *

MINIMAX = 0
RANDOM = 1


def comp_vs_comp():
    """ Minimax vs minimax - always a draw

    Start with a random move to give a different game each time
    """

    game_node = node(NOUGHT)
    computer1 = minimax_player(game_node)
    computer1.random_move()

    while True:
        computer1.make_move()

        tmp = game_node.symbol
        game_node.symbol = game_node.opposite_symbol
        game_node.opposite_symbol = tmp


def play():
    computer_symbol = NOUGHT
    computer_engine = MINIMAX   # RANDOM or MINIMAX
    comp_plays_first = False

    game_node = node(computer_symbol)

    if computer_engine == MINIMAX:
        computer = minimax_player(game_node)
    elif computer_engine == RANDOM:
        computer = random_player(game_node)

    human = human_player(game_node)

    game_node.print_position()

    if comp_plays_first:
        computer.random_move()
        game_node.print_position()

    while True:
        human.make_move()
        computer.make_move()


if __name__ == '__main__':
    computer_v_computer = False

    if computer_v_computer:
        comp_vs_comp()
    else:
        play()
