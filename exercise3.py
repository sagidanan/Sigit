"""
Exercise 3
to check who win we will sum each row / col / diagonal and see the sum
if the sum - its mean that player 1 win (1 + 1 + 1)
"""


def check_line(line):
    """
    this function will check if a line contain the same value
    :param line: a list
    :return: 0 - the elements doesnt contain the same value
             1 - the line contain only 1
             2 - the line contain only 2
    """
    x = line[0]
    for val in line:
        if x != val:
            return 0
    return x


def get_col(game, index):
    """
    this function will return the col of a specific index
    :param game: the board game
    :param index: the index
    :return: the col (presented as a list)
    """
    return [x[index] for x in game]


def get_main_diagonal(game):
    """
    this function will return the main diagonal
    :param game: the board game
    :return: the main diagonal (presented as a list)
    """
    return [game[i][i] for i in range(3)]


def get_second_diagonal(game):
    """
    this function will return the second diagonal
    :param game: the board game
    :return: the second diagonal (presented as a list)
    """
    return [game[i][-(i + 1)] for i in range(3)]


def check_win(game):
    """
    this function will check who is the winner
    :param game: the board game
    :return:    1 - player 1 is the winner
                2 - player 2 is the winner
                0 - Tie
    """
    # checking rows
    for row in game:
        win = check_line(row)
        if win != 0:
            return win

    # checking cols
    for i in range(3):
        win = check_line(get_col(game, i))
        if win != 0:
            return win

    # checking main diagonal
    win = check_line(get_main_diagonal(game))
    if win != 0:
        return win

    # checking second diagonal
    win = check_line(get_second_diagonal(game))
    if win != 0:
        return win
    return 0


def print_winner(winner):
    """
    this function will print the winner
    :param winner: can be 1 (player 1) / 2 (player 2) / 0 - Tie
    :return: None
    """
    if winner != 0:
        print("the winner is player number ", winner)
    else:
        print("Tie")


def main():
    """
    main function
    """
    game = [[0, 2, 1],
            [2, 1, 0],
            [1, 1, 2]]

    print_winner(check_win(game))


if __name__ == "__main__":
    main()