from Board import Board,State
from enum import Enum
import os
import re
import ast

class GameState(Enum):
    Fail = 400
    Illegal = 404
    Succ = 200

class GameProxy:

    def __init__(self,R,C,B):
        self.r = R
        self.c = C
        self.n_bomb = B
        self.Init()

    def Init(self):
        self.board = Board(self.r,self.c,self.n_bomb)

    def launch(self):
        while True:
            os.system("cls")
            feedback = self.new_round()
            if feedback == GameState.Fail:
                print("Oops! You click the bomb!")
                print("Here are the whole map:\n")
                self.board.showBombData()
                ipt = input("\n Type in any key to restart: ")
                if ipt == 'E' or ipt == 'e' or ipt == 'Exit' or ipt == 'exit':
                    exit()
                else:
                    self.Init()
                    self.launch()
            if feedback == GameState.Illegal:
                print("Oops! You click an illegal position! Retry!")
                input("Any key")
            if feedback == GameState.Succ:
                print("CONGRATS! You win the game!")
                print("Here are the whole map:\n")
                self.board.showBombData()
                ipt = input("\n Type in any key to restart: ")
                if ipt == 'E' or ipt == 'e' or ipt == 'Exit' or ipt == 'exit':
                    exit()
                else:
                    self.Init()
                    self.launch()

    def new_round(self):
        self.board.show()
        ipt = input("\n Hi, please input a position as a_b: ")
        if re.match("\d+\s\d+$",ipt) is None:
            return GameState.Illegal
        ipt = ipt.split(" ")
        x,y = int(ipt[0]),int(ipt[1])
        x-=1
        y-=1
        feedback = self.board.click(x,y)
        if feedback == State.isBomb:
            return GameState.Fail
        elif feedback == State.isIllegal:
            return GameState.Illegal
        else:
            if self.board.check():
                return GameState.Succ
            else:
                return None


if __name__ == '__main__':
    game = GameProxy(10,10,10)
    game.launch()