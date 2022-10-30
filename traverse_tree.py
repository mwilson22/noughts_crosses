from board import *

PLAYER = 0
OPPONENT = 1
MINIMAX = 10


class node(board):
    def __init__(self, position=None, player=EMPTY, square=[0, 0]):
        super().__init__(position)
        self.player = player    # node is either a nought or cross
        self.square = square    # Move associated with this node
        self.depth = 0
        # Win-weighting for each child node
        self.move_values = [0.0] * 9
        self.tree_total = 0     # Win-weighting for this node

    def __str__(self):
        self.print_position()

    def print_position(self):
        return super().print_position()

    def empty_squares_count(self):
        return self.position.count(EMPTY)

    def opposite_symbol(self):
        return NOUGHT if self.player == CROSS else CROSS

    def whose_move(self):
        if self.depth % 2 == 0:
            return PLAYER
        else:
            return OPPONENT

    def is_winner(self, who):
        """ Test for a win """
        if who is PLAYER:
            player = self.player
        else:
            player = self.opposite_symbol()

        for row in range(3):
            if all(square == player for square in self.position[row]):
                return True

        for col in range(3):
            coln = [self.position[i][col] for i in range(3)]
            if all(square == player for square in coln):
                return True

        diag_1 = [self.position[i][i] for i in range(3)]
        if all(square == player for square in diag_1):
            return True

        diag_2 = [self.position[2 - i][i] for i in range(3)]
        if all(square == player for square in diag_2):
            return True

        return False

    def clear_current_square(self):
        self.position[self.square[0]][self.square[1]] = EMPTY

    def traverse(self):
        if self.is_winner(self.whose_move()) is True:
            if self.whose_move() == OPPONENT:
                self.tree_total = MINIMAX - self.depth
            else:
                self.tree_total = self.depth - MINIMAX
            self.clear_current_square()
            return

        if self.empty_squares_count != 0:
            for row in range(3):
                for col in range(3):
                    if self.position[row][col] == EMPTY:
                        next_node = node(
                            self.position, self.player, [row, col])
                        next_node.position[row][col] = self.player if self.whose_move(
                        ) == OPPONENT else self.opposite_symbol()
                        next_node.depth = self.depth + 1
                        next_node.traverse()
                        # self.print_position()
                        self.move_values[3 * row + col] = next_node.tree_total
                        # print(self.move_values)

        if self.whose_move() == PLAYER:
            self.tree_total = max(self.move_values)
        else:
            self.tree_total = min(self.move_values)

        # Set the square filled for this node back to empty
        if self.depth > 0:
            self.clear_current_square()

    def make_move(self):
        self.print_position()
        self.traverse()
        max_value = max(self.move_values)
        max_index = self.move_values.index(max_value)
        self.position[max_index // 3][max_index % 3] = self.opposite_symbol()
        self.print_position()
        print(self.move_values)
        print(max_index)
        return max_index


def play():
    my_board = board()

    my_node = node(my_board.position, NOUGHT, [0, 1])

    while True:
        my_board.print_position()
        move = int(input("Your move: [1->9]")) - 1
        my_node.position[move // 3][move % 3] = 'O'
        my_node.make_move()


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

    my_board.position = [
        ['X', 'O', 'X'],
        ['O', 'O', 'X'],
        [' ', ' ', ' ']
    ]

    """
    my_board.position = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    """

    my_board.print_position()

    my_node = node(my_board.position, NOUGHT, [0, 1])
    # my_node.print_position()

    # fill_row(my_board.position, 0, CROSS)
    # my_node.print_position()
    # print(my_node.is_winner())

    my_node.make_move()


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
play()

test()
