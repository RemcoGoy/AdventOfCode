from math import lcm
from typing import List

input_file = open("./input.txt", "r")

lines = input_file.readlines()


def navigate_network(instructions, network, starting_node):
    current_node = starting_node
    steps = 0
    instruction_index = 0

    while not current_node.endswith("Z"):
        if instructions[instruction_index] == "L":
            current_node = network[current_node][0]
        else:
            current_node = network[current_node][1]

        steps += 1
        instruction_index = (instruction_index + 1) % len(instructions)

    return steps


# Define the network and instructions
instructions = [c for c in lines.pop(0).split("\n")[0]]

network = {}
starting_nodes: List[str] = []

current_step = None

for line in lines:
    if line == "\n":
        continue

    s = line.split(" = ")
    key = s[0]
    value = s[1].strip("\n")
    value = value[1 : len(value) - 1].split(", ")

    network[key] = value

    if key.endswith("A"):
        starting_nodes.append(key)

    if not current_step:
        current_step = key

print(starting_nodes)

# Call the function
steps = []
for starting_node in starting_nodes:
    steps.append(navigate_network(instructions, network, starting_node))

needed = steps[0]
for step in steps[1:]:
    needed = lcm(needed, step)
print(f"It takes {needed} steps to reach ZZZ.")

input_file.close()
