input_file = open("./input.txt", "r")

lines = input_file.readlines()


def navigate_network(instructions, network):
    current_node = "AAA"
    steps = 0
    instruction_index = 0

    while current_node != "ZZZ":
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

current_step = None

for line in lines:
    if line == "\n":
        continue

    s = line.split(" = ")
    key = s[0]
    value = s[1].strip("\n")
    value = value[1 : len(value) - 1].split(", ")

    network[key] = value

    if not current_step:
        current_step = key


# Call the function
steps = navigate_network(instructions, network)
print(f"It takes {steps} steps to reach ZZZ.")

input_file.close()
