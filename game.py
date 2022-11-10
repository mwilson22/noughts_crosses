import random
from traverse_tree import *
from players import *

MINIMAX = 0
RANDOM = 1


def decision(difficulty):
    probability = difficulty / 5
    return random.random() < probability


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
    comp_plays_first = False
    difficulty = 3  # 0->5 0=random 5=unbeatable

    while True:
        str_difficulty = input('\nChoose difficulty: [0..5 where 0=random 5=unbeatable] ')
        try:
            difficulty = int(str_difficulty)
        except ValueError:
            print('0..5 only please')
            continue
        if 0 <= difficulty <= 5:
            break
        else:
            print('0..5 only please')

    game_node = node(computer_symbol)

    comp_minimax = minimax_player(game_node)
    comp_random = random_player(game_node)

    human = human_player(game_node)

    game_node.print_position()

    if comp_plays_first:
        comp_random.make_move()
        game_node.print_position()

    while True:
        human.make_move()
        if decision(difficulty):
            comp_minimax.make_move()
        else:
            comp_random.make_move()


if __name__ == '__main__':
    computer_v_computer = False

    if computer_v_computer:
        comp_vs_comp()
    else:
        play()
