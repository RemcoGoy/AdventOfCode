input_file = open("./input.txt", "r")

lines = input_file.read()

lines = lines.split("\n\n")

seeds = [int(seed) for seed in lines.pop(0).split(":")[1].split(" ") if not seed == ""]

seed_map = {k: k for k in seeds}

for step in lines:
    sub_lines = step.split("\n")
    info = sub_lines.pop(0)
    # print(info)
    seen_seeds = []

    ranges = []

    for sub in sub_lines:
        s = [int(x) for x in sub.split(" ")]
        dest_range = range(s[0], s[0] + s[2])
        source_range = range(s[1], s[1] + s[2])

        for seed, seed_index in seed_map.items():
            if seed not in seen_seeds:
                if seed_index in source_range:
                    diff = seed_index - source_range.start

                    new_index = dest_range.start + diff
                    # print(f"Move seed {seed} to index {new_index}")
                    seed_map[seed] = new_index
                    seen_seeds.append(seed)

# print(seed_map)
print(min(seed_map.values()))

input_file.close()
