import numpy as np
from itertools import product

input_file = open("./input.txt", "r")

lines = input_file.readlines()

input_file.close()

total = 0

lines = [[c for c in line if c != "\n"] for line in lines]
lines = np.array(lines)

pattern = 'XMAS'
dirs = list(product((-1, 0, +1), repeat=2))
dirs.remove((0, 0))
I, J = range(len(lines)), range(len(lines[0]))

for i, j in product(I, J):
    if lines[i][j] != 'X':
        continue
    for i_, j_ in dirs:
        for n in range(1, 4):
            ni, nj = i+i_*n, j+j_*n
            if ni not in I or nj not in J or lines[ni][nj] != pattern[n]:
                break
        else:
            total += 1

print(total)