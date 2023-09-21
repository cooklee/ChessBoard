class Figure:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

    def check_if_moves_are_in_board(self, x, y):
        return x >= 0 and x <= 7 and y >= 0 and y <= 7

    def remove_moves_out_of_board(self, moves):
        return [move for move in moves if move[0] >= 0 and move[1] >= 0 and move[0] <= 7 and move[1] <= 7]

    def _get_diagonal_moves(self, chessboard):
        moves = []
        jump = 1
        while self.x + jump <= 7 and self.y + jump <= 7:
            x = self.x + jump
            y = self.y + jump
            if not self.check_if_moves_are_in_board(x, y):
                break
            if chessboard.board[x][y] is not None:
                if chessboard.board[x][y].color != self.color:
                    moves.append((x, y))
                break
            moves.append((x, y))
            jump += 1
        jump = 1
        while self.x + jump <= 7 and self.y - jump >= 0:
            x = self.x + jump
            y = self.y - jump
            if not self.check_if_moves_are_in_board(x, y):
                break
            if chessboard.board[x][y] is not None:
                if chessboard.board[x][y].color != self.color:
                    moves.append((x, y))
                break
            moves.append((x, y))
            jump += 1
        jump = 1
        while self.x - jump >= 0 and self.y + jump <= 7:
            x = self.x - jump
            y = self.y + jump
            if not self.check_if_moves_are_in_board(x, y):
                break
            if chessboard.board[x][y] is not None:
                if chessboard.board[x][y].color != self.color:
                    moves.append((x, y))
                break
            moves.append((x, y))
            jump += 1
        jump = 1
        while self.x - jump >= 0 and self.y - jump >= 0:
            x = self.x - jump
            y = self.y - jump
            if not self.check_if_moves_are_in_board(x, y):
                break
            if chessboard.board[x][y] is not None:
                if chessboard.board[x][y].color != self.color:
                    moves.append((x, y))
                break
            moves.append((x, y))
            jump += 1
        return self.remove_moves_out_of_board(moves)

    def _get_horizontal_and_vertical_moves(self, chessboard):
        moves = []
        jump = 1
        y = self.y
        while self.x + jump <= 7:
            x = self.x + jump
            if chessboard.board[x][y] is not None:
                if chessboard.board[x][y].color != self.color:
                    moves.append((x, y))
                break
            moves.append((x, y))
            jump += 1
        jump = 1
        while self.x - jump >= 0:
            x = self.x - jump
            if chessboard.board[x][y] is not None:
                if chessboard.board[x][y].color != self.color:
                    moves.append((x, y))
                break
            moves.append((x, y))
            jump += 1
        jump = 1
        x = self.x
        while self.y + jump <= 7:
            y = self.y + jump
            if chessboard.board[x][y] is not None:
                if chessboard.board[x][y].color != self.color:
                    moves.append((x, y))
                break
            moves.append((x, y))
            jump += 1
        jump = 1
        while self.y - jump >= 0:
            y = self.y - jump
            if chessboard.board[x][y] is not None:
                if chessboard.board[x][y].color != self.color:
                    moves.append((x, y))
                break
            moves.append((x, y))
            jump += 1
        return self.remove_moves_out_of_board(moves)


class Pawn(Figure):

    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.moved = False
        self.c = 'p'

    def move(self, x, y):
        super().move(x, y)
        self.moved = True

    def list_allowed_moves(self, chessboard):

        moves = []

        if self.color == 'white':
            jump = 1
        else:
            jump = -1
        if self.moved:
            steps = [1]
        else:
            steps = [1,2]

        for step in steps:
            x = self.x
            y = self.y + step * jump
            if not self.check_if_moves_are_in_board(x, y):
                break
            if chessboard.board[x][y] is None:
                moves.append((x, y))
            else:
                break
        for step in (-1, 1):
            y = self.y + jump
            x = self.x + step
            if not self.check_if_moves_are_in_board(x, y):
                continue
            figure = chessboard.board[x][y]
            if figure is not None and figure.color != self.color:
                moves.append((x, y))

        return self.remove_moves_out_of_board(moves)


