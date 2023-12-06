sum = 0

data = "day4_data.txt"


def winner_checker(values, winners):
    return list(set(winners) & set(values))


with open(data) as file:
    for line in file:
        _, game_data = line.split(": ")
        winners, trials = game_data.split("|")
        trials = [i for i in trials.strip().split(" ") if i]
        winners = [i for i in winners.strip().split(" ")ers if i]
        matches = winner_checker(trials, winners)
        points = int((0.5) * pow(2, (len(winner_checker(trials, winners)))))
        sum += points


print(sum)
