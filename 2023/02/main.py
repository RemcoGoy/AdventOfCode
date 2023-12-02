import numpy

input_file = open("./input.txt", "r")

max_config = {"red": 12, "green": 13, "blue": 14}

valid_games_count = 0

sets_power = 0


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

    curr_needed_dict = {"red": -1, "green": -1, "blue": -1}

    for s in sets:
        # Part 1
        # valid_game = valid_set(s) and valid_game

        # Part 2
        pulls = s.strip().split(",")
        for pull in pulls:
            pull = pull.strip()
            split_pull = pull.split(" ")
            amount = int(split_pull[0])
            color = split_pull[1]

            curr_needed = curr_needed_dict[color]

            if curr_needed == -1 or amount > curr_needed:
                curr_needed_dict[color] = amount

    sets_power += numpy.prod(list(curr_needed_dict.values()))

    # Part 1
    # if valid_game:
    #     valid_games_count += game_index

print("-----------------------------------")
# Part 1
# print(valid_games_count)
print(sets_power)

input_file.close()
