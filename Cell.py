class Cell:
    def __init__(self, open = False, mine = False, marked = False):
        self.open = open
        self.mine = mine
        self.marked = marked
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
    
    def get_marked(self):
        return self.marked
    
    def toggle_marked(self):
        if not self.open:
            print("marked je" + str(self.marked))
            self.marked = not self.marked
        print("marked je" + str(self.marked))

    def get_neighbour_mine_count(self):
        return self.neighbour_mine_count
    
    def set_neighbour_mine_count(self, value):
        self.neighbour_mine_count = value
    
    def get_display_value(self):
        if self.marked:
            return "O"
        elif self.open:
            if self.mine:
                return "m"
            else:
                return str(self.neighbour_mine_count)
        else:
            return "x"

    def dump(self):
        print("open:" + str(self.open))
        print("mine:" + str(self.mine))

#A = Cell()
#A.dump()
#b = Cell(True, True)
#b.dump()
#A.set_open(True)
#A.dump()

