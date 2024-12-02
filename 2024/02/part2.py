input_file = open("./input.txt", "r")

lines: list[list] = []
for line in input_file.readlines():
    lines.append([int(x) for x in line.split(" ")])

input_file.close()

safe_lines = 0

def check_valid_line(line):
    line_safe = True
    prev_x = line[0]
    inc_line = line[0] < line[1]

    for x in line[1:]:
        diff = abs(prev_x - x)
        
        if inc_line and prev_x > x:
            line_safe = False
            break

        if not inc_line and prev_x < x:
            line_safe = False
            break
            
        if not diff in [1,2,3]:
            line_safe = False
            break
        
        prev_x = x
    
    return line_safe

for line in lines:
    if check_valid_line(line):
        safe_lines += 1
    else:
        for i in range(len(line)):
            line_copy = line.copy()
            line_copy.pop(i)
            valid_now = check_valid_line(line_copy)

            if valid_now:
                safe_lines += 1
                break

print(safe_lines)