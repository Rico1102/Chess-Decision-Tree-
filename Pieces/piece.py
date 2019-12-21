from Pieces import Bishop, Pawn, Queen, King, Knight, Rook


class piece:
    def __init__(self, present, color='None', type='None'):
        self.present = present
        self.pos_x = 0
        self.pos_y = 0
        self.board_x = 0
        self.board_y = 0
        self.name = 'None'
        self.color = color
        if self.present == False:
            return
        if type == 'B':
            self.name = 'Bishop'
            self.type = Bishop.Bishop(self.color)
        elif type == 'R':
            self.name = 'Rook'
            self.type = Rook.Rook(self.color)
        elif type == 'K':
            self.name = 'King'
            self.type = King.King(self.color)
        elif type == 'N':
            self.name = 'Knight'
            self.type = Knight.Knight(self.color)
        elif type == 'P':
            self.name = 'Pawn'
            self.type = Pawn.Pawn(self.color)
        else:
            self.name = 'Queen'
            self.type = Queen.Queen(self.color)

    def get_moves(self, board, chess_board):
        # print('Coordinates', self.board_x, self.board_y)
        moves = self.type.find_move(board, self.board_x, self.board_y, chess_board)
        fin_moves = []
        for i in moves:
            if i.king_safe(chess_board):
                fin_moves.append(i)
        return fin_moves

    def draw_piece(self, canvas):
        canvas.blit(self.type.img, (self.pos_x, self.pos_y))
