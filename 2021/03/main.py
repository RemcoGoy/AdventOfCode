def main():
    f = open("input.txt")
    content = f.readlines()
    
    counts = []
    
    # Part 1
    # for line in content:
    #     for i, char in enumerate(line):
    #         if len(counts) <= i:
    #             counts.append(0)
    #         if char == "0":
    #             counts[i] -= 1
    #         elif char == "1":
    #             counts[i] += 1

    # counts = counts[:-1]
    # gamma_counts = map(lambda x: "1" if x > 0 else "0", counts)
    # eps_counts = map(lambda x: "0" if x > 0 else "1", counts)
    # gamma_rate = int("".join(gamma_counts), 2)
    # eps_rate = int("".join(eps_counts), 2)
    # print(gamma_rate * eps_rate)
    
    # Part 2
    lines_to_search_most = content
    for i in range(len(content[0])):
        zeros = 0
        ones = 0
        for line in lines_to_search_most:
            c = line[i]
            if c == '0':
                zeros += 1
            elif c == '1':
                ones += 1
        
        to_filter_most = '1' if ones >= zeros else '0'
        # to_filter_least = '1' if zeros > ones else '0'
        
        if (len(lines_to_search_most) == 1):
            break
        lines_to_search_most = filter(lambda x: x[i] == to_filter_most, lines_to_search_most)
        
    lines_to_search_least = content
    for i in range(len(content[0])):
        zeros = 0
        ones = 0
        for line in lines_to_search_least:
            c = line[i]
            if c == '0':
                zeros += 1
            elif c == '1':
                ones += 1
        
        to_filter_least = '1' if zeros > ones else '0'
        
        if (len(lines_to_search_least) == 1):
            break
        lines_to_search_least = filter(lambda x: x[i] == to_filter_least, lines_to_search_least)

    most = int("".join(lines_to_search_most[0]), 2)
    least = int("".join(lines_to_search_least[0]), 2)
    
    print(least * most)
    f.close()
    
if __name__ == "__main__":
    main()