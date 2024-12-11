"""
Day 2 of Advent of Code 2024
"""
from typing import List


s = r"""7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

def is_list_safe(data: str) -> bool:
    safe = True  # default to True because we'll break as soon as it's unsafe
    values = [int(x) for x in data.split()]

    # we will track which direction the list goes
    ascending = False
    descending = False

    for i in range(len(values)):
        # we care about distance between values so skip very first number
        if i == 0:
            continue

        if values[i] == values[i - 1]:
            safe = False
            break

        if i == 1:
            if values[i] > values[i - 1]:
                ascending = True
            elif values[i] < values[i - 1]:
                descending = True
        else:
            if ascending and values[i] < values[i - 1]:
                safe = False
                break
            elif descending and values[i] > values[i - 1]:
                safe = False
                break

        distance = abs(values[i] - values[i - 1])

        if distance > 3:
            safe = False
            break

    return safe


if __name__ == "__main__":
    with open('day2_2024_input.txt', 'r') as infile:
        data = infile.readlines()

        safe_count = 0
        for l in data:
            if is_list_safe(l):
                safe_count += 1

        print(safe_count)
