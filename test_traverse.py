from traverse_tree import *


def test():
    def clear_position(pos):
        pos.clear()
        return [[EMPTY for _ in range(3)] for _ in range(3)]

    def fill_row(pos, row, letter=EMPTY): pos[row] = [letter] * 3

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

    my_board = board()

    """
    my_board.position = [
        ['O', ' ', 'X'],
        ['X', ' ', ' '],
        ['X', 'O', 'O']
    ]
    """
    """
    my_board.position = [
        ['X', 'O', 'X'],
        ['O', 'O', ' '],
        [' ', ' ', ' ']
    ]
    """
    """
    my_board.position = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    """
    my_board.position = [
        ['O', ' ', 'X'],
        ['X', 'X', ' '],
        ['O', ' ', ' ']
    ]

    my_node = node(NOUGHT, my_board.position)
    # my_node.print_position()

    # fill_row(my_board.position, 0, CROSS)
    # my_node.print_position()
    # print(my_node.is_winner())

    my_node.print_position()
    my_node.make_move()
    my_node.print_position()


"""
    fill_col(my_node.position, 2, CROSS)
    my_node.print_position()
    print(my_node.is_winner())

    my_node.position = clear_position(my_node.position)
    fill_diag_1(my_node.position, NOUGHT)
    my_node.print_position()
    print(my_node.is_winner())

    my_node.position = clear_position(my_node.position)
    fill_diag_2(my_node.position, NOUGHT)
    my_node.print_position()
    print(my_node.is_winner())

    my_node.position = clear_position(my_node.position)
    fill_col(my_node.position, 1, NOUGHT)
    my_node.print_position()
    print(my_node.is_winner())
"""

test()
