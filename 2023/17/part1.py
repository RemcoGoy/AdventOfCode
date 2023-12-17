import heapq

import numpy as np

Right = (0, 1)
Down = (1, 0)
Left = (0, -1)
Up = (-1, 0)

input_file = open("./input.txt", "r")
data = input_file.read()

grid = np.array([[int(c) for c in x] for x in data.splitlines()])


def find_path(grid, min_dir, max_dir):
    visited = set()
    queue = [(0, 0, 0, Right, 1), (0, 0, 0, Down, 1)]

    while len(queue) > 0:
        cost, x, y, direction, count_direction = heapq.heappop(queue)

        # Check in visited
        if (x, y, direction, count_direction) in visited:
            continue
        else:
            visited.add((x, y, direction, count_direction))

        # Move direction
        new_x = x + direction[1]
        new_y = y + direction[0]

        # Check bounds
        if new_x < 0 or new_y < 0 or new_x >= len(grid[0]) or new_y >= len(grid):
            continue

        # Check value
        new_cost = cost + grid[new_y, new_x]

        # Check achieved
        if count_direction >= min_dir and count_direction <= max_dir:
            if new_x == len(grid[0]) - 1 and new_y == len(grid) - 1:
                return new_cost

        for d in [Right, Down, Left, Up]:
            # no reverse
            if d[0] + direction[0] == 0 and d[1] + direction[1] == 0:
                continue

            new_d_count = count_direction + 1 if d == direction else 1
            if (d != direction and count_direction < min_dir) or new_d_count > max_dir:
                continue

            heapq.heappush(queue, (new_cost, new_x, new_y, d, new_d_count))


print(find_path(grid, 1, 3))

input_file.close()
