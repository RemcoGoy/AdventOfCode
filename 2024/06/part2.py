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

start_pos = current_pos
Loc = P
Dir = P
visited: set[tuple[Loc, Dir]] = set()

def turn(dir):
    return dir * 1j

class oob(Exception):
    pass

class loop(Exception):
    pass

def step(grid, current_pos, dir):
    next_pos = current_pos + dir
    x, y = p_to_xy(next_pos)

    # Check out of bounds
    if y > len(grid)-1 or x > len(grid[0])-1 or y < 0 or x < 0:
        raise oob

    # Check block
    if grid[y][x] == "#":
        return False, P(0,0)

    return True, next_pos

def move(grid, current_pos, dir, history):
    history.add((current_pos, dir))
    while True:
        try:
            can_step, new_pos = step(grid, current_pos, dir)
        except oob:
            return {loc for loc, _ in history}

        if not can_step:
            dir = turn(dir)
        else:
            current_pos = new_pos

        entry = (current_pos, dir)
        if entry in history:
            raise loop
        else:
            history.add(entry)

u_pos = move(grid, current_pos, dir, visited)
to_check = u_pos - {start_pos}
c = 0
for loc in to_check:
    new_visited = set()
    curr_pos = start_pos
    grid_c = grid.copy()
    x,y = p_to_xy(loc)
    grid_c[y][x] = "#"
    try:
        move(grid_c, curr_pos, -1j, new_visited)
    except loop:
        c += 1

print(c)