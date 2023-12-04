input_file = open("./input.txt", "r")

lines = input_file.readlines()

total_cards = len(lines)

card_copies = {}

for card in lines:
    s = card.split(":")
    card_index = int(s[0].split(" ")[-1])
    numbers = s[1].split("|")
    winning = numbers[0].strip().split(" ")
    scratched = [x for x in numbers[1].strip().split(" ") if not x == ""]

    card_score = 0

    for x in scratched:
        if x in winning:
            card_score += 1

    copies = 0
    if card_index in card_copies:
        copies = card_copies[card_index]

    for _ in range(1 + copies):
        for i in range(1, card_score + 1):
            copy_index = i + card_index
            if copy_index in card_copies:
                card_copies[copy_index] += 1
            else:
                card_copies[copy_index] = 1

            total_cards += 1

print(total_cards)
input_file.close()
