import pygame
from Pieces import piece


class Move:
    def __init__(self, x_old, y_old, x_new, y_new, board):
        self.x_old = x_old
        self.x_new = x_new
        self.y_old = y_old
        self.y_new = y_new
        self.board = board
        self.type = self.get_type()
        self.valid = self.check_validity()
        self.RED = (255, 77, 77)
        self.GREEN = (77, 255, 77)
        self.VIOLET = (153, 51, 153)

    def get_type(self):
        if self.board[self.x_old][self.y_old].name == 'Pawn' and (self.x_new == 0 or self.x_new == 7):
            return 'Revival'
        elif self.board[self.x_new][self.y_new].present == True and self.board[self.x_old][self.y_old].color != \
                self.board[self.x_new][self.y_new].color:
            return 'Capture'
        elif self.board[self.x_new][self.y_new].present == True and self.board[self.x_old][self.y_old].color == \
                self.board[self.x_new][self.y_new].color:
            return 'Castling'
        return 'Normal'

    def check_validity(self):
        if self.x_new > 7 or self.x_new < 0:
            return False
        if self.x_old > 7 or self.x_old < 0:
            return False
        if self.y_new > 7 or self.y_new < 0:
            return False
        if self.y_old > 7 or self.y_old < 0:
            return False
        return True

    def show_move(self, canvas):
        if self.type == 'Normal':
            x = self.y_new * 70 + 20
            y = self.x_new * 70 + 20
            create_rect(x, y, self.GREEN, canvas)
        elif self.type == 'Castling' or self.type == 'Revival':
            x = self.y_new * 70 + 20
            y = self.x_new * 70 + 20
            create_rect(x, y, self.VIOLET, canvas)
        else:
            x = self.y_new * 70 + 20
            y = self.x_new * 70 + 20
            create_rect(x, y, self.RED, canvas)

    def make_move(self, board, pieces):
        print(self.type)
        if board[self.x_old][self.y_old][1] == 'P':
            pieces[self.x_old][self.y_old].type.first_move = False
        if board[self.x_old][self.y_old][1] == 'R':
            pieces[self.x_old][self.y_old].type.castling = False
        if board[self.x_old][self.y_old][1] == 'K':
            pieces[self.x_old][self.y_old].type.castling = False
        if self.type == 'Normal':
            board[self.x_old][self.y_old], board[self.x_new][self.y_new] = board[self.x_new][self.y_new], board[self.x_old][
                self.y_old]
            pieces[self.x_old][self.y_old], pieces[self.x_new][self.y_new] = pieces[self.x_new][self.y_new], \
                                                                             pieces[self.x_old][self.y_old]
        elif self.type == 'Castling':
            if board[self.x_old][self.y_old][1] == 'K':
                self.x_old, self.x_new = self.x_new, self.x_old
                self.y_old, self.y_new = self.y_new, self.y_old
            x1 = self.x_old
            y1 = self.y_old
            x2 = self.x_new
            y2 = self.y_new
            pieces[x2][y2].type.castling = False
            a = 0
            b = 0
            if y1 < y2:
                a -= 1
                b -= 2
            else:
                a += 1
                b += 2
            self.x_old = x1
            self.y_old = y1
            self.x_new = x2
            self.y_new = y2 + a
            board[self.x_old][self.y_old], board[self.x_new][self.y_new] = board[self.x_new][self.y_new], board[self.x_old][
                self.y_old]
            pieces[self.x_old][self.y_old], pieces[self.x_new][self.y_new] = pieces[self.x_new][self.y_new], pieces[self.x_old][self.y_old]
            self.x_old = x2
            self.y_old = y2
            self.x_new = x2
            self.y_new = y2 + b
            board[self.x_old][self.y_old], board[self.x_new][self.y_new] = board[self.x_new][self.y_new], board[self.x_old][
                self.y_old]
            pieces[self.x_old][self.y_old], pieces[self.x_new][self.y_new] = pieces[self.x_new][self.y_new], pieces[self.x_old][self.y_old]

        elif self.type == 'Capture':
            board[self.x_new][self.y_new] = '-'
            pieces[self.x_new][self.y_new].present = False
            board[self.x_old][self.y_old], board[self.x_new][self.y_new] = board[self.x_new][self.y_new], board[self.x_old][
                self.y_old]
            pieces[self.x_old][self.y_old], pieces[self.x_new][self.y_new] = pieces[self.x_new][self.y_new], \
                                                                             pieces[self.x_old][self.y_old]
        elif self.type == 'Revival':
            board[self.x_new][self.y_new] = '-'
            pieces[self.x_new][self.y_new].present = False
            board[self.x_old][self.y_old], board[self.x_new][self.y_new] = board[self.x_new][self.y_new], board[self.x_old][
                self.y_old]
            pieces[self.x_old][self.y_old], pieces[self.x_new][self.y_new] = pieces[self.x_new][self.y_new], \
                                                                             pieces[self.x_old][self.y_old]
            board[self.x_new][self.y_new] = board[self.x_new][self.y_new][0] +'Q'
            pieces[self.x_new][self.y_new] = piece.piece(True, board[self.x_new][self.y_new][0], 'Q')
        return board, pieces


def create_rect(x, y, color, canvas):
    pygame.draw.rect(canvas, color, [x+5, y+5, 60, 60])
