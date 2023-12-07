from icecream import ic

file = open("day5_data.txt")
data = file.read().strip().split("\n\n")
file.close()

seeds = {i: [i] for i in data[0].split(" ")[1:]}

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


def find_next_step(seed: int, map):
    for line in map:
        line = line.split(" ")
        destination_start = int(line[0])
        source_start = int(line[1])
        step = int(line[2])
        if source_start <= seed < (source_start + step):
            return str(destination_start + seed - source_start)
    return str(seed)


for seed, steps in seeds.items():
    for map in maps:
        seeds[seed].append(find_next_step(int(steps[-1]), map))


lowest_loc = sorted([int(i[-1]) for i in seeds.values()])[0]
ic(lowest_loc)
