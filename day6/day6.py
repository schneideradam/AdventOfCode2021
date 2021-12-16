#!/bin/python
import numpy as np

GESTATION_DAYS = 8

def part_1(days):
    genesis = np.array([int(x) for x in open('input.txt', 'r').read().split(",")])
    count = 0
    for _ in range(days):
        count = list(genesis).count(0)
        genesis = np.where(genesis == 0, 7, genesis)
        genesis = np.subtract(genesis, 1)
        genesis = np.append(genesis, [GESTATION_DAYS for _ in range(count)])
    print("Part 1: %s" % len(genesis))


def part_2(days):
    genesis = np.array([int(x) for x in open('input.txt', 'r').read().split(",")])
    totals = [0] * (GESTATION_DAYS + 1)

    # generate an initial totals list
    for counter in range(len(totals)):
        totals[counter] = list(genesis).count(counter)
    
    # update the list as it populates
    for _ in range(days):
        count = totals[0]
        totals[7] += totals[0] # replace all zeros with 7
        totals[0] = 0

        for i in range(len(totals) - 1):
            totals[i] = totals[i + 1] # subtract 1 or shift everything left

        totals[8] = count #append the 8s

    print("Part 2: %s" % sum(totals))

part_1(80)
part_2(256)