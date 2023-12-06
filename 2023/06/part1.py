input_file = open("./input.txt", "r")

lines = input_file.readlines()
times = [int(x) for x in lines[0].split(":")[1].strip().split(" ") if not x == ""]
distances = [int(x) for x in lines[1].split(":")[1].strip().split(" ") if not x == ""]

total = 1

for i, time in enumerate(times):
    wins = 0
    curr_record = distances[i]
    
    for j in range(1, time):
        holding = j
        going = time - holding
        distance = holding * going
        
        if distance > curr_record:
            wins += 1
    
    total *= wins
    
print(total)
input_file.close()