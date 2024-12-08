import numpy as np

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

P = complex

grid = np.array([np.array([x for x in line]) for line in lines])

antennas = {}

for row, line in enumerate(grid):
    for col, cell in enumerate(line):
        if cell != ".":
            if cell in antennas:
                antennas[str(cell)].append(P(col, row))
            else:
                antennas[str(cell)] = [P(col, row)]

height = len(grid)
width = len(grid[0])

anti_nodes = set()

for k, v in antennas.items():
    print(f"Checking {k}")
    for i in range(len(v)):
        for j in range(i+1, len(v)):
            print(v[i], v[j])
            diff_1 = v[i] - v[j]
            anti_1 = v[i] + diff_1
            x, y = p_to_xy(anti_1)
            if not (x < 0 or x > width-1 or y < 0 or y > height-1):
                anti_nodes.add(anti_1)
                grid[y][x] = "#"

            diff_2 = v[j] - v[i]
            anti_2 = v[j] + diff_2
            x, y = p_to_xy(anti_2)
            if not (x < 0 or x > width-1 or y < 0 or y > height-1):
                anti_nodes.add(anti_2)
                grid[y][x] = "#"
    
    print("-"*20)

# pretty_print(grid)
print(len(anti_nodes))