import numpy as np

input_file = open("./input.txt", "r")
data = input_file.read()

chart = np.array([[c for c in x] for x in data.splitlines()])

row_expand_index = []

for i, line in enumerate(chart):
    if all(c == "." for c in line):
        row_expand_index.append(i)


added = 0
for i in row_expand_index:
    chart = np.insert(chart, i + added, chart[i + added], axis=0)
    added += 1

transpose_chart = np.transpose(chart)

col_expand_index = []
for i, col in enumerate(transpose_chart):
    if all(c == "." for c in col):
        col_expand_index.append(i)

added = 0
for i in col_expand_index:
    transpose_chart = np.insert(transpose_chart, i + added, transpose_chart[i + added], axis=0)
    added += 1

chart = np.transpose(transpose_chart)

galaxies = []
for y, line in enumerate(chart):
    for x, c in enumerate(line):
        if c == "#":
            galaxies.append((x, y))


def shortest_path(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


solution = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        solution += shortest_path(galaxies[i], galaxies[j])

print(solution)
input_file.close()
