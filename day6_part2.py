from icecream import ic
import re
from math import sqrt, ceil

rate = 1  # mm/ms


file = open("day6_data.txt")
data = file.read().split("\n")
file.close()

time = "".join(re.findall("\d+", data[0]))
distance = "".join(re.findall("\d+", data[1]))
races = {int(time): int(distance)}
ic(races)

total_solutions = 1
for total_time, distance in races.items():
    solutions = 0
    radicand = sqrt(pow(rate * total_time, 2) - (4 * rate * distance))
    charge_time_plus = ceil((rate * total_time + radicand) / (2 * rate))
    charge_time_minus = ceil((rate * total_time - radicand) / (2 * rate))
    interval_to_check = range(charge_time_minus, charge_time_plus)
    first_distance = rate * (
        (interval_to_check[0] * total_time) - (pow(interval_to_check[0], 2))
    )
    last_distance = rate * (
        (interval_to_check[-1] * total_time) - (pow(interval_to_check[-1], 2))
    )
    if first_distance > distance and last_distance > distance:
        total_solutions *= len(interval_to_check)
    elif (first_distance < distance and last_distance >= distance) or (
        first_distance >= distance and last_distance < distance
    ):
        total_solutions *= len(interval_to_check) - 1
    elif first_distance <= distance and last_distance <= distance:
        total_solutions *= len(interval_to_check) - 2

ic(total_solutions)
