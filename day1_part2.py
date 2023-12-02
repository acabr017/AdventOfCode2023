sum = 0
data = "day1_part2_example_data.txt"
nums_spelled_out = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
}
legit_options = {
    "o": [3, "ne"],
    "t": {"w": [3, "wo"], "h": [5, "hree"]},
    "f": {"o": [4, "our"], "i": [4, "ive"]},
    "s": {"i": [3, "ix"], "e": [5, "even"]},
    "e": [5, "ight"],
    "n": [4, "ine"],
    "z": [4, "ero"],
}

with open(data) as file:
    for line in file:
        line = line.strip()
        numbers = []
        current_spot = 0
        limit = len(line)
        while current_spot < limit:
            current_letter = line[current_spot]
            if current_letter in ["o", "e", "n", "z"]:
                try:
                    slice_to_check = line[
                        current_spot : current_spot + legit_options[current_letter][0]
                    ]
                except IndexError:
                    break
                if slice_to_check in nums_spelled_out.keys():
                    numbers.append(nums_spelled_out[slice_to_check])
                    current_spot += legit_options[current_letter][0] - 2
            elif current_letter in ["t", "f", "s"]:
                try:
                    next_letter = line[current_spot + 1]
                except IndexError:
                    break
                if next_letter in legit_options[current_letter].keys():
                    length_of_slice = (
                        current_spot + legit_options[current_letter][next_letter][0]
                    )
                    try:
                        slice_to_check = line[current_spot:length_of_slice]
                    except IndexError:
                        break

                    if slice_to_check in nums_spelled_out.keys():
                        numbers.append(nums_spelled_out[slice_to_check])
                        current_spot += (
                            legit_options[current_letter][next_letter][0] - 2
                        )

            elif current_letter.isdigit():
                numbers.append(current_letter)

            current_spot += 1

        sum += int(numbers[0] + numbers[-1])

print(sum)
