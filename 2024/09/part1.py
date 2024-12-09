input_file = open('./input.txt', "r")

line = input_file.read()

input_file.close()

lengths = [int(num) for num in line]
disk_map = [i // 2 if i % 2 == 0 else -1 for i, x in enumerate(lengths) for _ in range(x)]

while -1 in disk_map:
    if disk_map[-1] == (-1):
        disk_map.pop()
    else:
        index = disk_map.index(-1)
        disk_map[index] = disk_map.pop()

final = sum(i * x for i, x in enumerate(disk_map))
print(final)