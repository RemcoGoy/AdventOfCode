import itertools

def main():
    f = open("input.txt")
    content = f.readlines()
    
    coords = get_coords(content)
    diagram = draw_empty(coords)
    
    for coord in coords:
        if coord["start"]["x"] == coord["end"]["x"]:
            # y movement
            x = coord['start']['x']
            if coord['start']['y'] < coord['end']['y']:
                y_range = range(coord['start']['y'], coord['end']['y'] + 1)
            else:
                y_range = range(coord['end']['y'], coord['start']['y'] + 1)
            
            for y in y_range:
                diagram[y][x] += 1
        elif coord["start"]["y"] == coord["end"]["y"]:
            # x movement
            y = coord['start']['y']
            if coord['start']['x'] < coord['end']['x']:
                x_range = range(coord['start']['x'], coord['end']['x'] + 1)
            else:
                x_range = range(coord['end']['x'], coord['start']['x'] + 1)
            
            for x in x_range:
                diagram[y][x] += 1
        else:
            if coord['start']['x'] < coord['end']['x']:
                x_range = range(coord['start']['x'], coord['end']['x'] + 1)
            else:
                x_range = range(coord['end']['x'], coord['start']['x'] + 1)[::-1]
                
            if coord['start']['y'] < coord['end']['y']:
                y_range = range(coord['start']['y'], coord['end']['y'] + 1)
            else:
                y_range = range(coord['end']['y'], coord['start']['y'] + 1)[::-1]
            
            assert len(y_range) == len(x_range)
            for i, x in enumerate(x_range):
                y = y_range[i]
                diagram[y][x] += 1
    
    pretty_2d(diagram)
    points = len(filter(lambda x: x >= 2, list(itertools.chain(*diagram))))
    print(points)
    f.close()

def draw_empty(coords):
    max_x = max(list(itertools.chain(*map(lambda coord: [int(coord["start"]["x"]), int(coord["end"]["x"])], coords))))
    max_y = max(list(itertools.chain(*map(lambda coord: [int(coord["start"]["y"]), int(coord["end"]["y"])], coords))))
    diagram = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    
    return diagram
    

def get_coords(lines):
    coords = []
    for line in lines:
        split = line.split("->")
        start = split[0].strip()
        end = split[1].strip()
        
        start_split = start.split(',')
        x1 = start_split[0]
        y1 = start_split[1]
        
        end_split = end.split(',')
        x2 = end_split[0]
        y2 = end_split[1]
        
        coords.append({"start": {"x": int(x1), "y": int(y1)}, "end": {"x": int(x2), "y": int(y2)}})
    
    new_coords = []
    for c in coords:
        if c['start']['x'] == c['end']['x'] or c['start']['y'] == c['end']['y']:
            new_coords.append(c)
        elif abs(c['start']['x'] - c['end']['x']) == abs(c['start']['y'] - c['end']['y']):
            new_coords.append(c)
    coords = filter(lambda c: c['start']['x'] == c['end']['x'] or c['start']['y'] == c['end']['y'] or abs(c['start']['x'] - c['end']['x']) == abs(c['start']['y'] - c['end']['y']), coords)
    return coords

def pretty_2d(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = ' '.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))

if __name__ == "__main__":
    main()