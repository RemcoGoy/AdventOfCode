from functools import cache


@cache
def apply_rules(n: int):
    if n == 0:
        return [1]

    string_num = str(n)
    if len(string_num) % 2 == 0:
        l = len(string_num) // 2
        return [int(string_num[:l]), int(string_num[l:])]

    return [n * 2024]


@cache
def calculate_stones(stone: int, blinks: int) -> int:
    if blinks == 0:
        return 1

    transformed_stones = apply_rules(stone)
    return sum(calculate_stones(num, blinks - 1) for num in transformed_stones)


input_file = open("./input.txt", "r")

line = input_file.readline()

input_file.close()

line = [int(x) for x in line.split(" ")]

BLINKS = 75

total = 0
for stone in line:
    total += calculate_stones(stone, BLINKS)

print(total)
