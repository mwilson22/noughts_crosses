NOUGHT = 'O'
CROSS = 'X'
EMPTY = ' '


class Board():
    def __init__(self, position=None):
        if position is None:
            self.position = self.make_empty_position()
        else:
            self.position = position

    def __str__(self):
        return f'{self.position}'

    def print_position(self):
        print('\n', end='')
        for r in range(3):
            for c in range(3):
                print(f' {self.position[r][c]}', end='')
                if c < 2:
                    print(' │', end='')
                elif r < 2:
                    print('\n⎯⎯⎯┼⎯⎯⎯┼⎯⎯')
        print('\n')

    def make_empty_position(self):
        return [[' ' for _ in range(3)] for _ in range(3)]
