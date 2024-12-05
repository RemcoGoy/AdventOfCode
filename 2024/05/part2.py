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

invalid_updates = []
reasons = []

for update in updates:
    valid = True
    curr_reasons = []
    for before in range(len(update) - 1):
        for after in range(before + 1, len(update)):
            curr_rules = list(filter(lambda x: update[before] == x[1], rules))

            first_numbers = list(map(lambda x: x[0], curr_rules))
            if update[after] in first_numbers:
                curr_reasons.append([update[after], update[before]])
                valid = False
    
    if not valid:
        invalid_updates.append(update)
        reasons.append(curr_reasons)

reordered = []
for i, update in enumerate(invalid_updates):
    graph = {}
    for rule in rules:
        if rule[1] not in graph and rule[1] in update:
            graph[rule[1]] = []
        if rule[1] in update and rule[0] in update:
            if rule[1] in graph:
                graph[rule[1]].append(rule[0])
    
    visited = set()
    temp = set()
    order = []
    
    def topological_sort(node):
        if node in temp:
            return False # Cycle detected
        if node in visited:
            return True
        temp.add(node)
        if node in graph:
            neighbors = sorted(graph[node], key=lambda x: update.index(x))
            for neighbor in neighbors:
                if not topological_sort(neighbor):
                    return False
        temp.remove(node)
        visited.add(node)
        order.append(node)
        return True
    
    valid = True
    for num in sorted(update, key=lambda x: update.index(x)):
        if not topological_sort(num):
            valid = False
            break
            
    if valid:
        print(f"Original update: {update}")
        print(f"Minimally reordered: {order[::-1]}")
    else:
        print(f"Update {update} cannot be reordered - contains cycle")
    
    reordered.append(order[::-1])
    print("-"*10)

middle_numbers = list(map(lambda x: x[int((len(x)-1)/2)], reordered))
print(sum(middle_numbers))