input_file = open("./input.txt", "r")

l1, l2 = [], []

for line in input_file.readlines():
    s = line.split("   ")
    l1.append(s[0])
    l2.append(s[1].replace("\n", ""))

input_file.close()

solution = 0

l1 = [int(x) for x in sorted(l1)]
l2 = [int(x) for x in sorted(l2)]

for i in range(len(l1)):
    diff = abs(l1[i] - l2[i])
    solution += diff

print(solution)