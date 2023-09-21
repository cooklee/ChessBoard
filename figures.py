class Figure:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def move(self, x, y):
        self.moved = True
        self.x = x
        self.y = y

    def check_moves(self, moves):
        return [move for move in moves if move[0] >= 0 and move[0] <= 7 and move[1] >= 0 and move[1] <= 7]

    def _get_diagonal_moves(self, chessboard):
        moves = []
        jump = 1
        while self.x + jump <= 7 and self.y + jump <= 7:
            moves.append((self.x + jump, self.y + jump))
            jump += 1
        jump = 1
        while self.x + jump <= 7 and self.y - jump >= 0:
            moves.append((self.x + jump, self.y - jump))
            jump += 1
        jump = 1
        while self.x - jump >= 0 and self.y + jump <= 7:
            moves.append((self.x - jump, self.y + jump))
            jump += 1
        jump = 1
        while self.x - jump >= 0 and self.y - jump >= 0:
            moves.append((self.x - jump, self.y - jump))
            jump += 1
        return moves

    def _get_horizontal_and_vertical_moves(self, chessboard):
        moves = []
        jump = 1
        while self.x + jump <= 7:
            moves.append((self.x + jump, self.y))
            jump += 1
        jump = 1
        while self.x - jump >= 0:
            moves.append((self.x - jump, self.y))
            jump += 1
        jump = 1
        while self.y + jump <= 7:
            moves.append((self.x, self.y + jump))
            jump += 1
        jump = 1
        while self.y - jump >= 0:
            moves.append((self.x, self.y - jump))
            jump += 1
        return moves

class Pawn(Figure):

    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.moved = False

    def list_allowed_moves(self, chessboard):

        moves = []
        if self.color == 'white':
            if self.y == 7:
                return []
            moves.append((self.x, self.y + 1))
            if not self.moved:
                moves.append((self.x, self.y + 2))
        else:
            if self.y == 0:
                return []
            moves.append((self.x, self.y - 1))
            if not self.moved:
                moves.append((self.x, self.y - 2))
        return self.check_moves(moves)


class Knight(Figure):

    def list_allowed_moves(self, chessboard):
        moves = []
        for i in [1, -1]:
            for j in [2, -2]:
                moves.append((self.x + i, self.y + j))
                moves.append((self.x + j, self.y + i))
        return self.check_moves(moves)


class Rook(Figure):

    def list_allowed_moves(self, chessboard):
        return self.check_moves(self._get_horizontal_and_vertical_moves(chessboard))


class Bishop(Figure):
    def list_allowed_moves(self, chessboard):
        return self.check_moves(self._get_diagonal_moves(chessboard))


class Queen(Figure):
    def list_allowed_moves(self, chessboard):
        moves = self._get_horizontal_and_vertical_moves(chessboard)
        moves.extend(self._get_diagonal_moves(chessboard))
        return self.check_moves(moves)



class King(Figure):

    def list_allowed_moves(self, chessboard):
        moves = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                moves.append((self.x + i, self.y + j))

        return self.check_moves(moves)




def drow_chessbard(f):
    for j in range(7,-1,-1):
        for i in range(0,8):
            if (i, j) in f.list_allowed_moves(None):
                print('x', end='')
            elif i == f.x and j == f.y:
                print('o', end='')
            else:
                print(' ', end='')
        print()

b = Queen(123, 5, 5)
for x in b.list_allowed_moves(12):
    print(x)
drow_chessbard(b)