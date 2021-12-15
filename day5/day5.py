#!/bin/python

import pandas as pd


INPUT = [x.strip().split(" -> ") for x in open('lines.txt', 'r').readlines()]
all_coordinates = list(map(lambda x: [list(map(int, x[0].split(","))), 
                                      list(map(int, x[1].split(",")))], INPUT))
def part_1():
    def _is_vertical_or_horizontal(coordinates):
        """
        filter any invalid lines?
        """
        return (coordinates[0][0] == coordinates[1][0] or
                coordinates[0][1] == coordinates[1][1] or
                abs(coordinates[0][0] - coordinates [1][0]) == abs(coordinates[0][1] - coordinates [1][1])
                )

    valid_coordinates = list(filter(_is_vertical_or_horizontal, all_coordinates))

    dataframe = pd.DataFrame(0, index=range(1001), columns=range(1001))

    def _step(val, distance):
        if distance < 0:
            val -= 1
            return val
        else:
            val += 1
            return val

    for coordinates in valid_coordinates:
        coordinates.sort()

        x1, x2 = coordinates[0][0], coordinates[1][0]
        y1, y2 = coordinates[0][1], coordinates[1][1]

        distance_x = x2 - x1
        distance_y = y2 - y1

        if abs(distance_x) == abs(distance_y):
            while x1 <= x2:
                dataframe.iloc[x1, y1] += 1
                x1 = _step(x1, distance_x)
                y1 = _step(y1, distance_y)
        else:
            dataframe.iloc[x1:x2 + 1, y1:y2 + 1] += 1
    
    # normalize and flag all overlapping an non-overlapping
    dataframe.mask(dataframe < 2, 0, inplace=True)
    dataframe.mask(dataframe >= 2, 1, inplace=True)

    print(dataframe.sum().sum())

part_1()






