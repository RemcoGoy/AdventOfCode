def main():
    f = open("input.txt")
    content = f.readlines()
    
    matrix = []
    for line in content:
        submatrix = []
        for x in line.strip():
            submatrix.append(int(x))
        matrix.append(submatrix)
    
    lowest = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            curr_count = matrix[i][j]
            
            up = matrix[i - 1][j] if i - 1 >= 0 else None
            down = matrix[i + 1][j] if i + 1 < len(matrix) else None
            left = matrix[i][j - 1] if j - 1 >= 0 else None
            right = matrix[i][j + 1] if j + 1 < len(matrix[0]) else None
            
            if (up is None or curr_count < up) and (down is None or curr_count < down) and (right is None or curr_count < right) and (left is None or curr_count < left):
                lowest.append({"x": i, "y": j})
    
    count = 0
    for low in lowest:
        curr = matrix[low["x"]][low["y"]] + 1
        count += curr
    
    print(count)
    # pretty(matrix)
    f.close()

def pretty(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = ' '.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))

if __name__ == '__main__':
    main()