from figures import Pawn, Rook, Knight, Bishop, King, Queen


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
                      [None] * 8,]

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
        for x in [0,7]:
            self.board[x][0] = Rook('white', x, 0)
            self.board[x][7] = Rook('black', x, 7)

    def setup_knights(self):
        for x in [1,6]:
            self.board[x][0] = Knight('white', x, 0)
            self.board[x][7] = Knight('black', x, 7)

    def setup_bishop(self):
        for x in [2,5]:
            self.board[x][0] = Bishop('white', x, 0)
            self.board[x][7] = Bishop('black', x, 7)

    def setup_kings(self):
        self.board[4][0] = King('white', 4, 0)
        self.board[4][7] = King('black', 4, 7)

    def setup_queen(self):
        self.board[3][0] = Queen('white', 3, 0)
        self.board[3][7] = Queen('black', 3, 7)