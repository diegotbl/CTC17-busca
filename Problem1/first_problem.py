import Problem1.n_queens as n_queens
import time
import Problem1.board as board


def main():
    """
    Solving the problem of the N queens for N = 10, 15, 20 and 25
    """
    # Solving 10 times for each N and printing elapsed times
    for N in range(10, 26, 5):
        print("N = ", N)
        for i in range(10):
            t_start = time.clock()
            queen_pos = n_queens.n_queens(N)
            t_finish = time.clock()
            print(t_finish - t_start)
            print("Solution found:")
            board.print_board(queen_pos)


if __name__ == "__main__":
    main()
