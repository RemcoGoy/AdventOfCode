input_file = open("./input.txt", "r")

lines = []
for line in input_file.readlines():
    lines.append([int(x) for x in line.split(" ")])

input_file.close()

safe_lines = 0

for line in lines:
    line_safe = True
    prev_x = line[0]
    inc_line = line[0] < line[1]

    for x in line[1:]:
        diff = abs(prev_x - x)
        
        if inc_line and prev_x > x:
            print(f"{line} not increasing when it should")
            line_safe = False
            break

        if not inc_line and prev_x < x:
            print(f"{line} not decreasing when it should")
            line_safe = False
            break
            
        if not diff in [1,2,3]:
            print(f"{line} diff to big")
            line_safe = False
            break
            
        prev_x = x

    if line_safe:
        safe_lines += 1

print(safe_lines)