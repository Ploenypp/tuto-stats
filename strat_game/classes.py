class Board :
    def __init__(self, dim) :
        self.dim = dim
        self.grid = [[" " for i in range(dim)] for j in range(dim)]

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
    
    # checks if a square is available or not
    def check_square(self, x, y) :
        return self.grid[y][x] == " "
    
    # checks if the proposed coordinates are out of bounds or in the end goal spots
    def check_coordinates(self, x, y) :
        return not((x == 0 and y == 0) or (x == self.dim - 1 and y == self.dim - 1) or x < 0 or x >= self.dim or y < 0 or y >= self.dim)
    
    def place(self, marker, x, y) :
        self.grid[y][x] = marker
    
    def update(self, marker, x0, y0, x1, y1) :
        self.grid[y0][x0] = " "
        self.grid[y1][x1] = marker

class Block :
    def __init__(self, dim, board:Board) :
        self.marker = "◼︎"
        
        self.x = -1
        self.y = -1
        self.life = 3 # VARIABLE

        self.cpt = self.life
        self.active = False

        self.board = board
        self.dim = dim

    def countdown(self) :
        self.cpt -= 1
        if self.cpt == 0 :
            self.board.place(" ",self.x,self.y)
            self.cpt = self.life
            self.x = -1
            self.y = -1
            self.active = False

    def place(self, x, y) :
        if self.board.check_coordinates(x,y) and self.board.check_square(x,y) :
            self.board.place(self.marker, x, y)
            self.x = x
            self.y = y
            self.active = True
            return True
        return False

class Player :
    def __init__(self, id, marker, x, y, dim, board:Board) :
        self.id = id
        self.marker = marker

        self.x = x
        self.y = y

        self.dim = dim
        self.board = board

        self.blocks = [Block()] * (dim/2)

    # returns the index of the first available block
    def get_available_block(self) :
        for i in range(self.nb_blocks - 1) :
            if self.blocks[i].active == False : return i
        return -1
    
    def place_block(self, idx, x, y) :
        return self.blocks[idx].place(x,y)
    
    # checks if currently surrounded
    # True = surrounded
    def check_surrounded(self) :
        coordinates = [(self.x+1, self.y),(self.x,self.y+1),(self.x-1, self.y),(self.x, self.y-1)]

        for x,y in coordinates :
            if not (self.board.check_coordinates(x,y) or self.board.check_square(x,y)) : return True

        return False
    
    def get_accessible_dir(self) :
        x = self.x
        y = self.y

        dir = []

        if x - 1 >= 0 and self.board.grid[y][x-1] == " " : dir.append("a")
        if y - 1 >= 0 and self.board.grid[y-1][x] == " " : dir.append("w")
        if y + 1 < self.dim and self.board.grid[y+1][x] == " " : dir.append("s")
        if x + 1 < self.dim and self.board.grid[y][x+1] == " " : dir.append("d")

        return dir

    def move(self, dir) :
        x = self.x
        y = self.y
        match dir :
            case "a" : self.x -= 1
            case "s" : self.y += 1
            case "w" : self.y -= 1
            case "d" : self.x += 1
        if self.board.check_coordinates(x, y) :
            self.board.update(self.marker,self.x,self.y,x,y)
            return True
        return False
