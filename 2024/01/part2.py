input_file = open("./input.txt", "r")

l1, l2 = [], []

for line in input_file.readlines():
    s = line.split("   ")
    l1.append(s[0])
    l2.append(s[1].replace("\n", ""))

input_file.close()

solution = 0

l1 = [int(x) for x in l1]
l2 = [int(x) for x in l2]

c2 = {}

for x2 in l2:
    if not x2 in c2:
        c2[x2] = 1
    else:
        c2[x2] += 1

for x1 in l1:
    sub_solution = x1 * c2.get(x1, 0)
    solution += sub_solution

print(solution)