import Cell
import random

class Board:
    def __init__(self, width, height, mine_count):
        self.width = width
        self.height = height
        self.mine_count = mine_count
        self.board = None
        self.init_board()

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_mine_count(self):
        return self.mine_count

    def get_cell(self, row, col):
        return self.board[row][col]

    def get_mine(self, row, col):
        return self.get_cell(row, col).get_mine()

    def set_mine(self, row, col, value):
        self.get_cell(row, col).set_mine(value)

    def get_open(self, row, col):
        return self.get_cell(row, col).get_open()
    
    def set_open(self, row, col, value):
        self.get_cell(row, col).set_open(value)

    def get_marked(self, row, col):
        return self.get_cell(row, col).get_marked()

    def toggle_marked(self, row, col):
        print("toggle" + str(row) + str(col))
        self.get_cell(row, col).toggle_marked()

    def get_neighbour_mine_count(self, row, col):
        return self.get_cell(row, col).get_neighbour_mine_count() 

    def set_neighbour_mine_count(self, row, col, value):
        self.get_cell(row, col).set_neighbour_mine_count(value)

    def get_display_value(self, row, col):
        return self.get_cell(row, col).get_display_value() 

    def dump(self):
        print("width:" + str(self.width))
        print("height:" + str(self.height))
        print("mine_count:" + str(self.mine_count))
        #print(self.board.__str__())
        self.dump_board()

    def init_board(self):
        #naredimo igralno plosco
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(Cell.Cell())
            self.board.append(row)

        #randomly place mines to board
        count = self.mine_count
        while (count > 0):
            row_idx = random.randrange(0, self.height, 1)
            col_idx = random.randrange(0, self.width, 1)
            print(str(row_idx) + "," + str(col_idx))
            if (not self.get_mine(row_idx, col_idx)):
                self.set_mine(row_idx, col_idx, True)
                count = count - 1
            
        #izracunaj st. sosedov z minami in poklici policijo za lastno varnost
        for row in range(self.height):
            for col in range(self.width):
                self.set_neighbour_mine_count(row, col, self.count_neighbour_mines(row, col))

    def count_neighbour_mines(self, row, col):
        count = 0
        for row_idx in range(row - 1, row + 2):
            for col_idx in range(col - 1, col + 2):
                if (row_idx == row and col_idx == col):
                    continue
                if (row_idx < 0 or row_idx >= self.height):
                    continue
                if (col_idx < 0 or col_idx >= self.width):
                    continue
                #print(self.board[row_idx][col_idx].get_mine())
                if self.board[row_idx][col_idx].get_mine() == True:
                    count += 1
        return count

    def dump_board(self):
        for row in range(self.height):
            line = []
            for col in range(self.width):
                line.append(str(self.get_display_value(row, col)))
            print(line)

    def open(self, row, col):
        if self.get_marked(row, col):
            return
        if self.get_open(row, col):
            return
        self.set_open(row, col, True)