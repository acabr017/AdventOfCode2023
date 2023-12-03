limits = {"red": 12, "green": 13, "blue": 14}
power_sum = 0
data = "day2_example_data.txt"

with open(data) as file:
    for line in file:
        valid = True
        info = {"red": 0, "green": 0, "blue": 0}
        game_id = int(line.split(":")[0].split(" ")[1])
        values = line.split(":")[1].strip().split(";")
        for trial in values:
            sets = trial.split(",")
            for set in sets:
                number, colour = set.strip().split(" ")
                if info[colour] < int(number):
                    info[colour] = int(number)
        power_sum += info["red"]*info["green"]*info["blue"]

    print(power_sum)
