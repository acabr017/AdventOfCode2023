# Let's learn some regex stuff. I'll try to solve this day using RegEx

import re
from icecream import ic

max_red = 12
max_green = 13
max_blue = 14
sum = 0
with open("day2_data.txt") as file:
    for line in file:
        game_id = re.findall("^Game \d", line)[0].split(" ")[1]
        output = re.findall("\d+ [red|blue|green]*", line)
        reds = re.findall("\d+ red", " ".join(output))
        largest_red = max([int(i) for i in re.findall("\d+", " ".join(reds))])
        blues = re.findall("\d+ blue", " ".join(output))
        largest_blue = max([int(i) for i in re.findall("\d+", " ".join(blues))])
        green = re.findall("\d+ green", " ".join(output))
        largest_green = max([int(i) for i in re.findall("\d+", " ".join(blues))])

        if (
            largest_red <= max_red
            and largest_green <= max_green
            and largest_blue <= max_blue
        ):
            sum += int(game_id)

print(sum)
