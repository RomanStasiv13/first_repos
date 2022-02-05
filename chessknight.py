class ChessKnight:
    BOARD_SIZE = 8
    DELTA = [(2,1),(1,2),(-1,2),(1,-2),(-1,-2),(2,-1),(-2,1),(-2,-1)]

    def __init__(self, current_pos, finish_pos):
        self.__current_pos = current_pos
        self.__finish_pos = finish_pos
        self.shortest_path_len = 100

    @classmethod
    def valid_moves(cls, x, y):
         return filter(lambda c: 0<= c[0] <cls.BOARD_SIZE and 0<= c[1] <cls.BOARD_SIZE,[(x+xd,y+yd) for xd, yd in cls.DELTA])

    def shortest_path(self, current, path):
        can_go = set(self.valid_moves(*current)) - set(path)
        path.append(current)
        if can_go == set():
            return
        if len(path) >= self.shortest_path_len:
            return
        if self.__finish_pos in can_go:
            self.shortest_path_len = len(path)
            return
        for i in can_go:
            self.shortest_path(i, path[:])


if __name__ == '__main__':
    c = ChessKnight((0,0), (7,7))
    c.shortest_path((0,0),[])
    print(c.shortest_path_len)



