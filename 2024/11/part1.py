from tqdm import tqdm

input_file = open("./input.txt", "r")

line = input_file.readline()

input_file.close()

line = line.split(" ")

BLINKS = 75


def clean_leading_zeroes(number: str):
    n = int(number)
    return str(n)


for i in tqdm(range(BLINKS)):
    current_line = []

    for n in line:
        if n == "0":
            current_line.append("1")
        elif len(n) % 2 == 0:
            first_part = n[: int(len(n) / 2)]
            second_part = n[int(len(n) / 2) :]

            current_line.append(clean_leading_zeroes(first_part))
            current_line.append(clean_leading_zeroes(second_part))
        else:
            current_line.append(str(int(n) * 2024))

    line = current_line

print(len(line))
