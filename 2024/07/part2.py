import itertools

input_file = open("./input.txt", "r")

lines = input_file.read().split("\n")

input_file.close()

solution = 0

def gen_operators(n):
    operators = ["*", "+", "|"]
    combinations = list(itertools.product(operators, repeat=n-1))
    return [''.join(combination) for combination in combinations]

for line in lines:
    line = line.split(": ")
    value = int(line[0])
    numbers = [int(x) for x in line[1].split(" ")]

    operators = gen_operators(len(numbers))

    for options in operators:
        curr_val = numbers[0]

        for i, op in enumerate(options):
            if op == "+":
                curr_val += numbers[i+1]
            elif op == "*":
                curr_val *= numbers[i+1]
            elif op == "|":
                tmp = curr_val
                curr_val = int(f"{tmp}{numbers[i+1]}")

        if curr_val == value:
            solution += value
            break

print(solution)