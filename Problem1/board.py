from random import shuffle


def print_board(queen_pos):
    """
    Prints board on screen
    :param queen_pos: list of queens' positions
    """
    board_size = len(queen_pos)

    for x in range(board_size):
        for y in range(board_size):
            if queen_pos[y] == x:
                print(' Q ', end='')
            else:
                print(' . ', end='')
        print()


def random_board(board_size):
    """
    Generates a random board of size 'board_size'. Returns the list of queens' positions
    """
    queen_pos = list(range(board_size))

    shuffle(queen_pos)

    return queen_pos
