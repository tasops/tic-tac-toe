import os


field = '| |'
players = {'X': '|x|', 'O': '|o|'}
rqd_inrow = 3
directions = {'horizontal', 'vertical', 'diagonal', 'rev_diagonal'}


def main():

    # Create the matrix
    size = 3
    grid = [[field] * size for row in range(size)]

    while True:
        for player in players:
            # Check the matrix horizontally, vertically and diagonally
            for direction in directions:
                for row in range(len(grid)):
                    # Reset the count when changing the line
                    x_inline = 0
                    o_inline = 0
                    for column in range(len(grid[row])):
                        # Setup the direction based on picked direction
                        if direction == 'horizontal':
                            value = grid[row][column]
                        elif direction == 'vertical':
                            value = grid[column][row]
                        elif direction == 'diagonal':
                            value = grid[column][column]
                        elif direction == 'rev_diagonal':
                            value = grid[(len(grid) - 1) - column][column]

                        # Check the field
                        if value == players.get('X'):
                            x_inline += 1
                        elif value == players.get('O'):
                            o_inline += 1
                        else:
                            x_inline = 0
                            o_inline = 0

                        # If in that direction there is
                        # required number of valid values in a row, then win
                        if x_inline == rqd_inrow or o_inline == rqd_inrow:
                            main()

            while True:
                os.system('cls' if os.name == 'nt' else 'clear')

                # Display whose turn it is
                print(f'Turn: {player}\'s\n')

                # Print the board with coordinates
                print(
                    ' ' + ''.join([f' {column_number} ' for column_number in range(len(grid))]))
                for row_number, row in enumerate(grid):
                    print(str(row_number) + ''.join(row))

                # Take input
                try:
                    row = int(input('\nRow: '))
                    column = int(input('Column: '))
                except ValueError:
                    continue
                # Check if input is in range
                if row < size and row >= 0 and column < size and column >= 0:
                    # Then check if the choosen field is not occupied
                    if grid[row][column] == field:
                        # Draw on a board and give the turn for another player
                        grid[row][column] = players.get(player)
                        break


if __name__ == '__main__':
    main()
