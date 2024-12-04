import numpy as np
from itertools import product

input_file = open("./input.txt", "r")

lines = input_file.readlines()

input_file.close()

total = 0

lines = [[c for c in line if c != "\n"] for line in lines]
lines = np.array(lines)

dirs = list(product((-1, +1), repeat=2))
I, J = range(1, len(lines)-1), range(1, len(lines[0])-1)

for i, j in product(I, J):
    if lines[i][j] != 'A':
        continue
    X = [lines[i+i_][j+j_] for i_, j_ in dirs]  # X-neighbors
    if X.count('M') == X.count('S') == 2 and X[1] != X[2]:  # prevent MAMxSAS
        total += 1


print(total)