from classes import *
from bots import *

def player_input(prompt,type,accept) :
    ans = ""
    while ans not in accept :
        try :
            ans = type(input("\t"+prompt+" --"))
        except ValueError :
            if type == str : print("\t(!) input was not a string")
            if type == int : print("(!) input was not an integer")
    return ans

class Game :
    def __init__(self) :
        self.board = Board(5) # VARIABLE
        self.p1 = Player(1, "☀", 0, 0, self.board.dim, self.board)
        self.p2 = Player(2, "☾", self.board.dim-1, self.board.dim-1, self.board)
        self.bot = CompletelyRandomBot("bot", self.p2, self.board)

    def player_turn(self) :
        print("YOUR TURN")
        if self.p1.get_available_block != -1 :
            op = player_input("[1] move player / [2] place block", int, [1,2])

            if op == 1 :
                dir = player_input("input direction -> [a] : left / [w] : up / [s] : down / [d] : right", str, ["a","s","w","d"])

                while not 
            if op == 2 :

