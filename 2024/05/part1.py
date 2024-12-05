input_file = open("./input.txt", "r")

lines = input_file.readlines()

input_file.close()

is_rules = True
rules = []
updates = []

for line in lines:
    line: str = line.replace("\n", "")

    if line == "":
        is_rules = False
    elif is_rules:
        rules.append([int(x) for x in line.split("|")])
    else:
        updates.append([int(x) for x in line.split(",")])

valid_updates = []

for update in updates:
    valid = True
    for before in range(len(update) - 1):
        for after in range(before + 1, len(update)):
            curr_rules = list(filter(lambda x: update[before] == x[1], rules))

            first_numbers = list(map(lambda x: x[0], curr_rules))
            if update[after] in first_numbers:
                valid = False
    
    if valid:
        valid_updates.append(update)

middle_numbers = list(map(lambda x: x[int((len(x) - 1) / 2)], valid_updates))
print(sum(middle_numbers))