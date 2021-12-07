#!/bin/python

from numpy import empty
import pandas as pd

class Bingo:
    def __init__(self):
        self.boards = []
        self.called_numbers = []
        self.first_winner = pd.DataFrame()

    def make_data_frames(self):
        board = []
        for x in open('boards.txt', 'r').readlines():
            if x != '\n':
                board.append([int(i) for i in x.split()])
            if x == '\n' and len(board) == 5:
                self.boards.append(pd.DataFrame(board,
                                   columns=['B', 'I', 'N', 'G', 'O']))
                board = []
        return self.boards

    def flip_boards(self, number):
        for board in self.boards:
            board.replace(number, -1, True)
            if not self._check_bingo(board):
                if self.first_winner.empty: # if we don't have a winner yet
                    print(("FIRST /WINNER:\n{}\nSum: {}\n".format(board,
                           (board.replace(-1, 0).sum().sum() * number))))
                self.first_winner = board


    def marker(self):
        for number in list(map(int, open('called_numbers.txt',
                                         'r').read().split(','))):

            self.flip_boards(number)

            if len(self.boards) == 1 and not self._check_bingo(self.boards[0]):
                return ("LAST WINNER:\n{}\nSum: {}\n".format(self.boards[0],
                    (self.boards[0].replace(-1, 0).sum().sum() * number)))
            else:
                self.boards = list(filter(self._check_bingo, self.boards))
                

    def _check_bingo(self, board):   
        row_sums = board.sum(axis=1)
        col_sums = board.sum(axis=0)
        if any(row_sums == -5) or any(col_sums == -5):
            return False
        else:
            return True
        

bingo = Bingo()
bingo.make_data_frames()
print(bingo.marker())