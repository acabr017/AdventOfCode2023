from icecream import ic
from collections import Counter


file = open("day7_data.txt")
data = file.read().split("\n")
file.close()

high_card_strengths = {"A": "14", "K": "13", "Q": "12", "T": "10", "J": "01"}


def hand_conversion(hand: list):
    output = ""
    for char in hand:
        if char.isdigit() and len(char) < 2:
            output += "0"
            output += char
        elif char.isdigit():
            output += char
        else:
            output += high_card_strengths[char]
        output += "|"
    return output


def swapper(elements, swap, letter_to_swap):
    elements = list(elements)
    for i, char in enumerate(elements):
        if char == letter_to_swap:
            elements[i] = swap
    return elements


def deal_with_J(hand):
    # formatted_hand = hand_conversion(hand)
    # elements = formatted_hand.split("||")[0].split("|")
    # bet = formatted_hand.split("||")[1]
    count = Counter(hand)
    if len(count) == 1:
        return {"A": 1}

    else:
        highest_freq = 0
        highest_val_to_swap = ""
        for k, v in count.items():
            if k == "J":
                continue
            if v >= highest_freq:
                highest_freq = v
                highest_val_to_swap = k
        elements = swapper(hand, highest_val_to_swap, "J")

    return Counter(elements)


def organizer(hand, hand_counter):
    if len(hand_counter) == 1:
        five.append(hand)
    elif len(hand_counter) == 5:
        high.append(hand)
    elif len(hand_counter) == 4:
        pair.append(hand)
    elif len(hand_counter) == 2:
        if 4 in hand_counter.values():
            four.append(hand)
        elif 3 in hand_counter.values():
            f_house.append(hand)
    elif len(hand_counter) == 3:
        if 3 in hand_counter.values():
            three.append(hand)
        elif 2 in hand_counter.values():
            two_pair.append(hand)


five = []
four = []
f_house = []
three = []
two_pair = []
pair = []
high = []

all_combos = [high, pair, two_pair, three, f_house, four, five]

for line in data:
    hand = line.split(" ")[0]
    if "J" in hand:
        hand_counter = deal_with_J(hand)
    else:
        hand_counter = Counter(hand)
    bet = line.split(" ")[1]
    hand = hand_conversion(hand) + "|" + bet

    organizer(hand, hand_counter)


full_sorted_list = []
for kind in all_combos:
    full_sorted_list += sorted(kind)


total_winnings = 0

for i, hand in enumerate(full_sorted_list):
    total_winnings += int(hand.split("||")[1]) * (i + 1)

# ic(full_sorted_list)

ic(total_winnings)