class Knight(Figure):

    def list_allowed_moves(self, chessboard):
        moves = []
        for i in [1, -1]:
            for j in [2, -2]:
                x = self.x + i
                y = self.y + j
                if not self.check_if_moves_are_in_board(x, y):
                    continue
                if chessboard.board[x][y] is None or chessboard.board[x][y].color != self.color:
                    moves.append((x, y))
                x = self.x + j
                y = self.y + i
                if not self.check_if_moves_are_in_board(x, y):
                    continue
                if chessboard.board[x][y] is None or chessboard.board[x][y].color != self.color:
                    moves.append((x, y))
        return self.remove_moves_out_of_board(moves)


class Rook(Figure):

    def list_allowed_moves(self, chessboard):
        return self.remove_moves_out_of_board(self._get_horizontal_and_vertical_moves(chessboard))


class Bishop(Figure):
    def list_allowed_moves(self, chessboard):
        return self.remove_moves_out_of_board(self._get_diagonal_moves(chessboard))


class Queen(Figure):
    def list_allowed_moves(self, chessboard):
        moves = self._get_horizontal_and_vertical_moves(chessboard)
        moves.extend(self._get_diagonal_moves(chessboard))
        return self.remove_moves_out_of_board(moves)


class King(Figure):

    def list_allowed_moves(self, chessboard):
        moves = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                x = self.x + i
                y = self.y + j
                if not self.check_if_moves_are_in_board(x, y):
                    continue
                if chessboard.board[x][y] is not None and chessboard.board[x][y].color == self.color:
                    continue
                moves.append((self.x + i, self.y + j))

        return self.remove_moves_out_of_board(moves)


class Chessboard:

    def __init__(self, color='white'):
        self.color = color
        self.board = [[None] * 8,
                      [None] * 8,
                      [None] * 8,
                      [None] * 8,
                      [None] * 8,
                      [None] * 8,
                      [None] * 8,
                      [None] * 8, ]

    def setup(self):
        self.setup_pawns()
        self.setup_rooks()
        self.setup_bishop()
        self.setup_knights()
        self.setup_kings()
        self.setup_queen()

    def setup_pawns(self):
        for x in range(8):
            self.board[x][1] = Pawn('white', x, 1)

        for x in range(8):
            self.board[x][6] = Pawn('black', x, 6)

    def setup_rooks(self):
        for x in [0, 7]:
            self.board[x][0] = Rook('white', x, 0)
            self.board[x][7] = Rook('black', x, 7)

    def setup_knights(self):
        for x in [1, 6]:
            self.board[x][0] = Knight('white', x, 0)
            self.board[x][7] = Knight('black', x, 7)

    def setup_bishop(self):
        for x in [2, 5]:
            self.board[x][0] = Bishop('white', x, 0)
            self.board[x][7] = Bishop('black', x, 7)

    def setup_kings(self):
        self.board[4][0] = King('white', 4, 0)
        self.board[4][7] = King('black', 4, 7)

    def setup_queen(self):
        self.board[3][0] = Queen('white', 3, 0)
        self.board[3][7] = Queen('black', 3, 7)

    def list_allowed_moves(self, x, y):
        figure = self.board[x][y]
        if figure is None or figure.color != self.color:
            return []
        return figure.list_allowed_moves(self)

    def move(self, from_x, from_y, to_x, to_y):
        figure = self.board[from_x][from_y]
        figure_to = self.board[to_x][to_y]
        if figure_to is not None and figure.color != figure_to.color and type(figure_to) is King:
            return f"{figure.color} WON".upper()
        if (to_x, to_y) not in self.list_allowed_moves(from_x, from_y):
            raise ValueError('Nieprawidłowy ruch')
        figure.move(to_x, to_y)
        self.board[to_x][to_y] = figure
        self.board[from_x][from_y] = None
        if self.color == 'white':
            self.color = 'black'
        else:
            self.color = 'white'
