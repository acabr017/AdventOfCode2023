from icecream import ic
import re

sum = 0

data = "day4_data.txt"


def winner_checker(values, winners):
    return list(set(winners) & set(values))


file = open(data)
file_data = file.readlines()
games = {str(i + 1): 1 for i in range(len(file_data))}
# ic(games)

for line in file_data:
    _, game_data = line.split(": ")
    winners, trials = game_data.split("|")
    game_num = re.findall("\d+", _)[0]
    trials = [i for i in trials.strip().split(" ") if i]
    winners = [i for i in winners.strip().split(" ") if i]

    matches = len(winner_checker(trials, winners))
    # ic(matches)
    # ic(game_num, games[game_num], games, range(games[game_num]))
    for i in range(0, games[game_num]):
        for n in range(matches):
            key = str(n + 1 + int(game_num))
            games[key] += 1
    # ic(games)

for val in games.values():
    sum += val

ic(sum)
