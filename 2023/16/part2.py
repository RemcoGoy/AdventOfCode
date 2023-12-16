P = complex

input_file = open("./input.txt", "r")
data = input_file.read()


def print_grid(grid, w, h, empty=" "):
    for y in range(h):
        for x in range(w):
            print(grid.get(P(x, y), empty), end="")
        print()


def walk_path(grid, start=(-1, 1)):
    to_step, seen = [start], set()
    while to_step:
        p, d = to_step.pop()
        if (p, d) in seen:
            continue
        seen.add((p, d))
        if p + d not in grid:
            continue

        if grid[p + d] == "|" and d.real:
            to_step.extend([(p + d, -1j), (p + d, 1j)])
        elif grid[p + d] == "-" and d.imag:
            to_step.extend([(p + d, -1), (p + d, 1)])
        elif grid[p + d] == "/":
            to_step.append((p + d, -d.imag - 1j * d.real))
        elif grid[p + d] == "\\":
            to_step.append((p + d, d.imag + 1j * d.real))
        else:
            to_step.append((p + d, d))

    return len(set(p for p, _ in seen)) - 1


grid = {}
for y, l in enumerate(data.splitlines()):
    for x, v in enumerate(l):
        grid[P(x, y)] = v

mx, my, best = max(int(x.real) for x in grid), max(int(p.imag) for p in grid), 0
for x in range(mx + 1):
    best = max(best, walk_path(grid, (x - 1j, 1j)))
    best = max(best, walk_path(grid, (x + 1j * (my + 1), -1j)))

for y in range(my + 1):
    best = max(best, walk_path(grid, (-1 + 1j * y, 1)))
    best = max(best, walk_path(grid, (mx + (1j * my + 1), -1)))

print(best)

input_file.close()
