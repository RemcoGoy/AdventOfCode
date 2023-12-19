import json

input_file = open("./input.txt", "r")
data = input_file.read()

workflow, ratings = data.split("\n\n")

worksflow = workflow.splitlines()
ratings = ratings.splitlines()

workflows = {}


def check_rule(rule, input):
    for i, r in enumerate(rule):
        to_check = None
        if i == len(rule) - 1:
            return r

        compare, then = r.split(":")
        c = compare[0]
        x = compare[1]
        n = int(compare[2:])

        to_compare = input[c]
        if x == "<":
            if to_compare < n:
                to_check = then
        elif x == ">":
            if to_compare > n:
                to_check = then

        if to_check:
            return to_check

    return None


accepted = []
rejected = []

for line in worksflow:
    name, rules = line.split("{")
    rules = rules.replace("}", "")
    rules = rules.split(",")

    workflows[name] = rules

for i, rating in enumerate(ratings):
    rating = (
        rating.replace("=", ":")
        .replace("a", '"a"')
        .replace("x", '"x"')
        .replace("m", '"m"')
        .replace("s", '"s"')
    )
    rating = json.loads(rating)
    to_check = "in"
    while to_check:
        n = check_rule(workflows[to_check], rating)

        if n == "A":
            accepted.append(rating)
            break

        if n == "R":
            rejected.append(rating)
            break

        to_check = n

result = 0

for acc in accepted:
    result += sum(acc.values())

print(result)
input_file.close()
