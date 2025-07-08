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
        if ans not in accept : print("\t(!) input not in accepted values")
    return ans

class Game :
    def __init__(self) :
        self.board = Board(5) # VARIABLE
        self.dim = self.board.dim
        self.p1 = Player(1, "☀", 0, 0, self.dim, self.board)
        self.p2 = Player(2, "☾", self.dim-1, self.dim-1, self.board)
        self.bot = CompletelyRandomBot("bot", self.p2, self.board)

    def player_turn(self) :
        print("YOUR TURN")
        block = self.p1.get_accessible_dir()
        surrounded = self.p1.check_surrounded()

        match block, surrounded :
            case -1, True : 
                print("\t(!) no available blocks, player surrounded")
                print("\tmust pass turn")
            
            case _, True :
                print("\t(!) player surrounded")
                print("\tmust place block")

                x = player_input("input X-coordinate",int,list(range(0,self.dim)))

                y = player_input("input Y-coordinate",int,list(range(0,self.dim)))

                # loop if not able to place block and/or add error message to Block.place()

            case -1, False :
                print("\t(!) no available blocks")
                print("\tmust move")

            case _, False :


        if self.p1.get_available_block == -1 :
            print("\t(!) no available blocks")
            
            if not self.p1.check_surrounded() :
                available = self.p1.get_accessible_dir()

                dir_code = {"a":"left","w":"up","s":"down","d":"right"}

                dir_str = " | ".join([f"[{x}] : {dir_code[x]}" for x in available])

                dir = player_input(f"input direction -> {dir_str}", str, available)

                self.p1.move(dir)

            else :
                print("\t(!) player surrounded")
                print("\t(!) must pass turn")

        elif 
            