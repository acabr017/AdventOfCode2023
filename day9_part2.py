from icecream import ic
from sympy.polys.polyfuncs import interpolate

file = open("day9_data.txt")
data = file.read().split("\n")
file.close()

sum = 0
for line in data:
    data_points = [int(i) for i in line.split(" ")]
    next_x = 0
    next_digit = interpolate(data_points, next_x)
    sum += next_digit
    ic(next_digit)

ic(sum)
