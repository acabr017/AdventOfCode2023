data = "day3_data.txt"
master_symbols = ["-", "=", "%", "*", "#", "$", "&", "@", "/", "+"]
tracker = []


def element_finder(line):
    numbers = {}
    symbols = {}
    coords = []
    current_number = ""
    for i, char in enumerate(line.strip()):
        if char.isdigit():
            current_number += char
            coords.append(i)
            if i == len(line.strip()) - 1:
                try:
                    numbers[current_number].append(coords)
                except KeyError:
                    numbers[current_number] = []
                    numbers[current_number].append(coords)
        elif char.isdigit() is False and len(current_number) != 0:
            try:
                numbers[current_number].append(coords)
            except KeyError:
                numbers[current_number] = []
                numbers[current_number].append(coords)
            current_number = ""
            coords = []
        if char in master_symbols:
            try:
                symbols[char].append(i)
            except KeyError:
                symbols[char] = [i]

    return numbers, symbols


def check(line_dict, pos):
    valid = []
    for key, value in line_dict.items():
        for n in value:
            # print(n)
            if (
                abs(n[0] - pos) <= 1
            ):  # the closest number to the symbol is the leading number
                # -> i.e, the number is to the right of the symbol
                valid.append(key)
            elif (
                abs(n[-1] - pos) <= 1
            ):  # the closest number to the symbol is the last number
                # -> i.e the number is to the left of the symbol
                valid.append(key)

    return valid


file = open(data)
prompt = file.read().splitlines()
length_of_file = len(prompt)
file.close()
total_nums_data = {}
total_sym_data = {}
for i, line in enumerate(prompt):
    nums, syms = element_finder(line)
    if nums:
        total_nums_data[i] = nums
    if syms:
        total_sym_data[i] = syms

for level, sym_dict in total_sym_data.items():
    for value in sym_dict.values():
        for spot in value:
            try:
                tracker += check(total_nums_data[level - 1], spot)

            except KeyError:
                print("No numbers above this line.")
            try:
                tracker += check(total_nums_data[level], spot)
            except KeyError:
                print("No numbers on this line.")
            try:
                tracker += check(total_nums_data[level + 1], spot)
            except KeyError:
                print("No numbers below this line. ")

sum = 0
for n in tracker:
    sum += int(n)

print(sum)
