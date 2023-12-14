from collections import Counter

import numpy as np

input_file = open("./input.txt", "r")
data = input_file.read()

lines = np.array([np.array([c for c in x]) for x in data.splitlines()])


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


new_lines = np.transpose(lines)
shifted_lines = shift_rocks(new_lines)
grid = np.array([np.array([c for c in x]) for x in shifted_lines])
grid = np.transpose(grid)


def count_score(lines):
    total = 0
    for i, line in enumerate(lines):
        counter = Counter(line)
        total += (len(lines) - i) * counter.get("O") if "O" in counter else 0

    return total


solution = count_score(grid)
print(solution)

input_file.close()
