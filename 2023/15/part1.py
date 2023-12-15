input_file = open("./input.txt", "r")
data = input_file.read()

current_value = 0


steps = data.split(",")
for step in steps:
    step_value = 0
    for c in step:
        step_value += ord(c)
        step_value *= 17
        step_value = step_value % 256

    current_value += step_value

print(current_value)

input_file.close()
