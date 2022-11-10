from traverse_tree import *
from players import *


def clear_position(pos):
    pos.clear()
    return [[EMPTY for _ in range(3)] for _ in range(3)]


def fill_row(pos, row, letter=EMPTY):
    pos[row] = [letter] * 3


def fill_col(pos, col, letter=EMPTY):
    for i in range(3):
        pos[i].pop(col)
        pos[i].insert(col, letter)


def fill_diag_1(pos, letter):
    for i in range(3):
        pos[i].pop(i)
        pos[i].insert(i, letter)


def fill_diag_2(pos, letter):
    for i in range(3):
        pos[2 - i].pop(i)
        pos[2 - i].insert(i, letter)


def test():
    comp_symbol = NOUGHT
    node = Node(comp_symbol)
    player = MinimaxPlayer(node)

    """
    node.position = [
        ['O', ' ', 'X'],
        ['X', ' ', ' '],
        ['X', 'O', 'O']
    ]
    """
    """
    node.position = [
        ['X', 'O', 'X'],
        ['O', 'O', ' '],
        [' ', ' ', ' ']
    ]
    """
    """
    node.position = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    """
    node.position = [
        ['O', ' ', 'X'],
        ['X', 'X', ' '],
        ['O', ' ', ' ']
    ]

    node.print_position()
    player.make_move()


test()
