#!/usr/bin/env python3

import os
import time
import copy

BOARD_SIZE = 3
BLANK_FIELD = ' '
O = 'O'
X = 'X'


class TTTBoard:
    def __init__(self):
        self.players = (O, X)
        self.board = [[BLANK_FIELD] * BOARD_SIZE for row in range(BOARD_SIZE)]

    # Prints the board with added formatting
    def draw_board(self):
        board_copy = copy.deepcopy(self.board)
        for row in board_copy:
            row = [f'|{field}|' for field in row]

            print(''.join(row))

    def pick_field(self, player, row, col):
        if ((self.board[row][col] == BLANK_FIELD)
            and (row >= 0 and row < BOARD_SIZE)
            and (col >= 0 and col < BOARD_SIZE)):

            self.board[row][col] = player
            return True

    def check_for_winner(self):
        # Horizontal check
        for row in self.board:
            if row.count(O) >= BOARD_SIZE:
                return O
            elif row.count(X) >= BOARD_SIZE:
                return X

        # Vertical check
        transposed_board = list(zip(*self.board))
        for column in transposed_board:
            if column.count(O) >= BOARD_SIZE:
                return O
            elif column.count(X) >= BOARD_SIZE:
                return X

        #TODO: Diagonal check


# Simple cross-platform function to clear the terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    Game = TTTBoard()

    while True:
        for player in Game.players:

            if (winner := Game.check_for_winner()):
                print(f'{winner} WON!')
                time.sleep(3)
                main()

            while True:
                clear()
                print(f'Player: {player}\n')
                Game.draw_board()

                try:
                    sel_row = int(input('Enter row: '))
                    sel_col = int(input('Enter column: '))
                except ValueError:
                    continue

                if Game.pick_field(player, sel_row, sel_col):
                    break


if __name__ == '__main__':
    main()
