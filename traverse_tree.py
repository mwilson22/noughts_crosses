from board import *

MAX_DEPTH = 17


class node(board):
    def __init__(self, position=None, norc=EMPTY, square=[0, 0]):
        super().__init__(position)
        self.norc = norc        # node is either a nought or cross
        self.square = square    # Move associated with this node
        self.depth = 0
        # Win-weighting for each child node
        self.move_values = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.tree_total = 0     # Win-weighting for this node

    def __str__(self):
        self.print_position()

    def print_position(self):
        return super().print_position()

    def empty_squares_count(self):
        return self.position.count(EMPTY)

    def check_result(self):
        """ Test for a win """
        for row in range(3):
            if all(x == self.norc for x in self.position[row]):
                return True

        for col in range(3):
            coln = [self.position[i][col] for i in range(3)]
            if all(x == self.norc for x in coln):
                return True

        diag_1 = [self.position[i][i] for i in range(3)]
        if all(x == self.norc for x in diag_1):
            return True

        diag_2 = [self.position[2 - i][i] for i in range(3)]
        if all(x == self.norc for x in diag_2):
            return True

        return False

    # Look to see if current position gives a forced win next move
    def forced_win(self):
        pass

    def traverse(self):
        if self.check_result() is True:
            self.tree_total = 1
            self.position[self.square[0]][self.square[1]] = EMPTY
            return

        if self.depth is MAX_DEPTH:
            return

        if self.empty_squares_count != 0:
            for row in range(3):
                for col in range(3):
                    if self.position[row][col] == EMPTY:
                        next_node = node(
                            self.position, NOUGHT if self.norc == CROSS else CROSS, [row, col])
                        next_node.position[row][col] = next_node.norc
                        next_node.depth = self.depth + 1
                        next_node.traverse()
                        self.move_values[3 * row + col] = next_node.tree_total
                        self.tree_total += next_node.tree_total / 4
        # Set the square filled for this node back to empty
        self.position[self.square[0]][self.square[1]] = EMPTY
        # self.print_position()
        # print(id(self), 'leaving traverse', flush=True)

    def make_move(self):
        self.print_position()
        self.traverse()
        max_value = max(self.move_values)
        max_index = self.move_values.index(max_value)
        self.position[max_index // 3][max_index % 3] = 'T'
        self.print_position()
        print(self.move_values)
        print(max_index)


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
    # my_board.position = [['X', 'O', 'X'], ['O', 'X', ' '], [' ', ' ', ' ']]
    my_board.position = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    my_board.print_position()

    my_node = node(my_board.position, CROSS)
    # my_node.print_position()

    # fill_row(my_board.position, 0, CROSS)
    # my_node.print_position()
    print(my_node.check_result())

    my_node.make_move()


"""
    fill_col(my_node.position, 2, CROSS)
    my_node.print_position()
    print(my_node.check_result())

    my_node.position = clear_position(my_node.position)
    fill_diag_1(my_node.position, NOUGHT)
    my_node.print_position()
    print(my_node.check_result())

    my_node.position = clear_position(my_node.position)
    fill_diag_2(my_node.position, NOUGHT)
    my_node.print_position()
    print(my_node.check_result())

    my_node.position = clear_position(my_node.position)
    fill_col(my_node.position, 1, NOUGHT)
    my_node.print_position()
    print(my_node.check_result())
"""


test()
