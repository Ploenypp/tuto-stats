from random import random, randint, choice

class Board :
    def __init__(self, dim, block_life) :
        self.dim = dim
        self.grid = [[" " for i in range(dim)] for j in range(dim)]
        self.p1 = (0,0)
        self.p2 = (dim - 1, dim - 1)

        self.block_life = block_life
        self.p1_blocks = [-1] * (dim - 1)
        self.p2_blocks = [-1] * (dim - 1)
        
        self.grid[0][0] = "☀"
        self.grid[dim-1][dim-1] = "☾"
    
    def show(self) :
        print("___| ",end="")
        for i in range(self.dim) :
            print(i,end=" | ")
        print()
        i = 0
        for row in self.grid :
            print(i," |",end=" ")
            i += 1
            for square in row : 
                print(square,end=" | ")
            print("")

    def place_block(self, player, x, y) :
        if x < 0 or x > self.dim - 1 or y < 0 or y > self.dim - 1 : # coordinate check
            print("\n\t(!) invalid coordinates")
            return False
        if (x == 0 and y == 0) or (x == self.dim -1 and y == self.dim-1): # coordinate check
            print("\n\t(!) invalid coordinates")
            return False
        b = 0
        if player == 1 :
            while b < self.dim : # availability check
                if self.p1_blocks[b] == -1 : break
                b += 1
            if b == self.dim :
                print("\n\t(!) no blocks available")
                return False
            if self.grid[y][x] == " " : 
                self.grid[y][x] = "☐"
                self.p1_blocks[b] = self.block_life
                return True
        else :
            while b < self.dim : # availability check
                if self.p2_blocks[b] == -1 : break
                b += 1
            if b == self.dim : 
                print("\n\t(!) no blocks available")
                return False
            if self.grid[y][x] == " " : 
                self.grid[y][x] = "◼︎"
                self.p2_blocks[b] = self.block_life
                return True
        return False
    
    def move_player(self, player, x, y) :
        # coordinate check by player class
        if self.grid[y][x] != " " :
            print("\n\t(!) inaccessible square")
            return False
        if player == 1 :
            self.grid[self.p1[1]][self.p1[0]] = " "
            self.grid[y][x] = "☀"
            self.p1 = (x,y)
            return True
        else :
            self.grid[self.p2[1]][self.p2[0]] = " "
            self.grid[y][x] = "☾"
            self.p2 = (x,y)
            return True
    
    def update(self) :
        # check success 
        if self.p1 == (self.dim-1, self.dim-1) :
            print("Player 1 wins!")
            return True
        if self.p2 == (0,0) :
            print("Player 2 wins!")
            return True
        # countdown blocks
        for i in range(dim-1) :
            if self.p1_blocks[i] > -1 :
                self.p1_blocks[i] -= 1
                if self.p1_blocks[i] == 0 :
                    self.p1_blocks[i] = -1
                    self.p1.blocks += 1

            if self.p2_blocks[i] > -1 :
                self.p2_blocks[i] -= 1
                if self.p2_blocks[i] == 0 :
                    self.p2_blocks[i] = -1
                    self.p2.blocks += 1

        
        
        return False

class Player :
    def __init__(self, id, x, y, dim) :
        self.id = id
        self.x = x
        self.y = y
        self.dim = dim 

        self.blocks = dim - 1

    def move_player(self, dir, board:Board) :
        match dir :
            case "a" :
                if self.x == 0 : # left
                    print("\n\t(!) invalid move")
                    return False
                if board.move_player(self.id, self.x - 1, self.y) : self.x -= 1
            case "w" :
                if self.y == 0 : # up
                    print("\n\t(!) invalid move")
                    return False
                if board.move_player(self.id, self.x, self.y - 1) : self.y -= 1
            case "s" : # down
                if self.y == self.dim - 1 :
                    print("\n\t(!) invalid move")
                    return False
                if board.move_player(self.id, self.x, self.y + 1) : self.y += 1
            case "d" : # right
                if self.x == self.dim - 1 :
                    print("\n\t(!) invalid move")
                    return False
                if board.move_player(self.id, self.x + 1, self.y) : self.x += 1
        return True
    
    def place_block(self, x, y, board) :
        if self.blocks == 0 : 
            print("\n\t(!) no blocks available")
            return False
        if board.place_block(self.id, x, y) : 
            self.blocks -= 1
            return True

class CompletelyRandomBot :
    def __init__(self, player_class:Player, board:Board, dim) :
        self.p = player_class
        self.b = board
        self.dim = dim

    def play(self) :
        success = False
        if self.p.blocks != 0 :
            if random() < 0.5 : # move
                moves = ["a","s","w","d"]
                success = self.p.move_player(choice(moves),self.b)
                while not success :
                    success = self.p.move_player(choice(moves),self.b)
            else : # place block
                success = self.p.place_block(randint(0,self.dim-1), randint(0,self.dim-1), self.b)
                while not success :
                    success = self.p.place_block(randint(0,self.dim-1), randint(0,self.dim-1), self.b)
        else : 
            moves = ["a","s","w","d"]
            success = self.p.move_player(choice(moves),self.b)
            while not success :
                success = self.p.move_player(choice(moves),self.b)

# initialization
dim = 10
b = Board(dim, 3)
p1 = Player(1,0,0,10)
p2 = Player(2,9,9,10)
bot = CompletelyRandomBot(p2,b,dim)
b.show()

game_over = False
while not game_over :
    print("\n# YOUR TURN")
    op_success = False
    op = int(input("[1] move player / [2] place block --"))
    while op != 1 and op != 2 : 
        op = int(input("[1] move player / [2] place block --"))
        
    if op == 1 :
        while not op_success :
            dir = input("\tinput direction -> [a] : left / [w] : up / [s] : down / [d] : right --")
            while dir != "a" and dir != "w" and dir != "s" and dir != "d" :
                print(dir != "a" and dir != "w" and dir != "s" and dir != "d")
                dir = input("\tinput direction -> [a] : left / [w] : up / [s] : down / [d] : right --")
            op_success = p1.move_player(dir, b) 
        
    if op == 2 :
        while not op_success :
            x = int(input(f"input x-coordinate (0 : {dim - 1}) --"))
            while x < 0 or x > dim - 1 : 
                x = int(input(f"input x-coordinate (0 : {dim - 1}) --"))
                
            y = int(input(f"input y-coordinate (0 : {dim - 1}) --"))
            while y < 0 or y > dim - 1 : 
                y = int(input(f"input y-coordinate (0 : {dim - 1}) --"))
            op_success = p1.place_block(x, y, b)
    print("\n#BOT'S TURN")
    bot.play()
    b.show()
    game_over = b.update()