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
    print(line_dict)
    valid = []
    # going through each number and their coordinates
    for key, value in line_dict.items():
        # print(value)
        # going through each instance of the number.
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


def _grab_data(filename):
    file = open(filename)
    prompt = file.read().splitlines()
    file.close()
    return prompt


data = "day3_data.txt"
master_symbols = ["*"]

prompt = _grab_data(data)
length_of_file = len(prompt)
total_nums_data = {}
total_sym_data = {}
tracker = []
sum = 0

for i, line in enumerate(prompt):
    nums, syms = element_finder(line)
    if nums:
        total_nums_data[i] = nums
    if syms:
        total_sym_data[i] = syms

print(total_nums_data)

for level, sym_dict in total_sym_data.items():
    print(sym_dict)
    print(level)
    for value in sym_dict.values():
        adjacents = 0
        for spot in value:
            try:
                valid_nums_above = check(total_nums_data[level - 1], spot)
                print(f"Above: {valid_nums_above}")
                if valid_nums_above:
                    adjacents += 1
                    tracker += valid_nums_above
            except KeyError:
                print("No numbers above this line.")
                valid_nums_above = []
            try:
                valid_nums_on_level = check(total_nums_data[level], spot)
                print(f"Level: {valid_nums_on_level}")
                if valid_nums_on_level:
                    adjacents += 1
                    tracker += valid_nums_on_level
            except KeyError:
                print("No numbers on this line.")
                valid_nums_on_level = []
            try:
                valid_nums_below = check(total_nums_data[level + 1], spot)
                print(f"Below: {valid_nums_below}")
                if valid_nums_below:
                    adjacents += 1
                    tracker += valid_nums_below
            except KeyError:
                print("No numbers below this line. ")
                valid_nums_below = []
            adj = valid_nums_above + valid_nums_on_level + valid_nums_below
            if len(adj) == 2:
                prod = 1
                for n in adj:
                    prod *= int(n)
                sum += prod
                print(
                    f"GEAR!. \n \n The Gear Ratio is {prod}. \n\n \
                          The new sum is {sum}"
                )


print(tracker)
# sum = 0
# for n in tracker:
#     sum += int(n)

# print(sum)
