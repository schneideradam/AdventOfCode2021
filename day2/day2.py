#!/bin/python
COMMANDS = open('input.txt', 'r').readlines()

def part_1():
    depth, distance = 0, 0
    for command in COMMANDS:
        direction  = command.split()[0]
        amt = int(command.split()[1])
        if direction == 'forward':
            distance += amt
        elif direction == 'down':
            depth += amt
        else:
            depth -= amt

        if depth < 0: # in case depth is negative, we would be flying.
            depth = 0

    return (distance * depth)


def part_2():
    depth, distance, aim = 0, 0, 0
    for command in COMMANDS:
        direction  = command.split()[0]
        amt = int(command.split()[1])
        if direction == 'forward':
            distance += amt
            depth += aim * amt
        elif direction == 'down':
            aim += amt
        else:
            aim -= amt

        if depth < 0: # in case depth is negative, we would be flying.
            depth = 0

    return (distance * depth)

if __name__ == '__main__':
    print("part 1: %d" % part_1())
    print("part 2: %d" % part_2())