from board import *

COMPUTER = 0
HUMAN = 1
MINIMAX = 10


class node(board):
    def __init__(self, position=None, symbol=EMPTY):
        super().__init__(position)
        self.symbol = symbol            # node is either a nought or cross
        self.opposite_symbol = NOUGHT if self.symbol == CROSS else CROSS
        self.depth = 0
        self.move_values = [0.0] * 9    # Win-weighting for each child node
        self.tree_total = 0             # Win-weighting for this node

    def __str__(self):
        self.print_position()

    def print_position(self):
        return super().print_position()

    def num_empty_squares(self):
        empty_sqrs = 0
        for row in self.position:
            empty_sqrs += row.count(EMPTY)
        return empty_sqrs

    def whose_move(self):
        if self.depth % 2 == 0:
            return HUMAN
        else:
            return COMPUTER

    def strongest_move(self):
        # Select from empty squares only
        i = 0
        while i < len(self.move_values):
            if self.position[i // 3][i % 3] != EMPTY:
                self.move_values[i] = -MINIMAX - 1
            i += 1

        max_value = max(self.move_values)
        return self.move_values.index(max_value)

    def is_winner(self, player):
        """ Test for a win """
        if player is COMPUTER:
            symbol = self.symbol
        else:
            symbol = self.opposite_symbol

        for row in range(3):
            if all(square == symbol for square in self.position[row]):
                return True

        for col in range(3):
            coln = [self.position[i][col] for i in range(3)]
            if all(square == symbol for square in coln):
                return True

        diag_1 = [self.position[i][i] for i in range(3)]
        if all(square == symbol for square in diag_1):
            return True

        diag_2 = [self.position[2 - i][i] for i in range(3)]
        if all(square == symbol for square in diag_2):
            return True

        return False

    def traverse(self):
        if self.is_winner(self.whose_move()) is True:
            if self.whose_move() == COMPUTER:
                self.tree_total = MINIMAX - self.depth
            else:
                self.tree_total = self.depth - MINIMAX
            return

        if self.num_empty_squares != 0:
            for row in range(3):
                for col in range(3):
                    if self.position[row][col] == EMPTY:
                        next_node = node(self.position, self.symbol)
                        if self.whose_move() == HUMAN:
                            next_node.position[row][col] = self.symbol
                        else:
                            next_node.position[row][col] = self.opposite_symbol
                        next_node.depth = self.depth + 1

                        next_node.traverse()

                        self.position[row][col] = EMPTY
                        self.move_values[3 * row + col] = next_node.tree_total

        values = list(filter(lambda x: x != 0, self.move_values))
        if values == []:
            self.tree_total = 0
        elif self.whose_move() == COMPUTER:
            self.tree_total = min(values)
        else:
            self.tree_total = max(values)

    def make_move(self):
        self.traverse()

        max_index = self.strongest_move()
        self.position[max_index // 3][max_index % 3] = self.symbol
        self.move_values = [0.0] * 9    # Clear the move_values

        if self.is_winner(COMPUTER):
            self.print_position()
            print("Computer wins!")
            exit()


def play():
    my_board = board()

    my_node = node(my_board.position, NOUGHT)

    while True:
        my_board.print_position()

        """
        get string input
        check it's a digit
        convert to int
        minus 1
        check it's 1<9
        check it's not an empty square

        """
        while True:
            move_str = input("Your move: [1->9]")
            if move_str.isdigit() == True:
                move = int(move_str) - 1
                if move in range(0, 9):
                    if my_node.position[move // 3][move % 3] == EMPTY:
                        my_node.position[move // 3][move % 3] = 'X'
                        break

        if my_node.is_winner(HUMAN):
            my_node.print_position()
            print("You win!")
            exit()
        elif my_node.num_empty_squares() == 0:
            my_node.print_position()
            print("Draw!")
            exit()

        my_node.make_move()
        if my_node.is_winner(COMPUTER):
            my_node.print_position()
            print("Computer wins!")
            exit()


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

    my_node = node(my_board.position, NOUGHT)
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
