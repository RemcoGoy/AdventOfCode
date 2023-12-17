import numpy as np
from part1 import find_path

input_file = open("./input.txt", "r")
data = input_file.read()

grid = np.array([[int(c) for c in x] for x in data.splitlines()])

print(find_path(grid, 4, 10))

input_file.close()
