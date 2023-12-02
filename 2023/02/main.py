input_file = open("./input.txt", "r")

max_config = {"red": 12, "green": 13, "blue": 14}

answer = 0


def valid_pull(pull):
    valid_pull = True

    pull = pull.strip()

    split_pull = pull.split(" ")
    amount = int(split_pull[0])
    color = split_pull[1]

    curr_max = max_config[color]

    if amount > curr_max:
        valid_pull = False

    return valid_pull


def valid_set(set):
    valid_set = True
    pulls = set.strip().split(",")

    for pull in pulls:
        valid_set = valid_pull(pull) and valid_set

    return valid_set


for game in input_file.readlines():
    valid_game = True

    split_line = game.split(":")
    game_index = int(split_line[0].split(" ")[-1])

    sets = split_line[1].split(";")

    for s in sets:
        valid_game = valid_set(s) and valid_game

    if valid_game:
        answer += game_index

print("-----------------------------------")
print(answer)

input_file.close()
