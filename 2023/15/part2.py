from collections import defaultdict

input_file = open("./input.txt", "r")
data = input_file.read()

current_value = 0


def get_label_value(label):
    label_value = 0

    for c in label:
        label_value += ord(c)
        label_value *= 17
        label_value = label_value % 256

    return label_value


boxes = defaultdict(lambda: [])
lens_map = {}

steps = data.split(",")
for step in steps:
    if "=" in step:
        lens, length = step.split("=")
    elif "-" in step:
        lens = step.split("-")[0]
        length = None

    label_value = get_label_value(lens)

    # Add lens
    if length:
        if lens in lens_map:
            # Update pos
            existing_lens = list(filter(lambda x: x["lens"] == lens, boxes[label_value]))[0]
            index = boxes[label_value].index(existing_lens)
            boxes[label_value][index] = {"lens": lens, "value": int(length)}
        else:
            boxes[label_value].append({"lens": lens, "value": int(length)})

        lens_map[lens] = label_value
    # Remove lens
    else:
        if lens in lens_map:
            box = lens_map[lens]
            boxes[box] = list(filter(lambda x: x["lens"] != lens, boxes[box]))
            del lens_map[lens]

for box in boxes:
    for i, lens in enumerate(boxes[box]):
        curr_value = int(box) + 1
        curr_value *= i + 1
        curr_value *= lens["value"]

        current_value += curr_value

print(current_value)

input_file.close()
