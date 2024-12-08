import numpy as np

P = complex

input_file = open("./input.txt", "r")

lines = input_file.read().split("\n")

input_file.close()

def p_to_xy(dir):
    return int(dir.real), int(dir.imag)

def pretty_print(grid: np.array):
    for row in grid:
        for cell in row:
            print(cell, end="")
        
        print("\n", end="")


grid = np.array([np.array([x for x in line]) for line in lines])

height = len(grid)
width = len(grid[0])

def check_bounds(loc: P):
    x,y = p_to_xy(loc)
    if x < 0 or y < 0 or x > width - 1 or y > height - 1:
        return False
    return True

antennas = {}
anti_nodes = set()

for row, line in enumerate(grid):
    for col, cell in enumerate(line):
        if cell != ".":
            anti_nodes.add(P(col, row))
            if cell in antennas:
                antennas[str(cell)].append(P(col, row))
            else:
                antennas[str(cell)] = [P(col, row)]

for k, v in antennas.items():
    print(f"Checking {k}")
    for i in range(len(v)):
        for j in range(i+1, len(v)):
            print(v[i], v[j])
            diff_1 = v[i] - v[j]
            anti_1 = v[i] + diff_1
            in_bounds = check_bounds(anti_1)
            while in_bounds:
                x, y = p_to_xy(anti_1)
                anti_nodes.add(anti_1)
                grid[y][x] = "#"

                anti_1 += diff_1
                in_bounds = check_bounds(anti_1)

            diff_2 = v[j] - v[i]
            anti_2 = v[j] + diff_2
            in_bounds = check_bounds(anti_2)
            while in_bounds:
                x, y = p_to_xy(anti_2)
                anti_nodes.add(anti_2)
                grid[y][x] = "#"

                anti_2 += diff_2
                in_bounds = check_bounds(anti_2)
    
    print("-"*20)

def flatten(xss):
    return [x for xs in xss for x in xs]

pretty_print(grid)
print(len(anti_nodes))