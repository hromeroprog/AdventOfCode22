# open the input file
with open("input.txt") as f:
    # read the grid of trees from the file
    grid = [list(map(int, line.strip())) for line in f.readlines()]

# define the number of rows and columns in the grid
num_rows = len(grid)
num_cols = len(grid[0])

# define a function to check if a tree is visible from the left
def is_visible_from_left(row, col):
    for c in range(col):
        if grid[row][c] >= grid[row][col]:
            return False
    return True

# define a function to check if a tree is visible from the top
def is_visible_from_top(row, col):
    for r in range(row):
        if grid[r][col] >= grid[row][col]:
            return False
    return True

# define a function to check if a tree is visible from the bottom
def is_visible_from_bottom(row, col):
    for r in range(row + 1, num_rows):
        if grid[r][col] >= grid[row][col]:
            return False
    return True

# define a function to check if a tree is visible from the right
def is_visible_from_right(row, col):
    for c in range(col + 1, num_cols):
        if grid[row][c] >= grid[row][col]:
            return False
    return True

# initialize a counter for the number of visible trees
num_visible_trees = 0

# loop through each tree in the grid
for row in range(num_rows):
    for col in range(num_cols):
        # check if the tree is visible from the left, top, bottom, or right
        if is_visible_from_left(row, col) or is_visible_from_top(row, col) or is_visible_from_bottom(row, col) or is_visible_from_right(row, col):
            num_visible_trees += 1

# print the number of visible trees
print(num_visible_trees)