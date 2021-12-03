#!/bin/python

NUMBERS = [int(i.strip('\n')) for i in open('input.txt', 'r').readlines()]
WINDOW = 3

def part_1():
    count = 0
    prev_num = float('inf')
    for curr_num in NUMBERS:
        count += int(curr_num > prev_num)
        prev_num = curr_num
    return count

def part_2():
    count = 0
    prev_sum = float('inf')
    for line in range(WINDOW, len(NUMBERS) + 1):
        curr_sum = sum(NUMBERS[(line-WINDOW):line])
        count += int(curr_sum > prev_sum)
        prev_sum = curr_sum
    return count


print(part_1())
print(part_2())
