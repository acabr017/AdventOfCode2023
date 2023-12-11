from icecream import ic


file = open("day10_data.txt")
data = file.read().split("\n")
file.close()

data_array = []
for line in data:
    data_array.append([char for char in line])


def find_S(data_array):
    for y, line in enumerate(data_array):
        for x, char in enumerate(line):
            if char == "S":
                return x, y


# directions = {
#     "|":,
#     "-":[1,0],
#     "L":[]
# }

S_x, S_y = find_S(data_array)
ic(S_x, S_y)

try:
    # look above:
    above = data_array[S_y - 1][S_x]
except IndexError:
    print("Nothing above")
    above = None

try:
    # look below:
    below = data_array[S_y + 1][S_x]
except IndexError:
    print("Nothing below")
    below = None

try:
    # look to the right:
    right = data_array[S_y][S_x + 1]
except IndexError:
    print("Nothing to the right")
    right = None

try:
    # look to the left
    left = data_array[S_y][S_x - 1]
except IndexError:
    print("Nothing to the left")
    left = None


ic(above, below, left, right)
