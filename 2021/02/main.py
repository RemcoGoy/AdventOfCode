def main():
    f = open("input.txt")
    content = f.readlines()
    
    depth = 0
    horizontal = 0
    aim = 0
    
    for line in content:
        commands = line.split(" ")
        command = commands[0]
        amount = commands[1]
        
        if command == 'forward':
            horizontal += int(amount)
            depth += (aim * int(amount))
        
        if command == 'up':
            aim -= int(amount)
            
        if command == 'down':
            aim += int(amount)
    
    print(depth * horizontal)
    f.close()
    
if __name__ == "__main__":
    main()