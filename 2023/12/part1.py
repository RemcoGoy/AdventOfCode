import functools

input_file = open("./input.txt", "r")
data = input_file.read()

solution = 0


@functools.cache
def count_matches(pattern, size, splits):
    if len(splits) == 0:
        if all(c in ".?" for c in pattern):
            return 1
        return 0

    a = splits[0]
    rest = splits[1:]
    after = sum(rest) + len(rest)

    count = 0

    for before in range(size - after - a + 1):
        cand = "." * before + "#" * a + "."
        if all(c0 == c1 or c0 == "?" for c0, c1 in zip(pattern, cand)):
            count += count_matches(pattern[len(cand) :], size - a - before - 1, rest)

    return count


for line in data.splitlines():
    springs, groups = line.split(" ")
    groups = tuple([int(x) for x in groups.split(",")])
    solution += count_matches(springs, len(springs), groups)

print(solution)

input_file.close()
