import re

input_file = open("./input.txt", "r")
lines = input_file.read()
input_file.close()

solution = 0

rgx = r"mul\(\d+\,\d+\)"

def get_mul(s:str):
    s = s.replace("mul(", "").replace(")", "")
    s_numbers = [int(x) for x in s.split(",")]
    return s_numbers[0] * s_numbers[1]

dos = lines.split("do()")
dos_dont = [x.split("don't()") for x in dos]

for dd in dos_dont:
    do = dd[0]
    matches = re.findall(rgx, do)
    for m in matches:
        solution += get_mul(m)

print(solution)