input_file = open("input.txt", "r")

curr_val = 0

digit_strings = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

for line in input_file.readlines():
    print(f"Current line: {line}")
    line_val = 0
    
    first_value = None
    first_index = -1
    
    for digit in digit_strings.keys():
        res = line.find(digit)
        if not res == -1:
            if first_index == -1 or res < first_index:
                first_value = digit_strings[digit]
                first_index = res
    
    
    for i in range(0, first_index if not first_index == -1 else len(line) - 1):
        x_num = line[i]
        if x_num.isdigit():
            first_value = int(x_num)
            break
    
    rev_line = line[::-1]
    
    last_value = None
    last_index = -1
    
    for digit in digit_strings.keys():
        rev_digit = digit[::-1]
        res = rev_line.find(rev_digit)
        if not res == -1:
            if last_index == -1 or res < last_index:
                last_value = digit_strings[digit]
                last_index = res
               
    for i in range(len(line) - 1, len(line) - last_index - 1 if not last_index == -1 else 0, -1):
        y_num = line[i]
        if y_num.isdigit():
            last_value = int(y_num)
            break
    
    line_val += first_value * 10
    
    if last_value == None:
        line_val += first_value
    else:
        line_val += last_value
    # Part #1
    # num = ""
    # for x in line:
    #     if x.isdigit():
    #        num += x
    #        break
           
    # for y in range(len(line), 0, -1):
    #     y_num = line[y - 1]
    #     if y_num.isdigit():
    #         num += y_num
    #         break
        
    # curr_val += int(num)
    print(line_val)
    curr_val += line_val

print('--------------')
print(curr_val)
input_file.close()