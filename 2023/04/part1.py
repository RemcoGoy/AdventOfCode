input_file = open("./input.txt", "r")

total_score = 0

for card in input_file.readlines():
    numbers = card.split(":")[1].split("|")
    winning = numbers[0].strip().split(" ")
    scratched = [x for x in numbers[1].strip().split(" ") if not x == ""]
    
    card_score = 0
    
    for x in scratched:
        if x in winning:
            if card_score == 0:
                card_score = 1
            else:
                card_score *= 2
        
    total_score += card_score

print(total_score)

input_file.close()