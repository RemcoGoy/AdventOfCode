def main():
    f = open("input.txt")
    content = f.readlines()
    
    initial = content[0].split(",")
    days = 256
    state = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for i in initial:
        state[int(i)] += 1
    
    for day in range(days):
        check_zeros(state)
        update_zeros(state)
        lower_days(state)
        # print(day, state)
    
    print(count_fish(state))
    f.close()

def count_fish(state):
    sum = 0
    for i in state:
        sum += state[i]
    
    return sum
    

def lower_days(state):
    copy = state.copy()
    for i in range(10):
        state[i] = copy.get(i + 1, 0)
        
    # return [ int(x) - 1 for x in state ]

def check_zeros(state):
    # zeros = len([x for x in state if x == 0])
    zeros = state[0]
    # state.extend([9 for _ in range(zeros)])
    state[9] += zeros

def update_zeros(state):
    zeros = state[0]
    state[7] += zeros
    state[0] = 0
    # return [ 6 if x < 0 else x for x in state]

if __name__ == "__main__":
    main()