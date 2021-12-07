#!/bin/python

from copy import copy

INPUT = [(i.strip('\n')) for i in open('input.txt', 'r').readlines()]

def part_1(numbers):
    positions = list(map(lambda x: [0, 0,], range(len(numbers[0]))))

    for line in numbers:
        for idx, num in enumerate(line):
            positions[idx][int(num)] += 1

    gamma = "".join([str(totals.index(max(totals))) for totals in positions])
    epsilon = "".join([str(totals.index(min(totals))) for totals in positions])

    print("Power consumption: %s" % (int(gamma, base=2) * int(epsilon, base=2)))
    return gamma, epsilon

def _get_most_common_in_position(numbers, position, most_or_least):
    """
    Find the most common bit for a given position
    Returns 1 if they are equally common
    """
    dominant = [0, 0]
    for line in numbers:
        thing = int(line[position])
        dominant[thing] += 1
    if most_or_least == 'oxygen':
        if dominant[0] == dominant[1]:
            return 1
        else:
            return dominant.index(max(dominant))
    elif most_or_least == 'co2':
        if dominant[0] == dominant[1]:
            return 0
        else:
            return dominant.index(min(dominant))

def _filter_unmatched(numbers, position, most_common):
    filtered_numbers = []
    for number in numbers:
        if int(number[position]) == most_common:
            filtered_numbers.append(number)
    return filtered_numbers


def part_2(nums):
    ratings = {}
    for commonality in ['oxygen', 'co2']:
        numbers = copy(nums)
        for position in range(len(nums[0])):
            if len(numbers) > 1:
                common = _get_most_common_in_position(numbers, position, commonality)
                numbers = _filter_unmatched(numbers, position, common)
            else:
                break
        ratings.update({commonality: numbers[0]})
    
    print("Life support rating: %d" % (int(ratings['oxygen'],
                                       base=2) * int(ratings['co2'], base=2)))
    print(ratings)


print(part_1(INPUT))
part_2(INPUT)