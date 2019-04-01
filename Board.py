import random
import math
import os
from enum import Enum

class State(Enum):
    isBomb = 400
    isIllegal = 404
    isSucc = 200


class Board:
    def __init__(self, r, c, n_bomb):
        assert r*c>=n_bomb
        self.r = r
        self.c = c
        self.n_bomb = n_bomb

        self.bomb_list = self.initBomb()
        self.map = self.initMap()

    def initBomb(self):
        b_list = random.sample(range(self.r * self.c), self.n_bomb)
        return set([ (x//self.c, x%self.c) for x in b_list]) #store the coordinate of bombs.

    def initMap(self):
        m = [ ['X' for j in range(self.c)] for i in range(self.r)]
        self.visit = [[0 for j in range(self.c)] for i in range(self.r)]
        return m

    def click(self,x, y):
        '''
        :param x: the coordinate x
        :param y: the coordinate y
        :return: the SIGNAL
        400 - click the bomb
        404 - click the place has been cleaned
        200 - Success
        '''
        #print(x,y)
        if x < 0 or x >= self.r or y < 0 or y >= self.c or self.visit[x][y] == 1:
            return State.isIllegal
        if (x,y) in self.bomb_list:
            return State.isBomb

        n_bomb = 0
        arrs = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        #detect
        for arr in arrs:
            newx = x + arr[0]
            newy = y + arr[1]
            if newx >=0 and newx < self.r and newy >=0 and newy < self.c and (newx, newy) in self.bomb_list:
                n_bomb += 1

        self.visit[x][y] = 1

        if n_bomb > 0:
            self.map[x][y] = str(n_bomb)
        else:
            for arr in arrs:
                newx = x + arr[0]
                newy = y + arr[1]
                _ = self.click(newx, newy)
            self.map[x][y] = ' '
        return State.isSucc

    def check(self):
        left_bomb = 0
        for i in range(self.r):
            for j in range(self.c):
                if self.map[i][j] == 'X':
                    left_bomb +=1
        return left_bomb == self.n_bomb

    def showBombData(self):
        for i in range(self.r):
            line = ""
            for j in range(self.c):
                if (i,j) in self.bomb_list:
                    line += " B"
                else:
                    line += " X"
            print(line)


    def show(self):
        print(" ")
        for i in range(self.r):
            line = ""
            for j in range(self.c):
                line += " "+self.map[i][j]
            print(line)


if __name__ == '__main__':
    board = Board(10,10,20)
    board.show()
    board.click(3,4)
    board.show()
