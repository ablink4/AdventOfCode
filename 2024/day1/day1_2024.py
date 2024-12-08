"""
Advent of Code 2024, Day 1:
https://adventofcode.com/2024/day/1
"""
from typing import List, Tuple


def get_lists_from_input(input_list: str) -> Tuple[List[int],List[int]]:
    lines = input_list.split('\n')

    left_list = []
    right_list = []

    for line in lines:
        parts = line.split()
        if len(parts) != 2:
            print(f"Error parsing line: {line}")
            continue

        left,right = parts[0],parts[1]
        left_list.append(int(left))
        right_list.append(int(right))

    left_list = sorted(left_list, reverse=True)
    right_list = sorted(right_list, reverse=True)

    return left_list,right_list

def get_distance(left: List[int], right: List[int]) -> int:
    distance = 0

    if len(left) != len(right):
        print(f"Lists are not the same length, got left length = {len(left)}, right length = {len(right)}")
    else:
        # we've alrady verified lengths are matching, so it doesn't matter which list we take the len() of
        for i in range(len(left)):
            distance += abs(left[i] - right[i])

    return distance


if __name__ == "__main__":
    with open('day1_2024_input.txt', 'r') as infile:
        data = infile.read()
        l, r = get_lists_from_input(data)
        distance = get_distance(l, r)

        print(distance)