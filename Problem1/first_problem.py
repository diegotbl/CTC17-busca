import Problem1.n_queens as n_queens
import time
import Problem1.board as board


def main():
    """
    Solving the problem of the N queens for N = 10, 15, 20 and 25
    """
    # Solving 'n_times' times for each N and printing elapsed times
    n_times = 100

    for N in range(10, 26, 5):
        mean_time = 0
        mean_generated_boards = 0
        print("N = ", N)
        min_time = 1000
        max_time = 0
        for i in range(n_times):
            t_start = time.clock()
            queen_pos, generated_boards = n_queens.n_queens(N)
            t_finish = time.clock()
            if t_finish - t_start < min_time:
                min_time = t_finish - t_start
            if t_finish - t_start > max_time:
                max_time = t_finish - t_start
            mean_time += t_finish - t_start
            mean_generated_boards += generated_boards
            print("Elapsed time: ", t_finish - t_start, "s. Number of generated boards: ", generated_boards)
            print("Solution found:")
            board.print_board(queen_pos)
        mean_time /= n_times
        mean_generated_boards /= n_times

        print("Mean time for N = ", N, ": ", mean_time, "s")
        print("Minimum time for N = ", N, ": ", min_time, "s. Maximum time: ", max_time)
        print("Generated boards' mean for N = ", N, ": ", mean_generated_boards)


if __name__ == "__main__":
    main()
