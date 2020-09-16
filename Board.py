import Cell
import random
import GameStatus

class Board:

    def __init__(self, width, height, mine_count):
        self.init(width, height, mine_count)

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

    def get_exploded(self, row, col):
        return self.get_cell(row, col).get_exploded()

    def set_exploded(self, row, col, value):
        self.get_cell(row, col).set_exploded(value)
        self.status = GameStatus.GameStatus.Failure

    def get_open(self, row, col):
        return self.get_cell(row, col).get_open()
    
    def set_open(self, row, col, value):
        self.get_cell(row, col).set_open(value)

    def get_marked(self, row, col):
        return self.get_cell(row, col).get_marked()

    def toggle_marked(self, row, col):
        if self.get_open(row, col):
            return
        self.get_cell(row, col).toggle_marked()
        if self.get_marked(row, col):
            self.remaining_mine_count -= 1
        else:
            self.remaining_mine_count += 1
    
    def get_remaining_mine_count(self):
        return self.remaining_mine_count

    def get_neighbour_mine_count(self, row, col):
        return self.get_cell(row, col).get_neighbour_mine_count() 

    def set_neighbour_mine_count(self, row, col, value):
        self.get_cell(row, col).set_neighbour_mine_count(value)

    def get_visited(self, row, col):
        self.get_cell(row, col).get_visited()

    def set_visited(self, row, col, value):
        self.get_cell(row, col).set_visited(value)

    def is_game_in_progress(self):
        return (self.status == GameStatus.GameStatus.InProgress)

    def init(self, width, height, mine_count):
        self.width = width
        self.height = height
        self.mine_count = mine_count
        self.board = None
        self.remaining_mine_count = mine_count
        self.status = GameStatus.GameStatus.InProgress

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
    
    def get_neighbour_marked_count(self, row, col):
        count = 0
        for row_idx in range(row - 1, row + 2):
            for col_idx in range(col - 1, col + 2):
                if (row_idx < 0 or row_idx >= self.height):
                    continue
                if (col_idx < 0 or col_idx >= self.width):
                    continue
                if (row_idx == row and col_idx == col):
                    continue
                if self.get_marked(row_idx, col_idx):
                    count += 1
        return count

    def dump_board(self):
        for row in range(self.height):
            line = []
            for col in range(self.width):
                line.append(str(self.get_display_value(row, col)))
            print(line)

    def clear_visited(self):
        for row in range(self.height):
            for col in range(self.width):
                self.set_visited(row, col, False)

    def open(self, row, col):
        if self.get_marked(row, col):
            return

        if self.get_open(row, col):
            return

        if self.get_mine(row, col):
            self.set_exploded(row, col, True)
            self.on_game_lost()
            return

        if self.get_neighbour_mine_count(row, col) > 0:
            self.set_open(row, col, True)
            return

        # celica je prazna
        self.clear_visited()
        self.set_open(row, col, True)
        cells_curr = [(row, col)]
        cells_next = []
        while len(cells_curr) > 0:
            for cell in cells_curr:
                row = cell[0]
                col = cell[1]
                for row_idx in range(row - 1, row + 2):
                    for col_idx in range(col - 1, col + 2):
                        if (row_idx < 0 or row_idx >= self.height):
                            continue
                        if (col_idx < 0 or col_idx >= self.width):
                            continue
                        if self.get_visited(row_idx, col_idx):
                            continue
                        self.set_visited(row_idx, col_idx, True)
                        if (row_idx == row and col_idx == col):
                            continue
                        if self.get_open(row_idx, col_idx):
                            continue
                        if self.get_marked(row_idx, col_idx):
                            continue
                        if self.board[row_idx][col_idx].get_mine() == True:
                            continue
                            
                        self.set_open(row_idx, col_idx, True)
                        if self.get_neighbour_mine_count(row_idx, col_idx) == 0:
                            cells_next.append((row_idx, col_idx))
            
            cells_curr = cells_next
            cells_next = []

    def open_neighbours(self, row, col):
        if not self.get_open(row, col):
            return
        if self.get_neighbour_marked_count(row, col) != self.get_neighbour_mine_count(row, col):
            return
        mine_exploded = False
        for row_idx in range(row - 1, row + 2):
            for col_idx in range(col - 1, col + 2):
                if (row_idx < 0 or row_idx >= self.height):
                    continue
                if (col_idx < 0 or col_idx >= self.width):
                    continue
                if self.get_open(row_idx, col_idx):
                    continue
                if self.get_marked(row_idx, col_idx):
                    continue
                if self.get_mine(row_idx, col_idx):
                    self.set_exploded(row_idx, col_idx, True)
                    mine_exploded = True
                if self.get_neighbour_mine_count(row_idx, col_idx) == 0:
                    self.open(row_idx, col_idx)
                self.set_open(row_idx, col_idx, True)
        if mine_exploded:
            self.on_game_lost()

    def on_game_lost(self):
        for row_idx in range(self.height):
            for col_idx in range(self.width):
                if self.get_mine(row_idx, col_idx):
                    self.set_open(row_idx, col_idx, True)
                else:
                    if self.get_marked(row_idx, col_idx):
                        self.set_open(row_idx, col_idx, True)
     