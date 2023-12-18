from PIL import Image, ImageDraw

input_file = open("./input.txt", "r")
data = input_file.read()

P = complex


def print_grid(grid, w, h, empty=" "):
    for y in range(h):
        for x in range(w):
            print(grid.get(P(x, y), empty), end="")
        print()


grid = {}

curr_index = P(0, 0)

dir_map = {0: "R", 1: "D", 2: "L", 3: "U"}

for line in data.splitlines():
    _, _, x = line.split(" ")

    x = [c for c in x]
    x = x[2:-1]

    d = dir_map[int(x.pop(-1))]
    l = int("".join(x), 16)

    dir = None
    l = int(l)

    if d == "R":
        dir = 1
    elif d == "L":
        dir = -1
    elif d == "U":
        dir = -1j
    elif d == "D":
        dir = 1j

    for _ in range(l):
        curr_index += dir
        grid[curr_index] = "#"

x_coordinates = [int(point.real) for point in grid.keys()]
y_coordinates = [int(point.imag) for point in grid.keys()]

width = max(x_coordinates) - min(x_coordinates)
height = max(y_coordinates) - min(y_coordinates)


im = Image.new(mode="RGB", size=(width + 1, height + 1), color=(0, 0, 0))
for x, y in zip(x_coordinates, y_coordinates):
    im.putpixel(xy=(x, y), value=(255, 255, 255))

ImageDraw.floodfill(im, (1, 1), value=(255, 255, 255))
# ImageDraw.floodfill(im, (10, height), value=(255, 255, 255))
# ImageDraw.floodfill(im, (200, height), value=(255, 255, 255))
im.save("test.png")

area = 0
for pixel in im.getdata():
    if pixel == (255, 255, 255):
        area += 1

print(area)

input_file.close()
