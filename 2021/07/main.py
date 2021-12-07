import itertools as it

def main():
    f = open("input.txt")
    content = f.readlines()
    
    positions = [ int(x) for x in content[0].split(',') ]
    max_pos = max(positions)
    
    min_fuel = None
    min_fuel_index = None
    for i in range(max_pos):
        fuel = 0
        for pos in positions:
            steps = abs(pos - i)
            curr_fuel = list(it.accumulate(range(steps + 1)))
            fuel += curr_fuel[-1] if len(curr_fuel) > 0 else 0
        
        if min_fuel is None and min_fuel_index is None:
            min_fuel = fuel
            min_fuel_index = i
        else:
            if min_fuel > fuel:
                min_fuel = fuel
                min_fuel_index = i

    print(min_fuel)
    f.close()

if __name__ == "__main__":
    main()