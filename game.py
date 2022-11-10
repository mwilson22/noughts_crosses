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

    game_node = Node(NOUGHT)
    computer = MinimaxPlayer(game_node)
    computer.random_move()

    while True:
        tmp = game_node.symbol
        game_node.symbol = game_node.opposite_symbol
        game_node.opposite_symbol = tmp

        computer.make_move()


def get_user_choices():
    while True:
        symbol = input('\nPlay X or O? ["'"X"'" / "'"O"'"]')
        if symbol in [NOUGHT, CROSS, NOUGHT.lower(), CROSS.lower()]:
            break
        else:
            print(' / '.join([NOUGHT, NOUGHT.lower(), CROSS, CROSS.lower()]), ' only please ')

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

    if symbol in [NOUGHT, NOUGHT.lower()]:
        computer_symbol = CROSS
    else:
        computer_symbol = NOUGHT

    return computer_symbol, difficulty


def play():
    comp_plays_first = False
    computer_symbol, difficulty = get_user_choices()

    game_node = Node(computer_symbol)
    comp_minimax = MinimaxPlayer(game_node)
    comp_random = RandomPlayer(game_node)
    human = HumanPlayer(game_node)

    if comp_plays_first:
        comp_random.make_move()
    else:
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
