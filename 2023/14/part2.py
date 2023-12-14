from collections import Counter

import numpy as np

input_file = open("./input.txt", "r")
data = input_file.read()


def hash_grid(grid):
    return hash(tuple(["".join(row) for row in grid]))


cycles = 1_000_000_000

dir_map = {
    0: "N",
    1: "W",
    2: "S",
    3: "E",
}

lines = np.array([np.array([c for c in x]) for x in data.splitlines()])


def shift_grid(grid, dir="W"):
    rotations = 0

    if dir == "N":
        rotations = 1
    elif dir == "E":
        rotations = 2
    elif dir == "S":
        rotations = 3

    rotated_grid = np.rot90(grid, rotations)
    shifted_grid = shift_rocks(rotated_grid)

    # Rotate back
    grid = np.rot90(shifted_grid, 4 - rotations)

    return grid


def shift_rocks(lines):
    new_grid = []

    for line in lines:
        s = "".join(line)
        curr_line = ""
        split = [u for x in s.split("#") for u in (x, "#")]
        split = split[: len(split) - 1]
        for group in split:
            if group == "":
                continue

            if group == "#":
                curr_line += "#"
                continue

            rocks = group.count("O")
            empty = group.count(".")

            curr_line += "O" * rocks + "." * empty

        new_grid.append([c for c in curr_line])

    return new_grid


def count_score(lines):
    total = 0
    for i, line in enumerate(lines):
        counter = Counter(line)
        total += (len(lines) - i) * counter.get("O") if "O" in counter else 0

    return total


grid = lines
seen = [0]
scores = [0]

# Find cycles
for i in range(cycles):
    grid = shift_grid(grid, "N")
    grid = shift_grid(grid, "W")
    grid = shift_grid(grid, "S")
    grid = shift_grid(grid, "E")

    hashed_grid = hash_grid(grid)
    scores.append(count_score(grid))
    if hashed_grid in seen:
        break

    seen.append(hashed_grid)

first_step = seen.index(hashed_grid)
cycle = len(seen) - first_step
want = int(((cycles) - first_step) % cycle + first_step)
solution = scores[want]
print(solution)

input_file.close()
