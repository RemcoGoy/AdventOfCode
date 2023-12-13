import numpy as np

input_file = open("./input.txt", "r")
data = input_file.read()

blocks = data.split("\n\n")


def calculate_symmetry(lines):
    indexes = [i for i in range(len(lines[0]))]
    possible_sym = list(indexes)

    for line in lines:
        for curr_pos in indexes:
            a = "".join(line[:curr_pos])
            b = "".join(line[curr_pos:][::-1])

            if len(a) == 0 or len(b) == 0:
                possible_sym.remove(curr_pos)
                continue

            if not (a.endswith(b) or b.endswith(a)):
                possible_sym.remove(curr_pos)

        indexes = list(possible_sym)

    return possible_sym


solution = 0

for block in blocks:
    lines = np.array([np.array([c for c in x]) for x in block.split("\n")])
    sym_index = calculate_symmetry(lines)
    if len(sym_index) == 0:
        lines = np.transpose(lines)
        sym_index = calculate_symmetry(lines)

        if not len(sym_index) == 0:
            solution += sym_index[0] * 100
    else:
        solution += sym_index[0]

print(solution)

input_file.close()
