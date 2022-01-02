from collections import Counter

def main():
    f = open("sample_input.txt")
    content = f.readlines()
    
    number_len = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    empty = { 
        "top": set(),
        "right_top": set(),
        "left_top": set(),
        "middle": set(),
        "right_bottom": set(),
        "left_bottom": set(),
        "bottom": set()
    }
        
    for line in content:
        chart = empty.copy()
        output = line.split("|")
        signal = output[0].strip()
        for n in signal.split(" "):
            pos_numbers = [ i for i, v in enumerate(number_len) if v == len(n) ]
            if len(pos_numbers) == 1:
                number = pos_numbers[0]
                if number == 8:
                    continue
                else:
                    if number == 1:
                        chart["right_top"].update(n)
                        chart["right_bottom"].update(n)
                    elif number == 7:
                        if len(chart['right_top']) > 0 and len(chart['right_bottom']) > 0:
                            chart["top"].update(n)
                        else:
                            chart["right_top"].update(n)
                            chart["right_bottom"].update(n)
                            chart["top"].update(n)
            else:
                print(pos_numbers)
            
            print(chart)
        
        output = output[1].strip()
        for n in output.split(" "):
            pos_numbers = [ i for i, v in enumerate(number_len) if v == len(n) ]
            print(pos_numbers)
        
        break
                
    f.close()

def main2():
    with open("sample_input.txt") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

        def unionOfStrings(str1, str2):
            return len(set(str1 + str2))

        def differenceOfStrings(str1, str2):
            return len(set(str1) - set(str2))

        def sortString(str):
            return "".join(sorted(str))

        def sortArrayOfStrings(arr):
            return [sortString(item) for item in arr]

        def ArrayToInt(arr):
            return int("".join([str(item) for item in arr]))

        sum = 0

        for line in lines:
            signals, output = [sortArrayOfStrings(item.split()) for item in line.split(" | ")]
            mappings = {}
            inverse_mappings = [''] * 10
            lenMap = {2: 1, 3: 7, 4: 4, 7: 8}

            for segment in signals:
                seglen = len(segment)
                if seglen not in lenMap:
                    continue
                mappings[segment] = lenMap[seglen]
                inverse_mappings[lenMap[seglen]] = segment

            for segment in signals:
                if len(segment) == 6:
                    sub7 = differenceOfStrings(segment, inverse_mappings[7])
                    sub4 = differenceOfStrings(segment, inverse_mappings[4])

                    if sub7 == 4:
                        mappings[segment] = 6
                    elif sub7 == 3 and sub4 == 2:
                        mappings[segment] = 9
                    else:
                        mappings[segment] = 0

                elif len(segment) == 5:
                    add4 = unionOfStrings(segment, inverse_mappings[4])
                    add7 = unionOfStrings(segment, inverse_mappings[7])

                    if add4 == 7:
                        mappings[segment] = 2
                    elif add4 == 6 and add7 == 6:
                        mappings[segment] = 5
                    else:
                        mappings[segment] = 3

            sum += ArrayToInt([mappings[x] for x in output])

        print(sum)

if __name__ == "__main__":
    main2()