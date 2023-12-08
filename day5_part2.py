from icecream import ic


def find_dst(number, map):
    for line in map:
        start_of_shift = int(line.split(" ")[0])
        start_of_start = int(line.split(" ")[1])
        step = int(line.split(" ")[2])
        src_range = range(start_of_start, start_of_start + step)
        if number in src_range:
            dst_range = range(start_of_shift, start_of_shift + step)
            return dst_range[src_range.index(number)]
    return number


file = open("day5_data.txt")
data = file.read().strip().split("\n\n")
file.close()

seeds = data[0].strip().split(" ")[1:]
seed_start = [seeds[i] for i in range(0, len(seeds), 2)]
seed_step = [seeds[i] for i in range(1, len(seeds), 2)]
seed_ranges = {}
for i, val in enumerate(seed_start):
    seed_ranges[i] = range(int(seed_start[i]), int(seed_start[i]) + int(seed_step[i]))


seed_to_soil_map = sorted(data[1].split("\n")[1:])
soil_to_fert_map = sorted(data[2].split("\n")[1:])
fert_to_water_map = sorted(data[3].split("\n")[1:])
water_to_light_map = sorted(data[4].split("\n")[1:])
light_to_temp_map = sorted(data[5].split("\n")[1:])
temp_to_humidity_map = sorted(data[6].split("\n")[1:])
humidity_to_loc_map = sorted(data[7].split("\n")[1:])

maps = [
    seed_to_soil_map,
    soil_to_fert_map,
    fert_to_water_map,
    water_to_light_map,
    light_to_temp_map,
    temp_to_humidity_map,
    humidity_to_loc_map,
]

locations = {}
lowest = 0
for seed_range in seed_ranges.values():
    for seed in seed_range:
        soil_loc = find_dst(seed, seed_to_soil_map)
        fert_loc = find_dst(soil_loc, soil_to_fert_map)
        water_loc = find_dst(fert_loc, fert_to_water_map)
        light_loc = find_dst(water_loc, water_to_light_map)
        temp_loc = find_dst(light_loc, light_to_temp_map)
        humidity_loc = find_dst(temp_loc, temp_to_humidity_map)
        loc = find_dst(humidity_loc, humidity_to_loc_map)
        if lowest == 0:
            lowest = loc
        elif loc < lowest:
            lowest = loc


ic(lowest)
