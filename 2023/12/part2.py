import functools

input_file = open("./input.txt", "r")
data = input_file.read()

solution = 0


@functools.cache
def find_match(pattern, size, groups):
    if len(groups) == 0:
        if all(c in ".?" for c in pattern):
            return 1
        return 0

    curr = groups[0]
    rest = groups[1:]
    after = sum(rest) + len(rest)

    count = 0

    for before in range(size - after - curr + 1):
        opt = "." * before + "#" * curr + "."
        if all(c0 == c1 or c0 == "?" for c0, c1 in zip(pattern, opt)):
            count += find_match(pattern[len(opt) :], size - curr - before - 1, rest)

    return count


for line in data.splitlines():
    springs, groups = line.split(" ")
    springs = "?".join((springs,) * 5)
    groups = tuple([int(x) for x in groups.split(",")]) * 5
    solution += find_match(springs, len(springs), groups)

print(solution)

input_file.close()
