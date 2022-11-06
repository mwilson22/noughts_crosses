from traverse_tree import *
import random


class player():
    """Parent class of all players

    Requires a game_node
    Provides functions for testing for wins
    """

    def __init__(self, game_node):
        self.game_node = game_node

    def test_for_win(self, player):
        def show_res_and_exit(res):
            self.game_node.print_position()
            print(res)
            exit()

        if self.game_node.num_empty_squares() == 0:
            show_res_and_exit("Draw!")
        elif self.game_node.is_winner(player):
            show_res_and_exit("You win!" if player == HUMAN else "Computer wins!")

    def test_and_display(self):
        self.test_for_win()
        self.game_node.print_position()


class human_player(player):
    """Takes input from the user

    Checks input is 0-9 and on an empty square
    """

    def test_for_win(self):
        super().test_for_win(HUMAN)

    def make_move(self):
        while True:
            move_str = input("Your move: [1->9]")
            if move_str.isdigit() == True:
                move = int(move_str) - 1
                if move in range(0, 9):
                    if self.game_node.position[move // 3][move % 3] == EMPTY:
                        self.game_node.position[move // 3][move %
                                                           3] = self.game_node.opposite_symbol
                        break
        self.test_and_display()


class computer_player(player):
    """Parent class of all computer players"""

    def test_for_win(self):
        super().test_for_win(COMPUTER)

    def random_move(self):
        while True:
            square = [random.randint(0, 2), random.randint(0, 2)]
            if self.game_node.position[square[0]][square[1]] == EMPTY:
                self.game_node.position[square[0]][square[1]] = self.game_node.symbol
                break


class minimax_player(computer_player):
    """The unbeatable player

    Uses the minimax algorithm to assess all possible moves
    Uses the node class to traverse the tree
    """

    def make_move(self):
        self.game_node.traverse()

        max_index = self.game_node.strongest_move()
        self.game_node.position[max_index // 3][max_index % 3] = self.game_node.symbol

        self.test_and_display()
        self.game_node.reset_node()


class random_player(computer_player):
    """Makes random moves"""

    def make_move(self):
        self.random_move()
        self.test_and_display()
