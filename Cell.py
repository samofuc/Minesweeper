class Cell:
    def __init__(self, open = False, mine = False):
        self.open = open
        self.mine = mine
        self.neighbour_mine_count = 0
    
    def __str__(self):
        return "open" + str(self.open) + "mine" + str(self.mine)

    def get_open(self):
        return self.open

    def set_open(self, open):
        self.open = open

    def get_mine(self):
        return self.mine

    def set_mine(self, mine):
        self.mine = mine

    def get_neighbour_mine_count(self):
        return self.neighbour_mine_count
    
    def set_neighbour_mine_count(self, value):
        self.neighbour_mine_count = value
    
    def dump(self):
        print("open:" + str(self.open))
        print("mine:" + str(self.mine))

A = Cell()
A.dump()
b = Cell(True, True)
b.dump()
A.set_open(True)
A.dump()

