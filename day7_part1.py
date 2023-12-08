from icecream import ic
from collections import Counter

file = open("day7_data.txt")
data = file.read().split("\n")
file.close()

high_card_strengths = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 1,
    "2": 1,
}


def high_card_checker(hand: str):
    highest = ""
    current_value = 0
    for card in hand:
        if high_card_strengths[card] > current_value:
            current_value = high_card_strengths[card]
            highest = card
    return highest


hands = {}
for line in data:
    hand = line.split(" ")[0]
    bet = line.split(" ")[1]
    hand_counter = Counter(hand)
    hands[hand] = [hand_counter]
    ic(hand, bet, hand_counter, hands)
    if len(hand_counter) == 5:
        ic("High card")
        hands[hand].append("HIGH_CARD")
        hands[hand].append(high_card_checker("".join([i for i in hands.keys()])))

    elif len(hand_counter) == 4:
        ic("A Pair")
        hands[hand].append("PAIR")
        hands[hand].append(hand_counter.most_common(1)[0][0])

    elif len(hand_counter) == 3:
        x = hand_counter.most_common(3)
        ic(x)

    elif len(hand_counter) == 1:
        ic("Five of a kind")
        hands[hand].append("FIVE")
        hands[hand].append(hand_counter.most_common(1)[0][0])

    ic(hands[hand])


# ic(data)
