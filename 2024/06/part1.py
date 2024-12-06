import numpy as np

input_file = open("./input.txt", "r")

lines = input_file.readlines()

input_file.close()

P = complex

grid = np.array([np.array([c for c in line if c != "\n"]) for line in lines])

def p_to_xy(dir):
    return int(dir.real), int(dir.imag)

current_pos = P(0, 0)
dir = -1j
left_grid = False

for row, line in enumerate(grid):
    for col, pos in enumerate(line):
        if pos == "^":
            current_pos = P(col, row)

visited = []

def move(grid, current_pos, dir):
    reached_block = False
    while not reached_block:
        next_pos = current_pos + dir
        x, y = p_to_xy(next_pos)

        if y > len(grid)-1 or x > len(grid[0])-1 or y < 0 or x < 0:
            print("Leaving grid")
            global left_grid
            left_grid = True
            reached_block = True
        elif grid[y][x] == "#":
            reached_block = True
        else:
            if [y, x] not in visited:
                visited.append([y, x])

            prev_x, prev_y = p_to_xy(current_pos)
            current_pos = next_pos
            grid[y][x] = "^"
            grid[prev_y][prev_x] = "X"
    
    dir *= 1j

    return grid, current_pos, dir

while not left_grid:
    print(grid)
    grid, current_pos, dir = move(grid, current_pos, dir)
    print("-"*10)
    print(grid)
    print("-"*10)
    # left_grid = True

print(len(visited) + 1)