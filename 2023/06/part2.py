input_file = open("./input.txt", "r")

lines = input_file.readlines()
race_time = int("".join([x for x in lines[0].split(":")[1].strip().split(" ") if not x == ""]))
target_distance = int("".join([x for x in lines[1].split(":")[1].strip().split(" ") if not x == ""]))

total = 0

for j in range(1, race_time):
    holding = j
    going = race_time - holding
    distance = holding * going

    if distance > target_distance:
        total += 1

print(total)   
input_file.close()