input_file = open("./input.txt", "r")

grid = input_file.read().split("\n")

input_file.close()

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def get_whole_plot(plant, pos, grid, found):
    global limits

    x, y = pos
    for dir in dirs:
        dx, dy = dir
        new_x = x + dx
        new_y = y + dy

        if (new_x, new_y) not in found:
            if all(p in lim for p, lim in zip([new_x, new_y], limits)):
                if grid[new_y][new_x] == plant:
                    new_pos = (new_x, new_y)
                    found.add(new_pos)
                    found.update(get_whole_plot(plant, new_pos, grid, found))
    return found


max_x = len(grid[0])
max_y = len(grid)

lim = [range(max_x), range(max_y)]
visited = set()
plot_number = 0
grid_identified = {}

for y in lim[1]:
    for x in lim[0]:
        start = (x, y)
        if start not in visited:
            plant = grid[y][x]
            found = set()
            found.add(start)
            found = get_whole_plot(plant, (x, y), grid, found)
            grid_identified[start] = found
            visited.update(found)

areas_perimeters = []
for start, plot_coords in grid_identified.items():
    num_fences = 0
    for pos in plot_coords:
        x, y = pos
        for direction in dirs:
            dx, dy = direction
            new_x = x + dx
            new_y = y + dy
            if (new_x, new_y) not in plot_coords or any(
                p not in lim for p, lim in zip([new_x, new_y], lim)
            ):
                num_fences += 1

    areas_perimeters.append((len(plot_coords), num_fences))

result = sum(a * p for a, p in areas_perimeters)
print(result)
