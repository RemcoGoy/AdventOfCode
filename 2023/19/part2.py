input_file = open("./input.txt", "r")

data = [s.splitlines() for s in input_file.read().split("\n\n")]

rules = {}
for l in data[0]:
    n, l = l.split("{")
    rules[n] = [p.split(":") for p in l[:-1].split(",")]


def count(l, h):
    x = max(h["x"] - l["x"], 0)
    m = max(h["m"] - l["m"], 0)
    a = max(h["a"] - l["a"], 0)
    s = max(h["s"] - l["s"], 0)
    return x * m * a * s


t = 0


def process(low, high, workflow):
    if workflow == "A":
        global t
        t += count(low, high)
        return

    if workflow == "R":
        return

    for i in rules[workflow]:
        if len(i) == 1:
            process(low, high, i[0])

        if "<" in i[0]:
            k, v = i[0].split("<")
            new_high = high.copy()
            new_high[k] = min(new_high[k], int(v))
            if count(low, new_high) > 0:
                process(low.copy(), new_high, i[1])
            low[k] = max(low[k], int(v))

        if ">" in i[0]:
            k, v = i[0].split(">")
            new_low = low.copy()
            new_low[k] = max(new_low[k], int(v) + 1)
            if count(new_low, high) > 0:
                process(new_low, high.copy(), i[1])
            high[k] = min(high[k], int(v) + 1)


process({"x": 1, "m": 1, "a": 1, "s": 1}, {"x": 4001, "m": 4001, "a": 4001, "s": 4001}, "in")
print(t)

input_file.close()
