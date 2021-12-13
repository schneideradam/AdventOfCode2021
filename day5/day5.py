#!/bin/python

import pandas as pd

INPUT = [x.strip().split(" -> ") for x in open('lines_test.txt', 'r').readlines()]
all_coordinates = list(map(lambda x: [list(map(int, x[0].split(","))), 
                                      list(map(int, x[1].split(",")))], INPUT))
def part_1():
    def is_vertical_or_horizontal(coordinates):
        """
        is it a vertical or horizontal line?
        """
        return (coordinates[0][0] == coordinates[1][0] or
                coordinates[0][1] == coordinates[1][1])

    valid_coordinates = list(filter(is_vertical_or_horizontal, all_coordinates))

    dataframe = pd.DataFrame(0, (x for x in range(1001)), (x for x in range(1001)))
    for coordinates in valid_coordinates:
        coordinates.sort()

        x1, x2 = coordinates[0][0], coordinates[1][0]
        y1, y2 = coordinates[0][1], coordinates[1][1]

        dataframe.iloc[x1:x2 + 1, y1:y2 + 1] += 1

    # normalize and flag all overlapping an non-overlapping
    dataframe.mask(dataframe < 2, 0, inplace=True)
    dataframe.mask(dataframe >= 2, 1, inplace=True)

    print(dataframe.sum().sum())


part_1()






