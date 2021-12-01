def main():
    f = open("input.txt")
    prev_window = None
    count = 0
    content = f.readlines()
    for i, line in enumerate(content):
        if i < len(content) - 2:
            n = int(line) + int(content[i+1]) + int(content[i+2]) 
            print(prev_window, n)
            if prev_window is not None and prev_window < n:
                count += 1

            prev_window = n
        else:
            break
    f.close()
    print(count)

if __name__ == '__main__':
    main()