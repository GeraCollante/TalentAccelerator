print('hello')

def find_empty(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return (row, col)
    return None

def find_possible(grid, row, col):
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        if grid[row][i] in values:
            values.remove(grid[row][i])
    for i in range(9):
        if grid[i][col] in values:
            values.remove(grid[i][col])
    box_x = row // 3
    box_y = col // 3
    for i in range(box_x * 3, box_x * 3 + 3):
        for j in range(box_y * 3, box_y * 3 + 3):
            if grid[i][j] in values:
                values.remove(grid[i][j])
    return values

# create a function that solves a sudoku
def solve(grid):
    # find the first empty space
    empty = find_empty(grid)
    # if there is no empty space, return the grid
    if not empty:
        return grid
    # if there is an empty space, find the possible values for that space
    row, col = empty
    values = find_possible(grid, row, col)
    # for each possible value
    for value in values:
        # create a new grid with the value in that space
        new_grid = grid[:]
        new_grid[row][col] = value
        # solve the new grid
        solved = solve(new_grid)
        # if the new grid is solved, return the solved grid
        if solved:
            return solved
    return False