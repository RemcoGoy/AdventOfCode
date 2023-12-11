import numpy as np

input_file = open("./input.txt", "r")
data = input_file.read()

chart = np.array([[c for c in x] for x in data.splitlines()])

expand_value = 1000000 - 1

row_expand_index = []

for i, line in enumerate(chart):
    if all(c == "." for c in line):
        row_expand_index.append(i)


# added = 0
# for i in row_expand_index:
#     chart = np.insert(chart, i + added, chart[i + added], axis=0)
#     added += 1

transpose_chart = np.transpose(chart)

col_expand_index = []
for i, col in enumerate(transpose_chart):
    if all(c == "." for c in col):
        col_expand_index.append(i)

# added = 0
# for i in col_expand_index:
#     transpose_chart = np.insert(transpose_chart, i + added, transpose_chart[i + added], axis=0)
#     added += 1

chart = np.transpose(transpose_chart)

galaxies = []
for y, line in enumerate(chart):
    for x, c in enumerate(line):
        if c == "#":
            galaxies.append((x, y))


def shortest_path(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def count_numbers_between(list_of_integers, new_integer_1, new_integer_2):
    new_integer_1, new_integer_2 = sorted([new_integer_1, new_integer_2])
    count = 0
    for integer in list_of_integers:
        if new_integer_1 <= integer <= new_integer_2:
            count += 1
    return count


solution = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        extra_cols = (
            count_numbers_between(col_expand_index, galaxies[i][0], galaxies[j][0]) * expand_value
        )

        extra_rows = (
            count_numbers_between(row_expand_index, galaxies[i][1], galaxies[j][1]) * expand_value
        )
        solution += shortest_path(galaxies[i], galaxies[j]) + extra_cols + extra_rows

print(solution)
input_file.close()
