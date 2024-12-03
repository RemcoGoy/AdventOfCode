import re

input_file = open("./input.txt", "r")

lines = input_file.readlines()

input_file.close()
rgx = "mul\(\d*\,\d*\)"
solutions = 0
for line in lines:
    matches: list[str] = re.findall(rgx, line)

    for match in matches:
        match = match.replace("mul(", "").replace(")", "")
        match_numbers = [int(x) for x in match.split(",")]
        solutions += match_numbers[0] * match_numbers[1]

print(solutions)