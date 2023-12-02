sum = 0
data = "day1_part1_example_data.txt"
with open(data) as file:
    for line in file:
        line = line.strip()
        numbers = []

        for char in line:
            if char.isdigit():
                numbers.append(char)
        sum += int(numbers[0] + numbers[-1])

print(sum)
