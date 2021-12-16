#!/bin/python

from statistics import median, mean

def part_1():
    fuel_cost = 0

    start_positions = [int(x) for x in open('input.txt', 'r').read().split(",")]

    end_position = int(median(start_positions))

    for x in start_positions:
        fuel_cost += abs(end_position - x)
    
    print(fuel_cost)

def part_2():
    fuel_cost = 0
    start_positions = [int(x) for x in open('input.txt', 'r').read().split(",")]
    end_position = int(mean(start_positions))

    def _triangular(n):
        num = 0
        for i in range(1, n + 1):
            num += i
        return num

    for x in start_positions:
        distance = abs(end_position - x)
        fuel_cost += abs(_triangular(distance))

    print(fuel_cost)


part_1()
part_2()