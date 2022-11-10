from board import *

COMPUTER = 0
HUMAN = 1
MINIMAX = 10


class Node(Board):
    """Main class for the game

    On init, symbol defines if computer is O or X
    """

    def __init__(self, symbol=EMPTY, position=None):
        super().__init__(position)
        self.symbol = symbol            # node is either a nought or cross
        self.opposite_symbol = NOUGHT if self.symbol == CROSS else CROSS
        self.depth = 0
        self.move_values = [0.0] * 9    # Win-weighting for each child node
        self.tree_total = 0             # Win-weighting for this node

    def num_empty_squares(self):
        empty_sqrs = 0
        for row in self.position:
            empty_sqrs += row.count(EMPTY)
        return empty_sqrs

    def reset_node(self):
        self.move_values = [0.0] * 9    # Clear the move_values

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
        symbol = self.symbol if player is COMPUTER else self.opposite_symbol

        # Check rows and cols
        for row_col in range(3):
            coln = [self.position[i][row_col] for i in range(3)]
            if all(square == symbol for square in coln) or \
               all(square == symbol for square in self.position[row_col]):
                return True

        diag_1 = [self.position[i][i] for i in range(3)]
        if all(square == symbol for square in diag_1):
            return True

        diag_2 = [self.position[2 - i][i] for i in range(3)]
        if all(square == symbol for square in diag_2):
            return True

        return False

    def traverse(self):
        """ Traverses the entire game tree depth first (DFS)
        """

        # If a win, records the minimax value and returns
        if self.is_winner(self.whose_move()) is True:
            if self.whose_move() == COMPUTER:
                self.tree_total = MINIMAX - self.depth
            else:
                self.tree_total = self.depth - MINIMAX
            return

        # Traverse the whole tree and record each result
        if self.num_empty_squares != 0:
            for row in range(3):
                for col in range(3):
                    if self.position[row][col] == EMPTY:
                        next_node = Node(self.symbol, self.position)
                        if self.whose_move() == HUMAN:
                            next_node.position[row][col] = self.symbol
                        else:
                            next_node.position[row][col] = self.opposite_symbol
                        next_node.depth = self.depth + 1

                        next_node.traverse()

                        self.position[row][col] = EMPTY
                        self.move_values[3 * row + col] = next_node.tree_total

        # All moves traversed - run minimax algo
        values = list(filter(lambda x: x != 0, self.move_values))
        if values == []:
            self.tree_total = 0
        elif self.whose_move() == COMPUTER:
            self.tree_total = min(values)
        else:
            self.tree_total = max(values)
