from classes import * 
from random import random, randint, choice

class CompletelyRandomBot :
    def __init__(self, id, player:Player, board:Board) :
        self.id = id
        self.player = player
        self.board = board

    def move(self) :
        if self.player.check_surrounded() : return False
        return self.player.move(choice(["a","s","w","d"]))

    def block(self) :
        b = self.player.get_available_block()
        if b == -1 : return False

        x = randint(0,self.board.dim-1)
        y = randint(0,self.board.dim-1)
        while not(self.board.check_coordinates(x,y) and self.board.check_square(x,y)) :
            x = randint(0,self.board.dim-1)
            y = randint(0,self.board.dim-1)
        return self.player.place_block(b,x,y)

    def play(self) :
        if self.player.get_available_block() == -1 :
            self.move()
        else :
            if random() < 0.5 : self.move()
            else : self.block()
        