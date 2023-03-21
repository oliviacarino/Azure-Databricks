tab = 2
print_var = True


def print_board_state(n, solution, indent=1):
    if len(solution) != n:
        return
    indent += tab
    for i in range(n):
        if i == 0:                  # printing the top of the board
            print(" "*indent, " ", "_"*((4*n)-1), sep="")

        print(" "*indent, "|", sep="", end="")
        if solution[n-(i+1)] != -1:  # queen placed in this row in the solution
            for j in range(n):
                print("_X_|" if solution[n-(i+1)] == j else "___|", end="")
        else:                       # no queen in solution in this row, move not in this row
            print("___|"*n, end="")   # so print an empty row
        print("")


# this method determines if a queen can be placed at proposed_row, proposed_col
# with current solution i.e. this move is valid only if no queen in current
# solution may attack the square at proposed_row and proposed_col
def is_valid_move(proposed_row, proposed_col, solution):
    temptab = tab
    temptab += 1
    # we need to check if any queen on the board in this solution can attack the proposed cell
    for i in range(0, proposed_row):
        old_row = i
        old_col = solution[i]
        diagonal_offset = proposed_row - old_row
        if (old_col == proposed_col or
            old_col == proposed_col - diagonal_offset or
                old_col == proposed_col + diagonal_offset):
            if print_var:
                print(temptab * "  ",
                      f"Invalid move: the proposed cell [{proposed_row}, {proposed_col}] is vulnerable to attack from the queen at [{i}, {solution[i]}].", sep="")
            return False
    if print_var:
        print(temptab * "  ",
              f"Valid move: the proposed cell [{proposed_row}, {proposed_col}] is safe.", sep="")
        print()
    return True


# Recursive worker function
def solve_n_queens_rec(n, solution, row, results):
    global tab
    global print_var
    # We have reached the last row (the nth row) with a valid
    # set of n queen positions
    if row == n:
        # Save this valid solution and backtrack so that the search for alternative solutions may continue
        print("  A valid solution found. We'll add it to the results array", sep="")
        print("  Solution: ", solution, sep="")
        results.append(solution)
        print_board_state(n, solution, 1)
        if print_var:
            print("\n Similarly, we'll find other such valid solutions")
        print_var = False
        print()
        return

    for i in range(0, n):
        if print_var:
            print(tab*"  ", "Placing queen ", row + 1, " in row ", row, sep="")
        valid = is_valid_move(row, i, solution)
        if valid:
            temp = tab + 1
            # Add this valid move to the current solution
            if print_var:
                print(
                    temp*"  ", "Since the move is valid, we'll add it to the current solution", sep="")
                print(temp*"  ", solution, " ⟶ ", end="", sep="")
            solution[row] = i
            if print_var:
                print(solution)
                print("")
            solve_n_queens_rec(n, solution, row + 1, results)
        else:
            if print_var:
                print(tab*"  ", "Backtracking...\n", sep="")


# Function to solve N-Queens problem
def solve_n_queens(n):
    print("\n Initialising variables")
    results = []
    solution = [-1] * n
    print("  Results: ", results, sep="")
    print("  Solution: ", solution, sep="")
    print_board_state(n, solution, 2)
    print("\n Placing the queens")
    solve_n_queens_rec(n, solution, 0, results)
    return len(results)


def main():
    n = [4, 5, 6, 7, 8]
    for i in range(len(n)):
        print(i+1, ". Queens: ",
              n[i], ", Chessboard: (", n[i], "x", n[i], ")", sep="")
        res = solve_n_queens(n[i])
        global tab
        tab = 2
        print("\nTotal solutions count for ",
              n[i], " queens on a ", n[i], "x", n[i], " chessboard: ", res, sep="")
        print("-"*100, "\n", sep="")


if __name__ == '__main__':
    main()
