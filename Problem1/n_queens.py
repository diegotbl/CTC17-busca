from copy import deepcopy
import Problem1.board as board


def n_queens(board_size):
    """
    Solves the N Queens puzzle for a 'board_size' sized board using Random Restart Hill Climbing algorithm
    """
    while True:
        queen_pos = board.random_board(board_size)
        last_number_attacks = 0

        # if 'last_number_attacks' equals the current heuristic means no movement was made
        # in the last iteration, therefore we reached a local minimum and should restart
        while last_number_attacks != attacking_queens(queen_pos):
            last_number_attacks = attacking_queens(queen_pos)
            for x_queen, y_queen in enumerate(queen_pos):
                # 'test_queen_pos' will be used for testing all possibilities for minimizing heuristic
                test_queen_pos = deepcopy(queen_pos)
                for i in range(board_size):
                    test_queen_pos[x_queen] = i
                    if attacking_queens(test_queen_pos) < attacking_queens(queen_pos):
                        queen_pos[x_queen] = i
                if attacking_queens(queen_pos) == 0:
                    return queen_pos


def attacking_queens(queen_pos):
    """
    Finds the number of attacking queens directly or indirectly. This will be used as heuristic.
    """
    attacks = 0

    for x_queen1, y_queen1 in enumerate(queen_pos):
        for x_queen2, y_queen2 in enumerate(queen_pos):
            if x_queen1 != x_queen2:        # otherwise it's the same queen and we just ignore.
                # first condition checks for horizontal; second, for main diagonal and third for antidiagonal attacks
                if y_queen1 == y_queen2 or \
                        y_queen2 - y_queen1 == x_queen2 - x_queen1 or \
                        x_queen1 + y_queen1 == x_queen2 + y_queen2:
                    attacks = attacks + 1

    attacks = attacks // 2       # each attack was counted twice

    return attacks
