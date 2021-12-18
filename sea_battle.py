import random

class Board:
    FREE_CELL = 99
    BOARD_SIZE = 10
    SHEAP = 33

    def __init__(self):
        self.shoots = set()
        self.board = {}
        self.sheaps_on_board = []
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                self.board[(i, j)] = self.FREE_CELL
        print(self.board)

    def create_ship(self, size):
        c1 = self.get_sheap_place(size)
        sheap_1 = Sheap(c1)
        self.set_place(c1, sheap_1)
        self.sheaps_on_board.append(sheap_1)

    def fill_boats(self):
        self.create_ship(4)
        self.create_ship(3)
        self.create_ship(3)
        self.create_ship(2)
        self.create_ship(2)
        self.create_ship(2)
        self.create_ship(1)
        self.create_ship(1)
        self.create_ship(1)
        self.create_ship(1)

    def set_place(self, coords, symbol):
        for coord in coords:
            self.board[coord] = symbol

    def get_sheap_place(self, boat_size):
        while True:
            i1 = random.randint(0, self.BOARD_SIZE - 1)
            j1 = random.randint(0, self.BOARD_SIZE - 1)
            if self.board[(i1, j1)] != self.FREE_CELL:
                continue
            direction = random.randint(0, 1)
            # 0 = x
            # 1 = y
            sheap_coord = []
            for i in range(boat_size):
                check_coord = (i1, j1 + i) if direction == 0 else (i1 + i, j1)
                if self.can_set(*check_coord):
                    sheap_coord.append(check_coord)

            if len(sheap_coord) == boat_size:
                return sheap_coord

    def in_board(self, x, y):
        return 0 <= x < self.BOARD_SIZE and 0 <= y < self.BOARD_SIZE

    def can_set(self, x, y):
        if not self.in_board(x, y):
            return False
        if self.board[(x, y)] != self.FREE_CELL:
            return False
        delta = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1), (-1, 1), (1, -1)]
        for xd, yd in delta:
            if not (not self.in_board(x+xd, y+yd) or
                    (self.in_board(x+xd, y+yd) and
                     self.board[(x+xd, y+yd)] == self.FREE_CELL)):
                return False
        return True

    def display_board(self):
        for i in range(self.BOARD_SIZE):
            print()
            for j in range(self.BOARD_SIZE):
                if self.board[(i, j)] == self.FREE_CELL:
                    print('#', end=' ')
                else:
                    s = self.board[(i, j)]
                    print(s.display((i, j)), end=' ')

    def miss_check(self, coords):
        if coords in self.board:
            if self.board[coords] != self.FREE_CELL and self.board[coords] != '$':
                self.board[coords] = '$'
                return True
            return False

    def random_coords(self):
        coords = random.choice(self.board.keys)
        if coords not in self.shoots:
            self.shoots.add(coords)
            return coords


class Sheap:
    def __init__(self, coords):
        self.size = len(coords)
        self.status = dict((coord, False) for coord in coords)

    def shoot(self, coords):
        if coords in self.status:
            self.status[coords] = True
            for s in self.status:
                if self.status[s] == False:
                    return True, False
            return True, True
        return False, False

    def am_i_die(self):
        return all(self.status.values())

    def display(self, coords):
        if self.am_i_die():
            return 'X'
        if self.status[coords]:
            return '~'
        return '*'


b_1 = Board()
b_2 = Board()

b_1.fill_boats()
b_2.fill_boats()

b_1.display_board()
print('\n' + '-'*100)
b_2.display_board()