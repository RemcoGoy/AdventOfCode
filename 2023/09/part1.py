input_file = open("./input.txt", "r")

lines = input_file.readlines()

solution = 0

for line in lines:
    numbers = list(map(int, line.split()))
    differences = numbers

    next_diff = 0

    while not all(difference == 0 for difference in differences):
        differences = [j - i for i, j in zip(differences[:-1], differences[1:])]
        next_diff += differences[-1]

    solution += next_diff + numbers[-1]

print(solution)
input_file.close()
