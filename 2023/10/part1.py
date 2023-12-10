input_file = open("./input.txt", "r")

data = input_file.read()

P = complex


def change_dir(d, pipe):
    if (
        (pipe == "7" and d == 1)  # ->
        or (pipe == "J" and d == 1j)  # v
        or (pipe == "L" and d == -1)  # <-
        or (pipe == "F" and d == -1j)  # ^
    ):
        return d * 1j  # Rotate 90 right

    if (
        (pipe == "7" and d == -1j)  # ^
        or (pipe == "J" and d == 1)  # ->
        or (pipe == "L" and d == 1j)  # v
        or (pipe == "F" and d == -1)  # <-
    ):
        return d * -1j  # Rotate 90 left

    if pipe in "-|":
        return d

    return None


def clean_grid(grid, start):
    return (
        get_path(grid, start, 1)
        or get_path(grid, start, -1)
        or get_path(grid, start, 1j)
        or get_path(grid, start, -1j)
    )


def get_path(grid, start, d):
    path = {}
    pos = start
    while pos in grid:
        path[pos] = grid[pos]
        pos += d
        if pos not in grid:
            return None

        if pos == start:
            return path

        d = change_dir(d, grid[pos])
        if d == None:
            return None


def print_grid(grid, w, h, empty=" "):
    for y in range(h):
        for x in range(w):
            print(grid.get(P(x, y), empty), end="")
        print()


grid = {}
start = None

for y, l in enumerate(data.splitlines()):
    for x, v in enumerate(l):
        if v != ".":
            grid[P(x, y)] = v
            if v == "S":
                start = P(x, y)

grid = clean_grid(grid, start)
print(len(grid) // 2)

input_file.close()
