import pygame
from Board import states
from Pieces import piece


class Move:
    def __init__(self, x_old, y_old, x_new, y_new, board, offline=True):
        self.x_old = x_old
        self.x_new = x_new
        self.y_old = y_old
        self.y_new = y_new
        self.board = board
        self.type = self.get_type()
        if offline:
            self.valid = self.check_validity()
        else:
            self.valid = True
        self.RED = (255, 77, 77)
        self.GREEN = (77, 255, 77)
        self.VIOLET = (153, 51, 153)

    def create_rect(self , x, y, color, canvas):
        pygame.draw.rect(canvas, color, [x + 5, y + 5, 60, 60])

    def copy(self, p):
        if p.name == 'Knight':
            N = 'N'
        else:
            N = p.name[0]
        q = piece.piece(p.present, p.color, N)
        q.board_x = p.board_x
        q.board_y = p.board_y
        q.pos_x = p.pos_x
        q.pos_y = p.pos_y
        if p.present and p.name == 'Pawn':
            q.type.first_move = (True and p.type.first_move)
        elif (p.name == 'Rook' or p.name == 'King') and p.present:
            q.type.castling = p.type.castling
        return q

    def copy_piece(self):
        p1 = self.copy(self.board[self.x_old][self.y_old])
        p2 = self.copy(self.board[self.x_new][self.y_new])
        return p1, p2

    def king_safe(self, chess_board):
        status = False
        p1, p2 = self.copy_piece()
        x1, y1, x2, y2 = self.x_old, self.y_old, self.x_new, self.y_new
        color = self.board[self.x_old][self.y_old].color
        chess_board, self.board = self.make_move(chess_board, self.board)
        st = states.States(self.board)
        status = st.check_condition(color)
        status = not status
        self.x_old, self.y_old, self.x_new, self.y_new = x1, y1, x2, y2
        chess_board, self.board = self.undo_move(chess_board, self.board, p1, p2)
        return status

    def get_type(self):
        if self.board[self.x_old][self.y_old].name == 'Pawn' and (self.x_new == 0 or self.x_new == 7):
            return 'Revival'
        elif self.board[self.x_new][self.y_new].present == True and self.board[self.x_old][self.y_old].color != \
                self.board[self.x_new][self.y_new].color:
            return 'Capture'
        elif self.board[self.x_new][self.y_new].present == True and self.board[self.x_old][self.y_old].color == \
                self.board[self.x_new][self.y_new].color and (self.board[self.x_old][self.y_old].name == 'King' or self.board[self.x_old][self.y_old].name == 'Rook'):
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
            self.create_rect(x, y, self.GREEN, canvas)
        elif self.type == 'Castling' or self.type == 'Revival':
            x = self.y_new * 70 + 20
            y = self.x_new * 70 + 20
            self.create_rect(x, y, self.VIOLET, canvas)
        else:
            x = self.y_new * 70 + 20
            y = self.x_new * 70 + 20
            self.create_rect(x, y, self.RED, canvas)

    def make_move(self, board, pieces):
        if pieces[self.x_old][self.y_old].present and pieces[self.x_old][self.y_old].name == 'Pawn':
            pieces[self.x_old][self.y_old].type.first_move = False
        if pieces[self.x_old][self.y_old].present and pieces[self.x_old][self.y_old].name == 'Rook':
            pieces[self.x_old][self.y_old].type.castling = False
        if pieces[self.x_old][self.y_old].present and pieces[self.x_old][self.y_old].name == 'King':
            pieces[self.x_old][self.y_old].type.castling = False
        if self.type == 'Normal':
            board[self.x_old][self.y_old], board[self.x_new][self.y_new] = board[self.x_new][self.y_new], \
                                                                           board[self.x_old][
                                                                               self.y_old]
            pieces[self.x_old][self.y_old], pieces[self.x_new][self.y_new] = pieces[self.x_new][self.y_new], \
                                                                             pieces[self.x_old][self.y_old]
            pieces[self.x_old][self.y_old].board_x, pieces[self.x_old][self.y_old].board_y = self.x_old, self.y_old
            pieces[self.x_new][self.y_new].board_x, pieces[self.x_new][self.y_new].board_y = self.x_new, self.y_new
        elif self.type == 'Castling':
            t_ox, t_nx = self.x_old, self.x_new
            t_oy, t_ny = self.y_old, self.y_new
            if pieces[self.x_old][self.y_old].name == 'King':
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
            board[self.x_old][self.y_old], board[self.x_new][self.y_new] = board[self.x_new][self.y_new], \
                                                                           board[self.x_old][
                                                                               self.y_old]
            pieces[self.x_old][self.y_old], pieces[self.x_new][self.y_new] = pieces[self.x_new][self.y_new], \
                                                                             pieces[self.x_old][self.y_old]
            self.x_old = x2
            self.y_old = y2
            self.x_new = x2
            self.y_new = y2 + b
            board[self.x_old][self.y_old], board[self.x_new][self.y_new] = board[self.x_new][self.y_new], \
                                                                           board[self.x_old][
                                                                               self.y_old]
            pieces[self.x_old][self.y_old], pieces[self.x_new][self.y_new] = pieces[self.x_new][self.y_new], \
                                                                             pieces[self.x_old][self.y_old]
            self.x_old, self.y_old, self.x_new, self.y_new = t_ox, t_oy, t_nx, t_ny
            pieces[self.x_old][self.y_old].board_x, pieces[self.x_old][self.y_old].board_y = x2, y2 + a
            pieces[self.x_new][self.y_new].board_x, pieces[self.x_new][self.y_new].board_y = x2, y2 + b
        elif self.type == 'Capture':
            board[self.x_new][self.y_new] = '_'
            pieces[self.x_new][self.y_new] = piece.piece(False)
            board[self.x_old][self.y_old], board[self.x_new][self.y_new] = board[self.x_new][self.y_new], \
                                                                           board[self.x_old][
                                                                               self.y_old]
            pieces[self.x_old][self.y_old], pieces[self.x_new][self.y_new] = pieces[self.x_new][self.y_new], \
                                                                             pieces[self.x_old][self.y_old]
            pieces[self.x_old][self.y_old].board_x, pieces[self.x_old][self.y_old].board_y = self.x_old, self.y_old
            pieces[self.x_new][self.y_new].board_x, pieces[self.x_new][self.y_new].board_y = self.x_new, self.y_new
        elif self.type == 'Revival':
            board[self.x_new][self.y_new] = '_'
            pieces[self.x_new][self.y_new].present = piece.piece(False)
            board[self.x_old][self.y_old], board[self.x_new][self.y_new] = board[self.x_new][self.y_new], \
                                                                           board[self.x_old][
                                                                               self.y_old]
            pieces[self.x_old][self.y_old], pieces[self.x_new][self.y_new] = pieces[self.x_new][self.y_new], \
                                                                             pieces[self.x_old][self.y_old]
            board[self.x_new][self.y_new] = board[self.x_new][self.y_new][0] + 'Q'
            pieces[self.x_new][self.y_new] = piece.piece(True, board[self.x_new][self.y_new][0], 'Q')
            pieces[self.x_old][self.y_old].board_x, pieces[self.x_old][self.y_old].board_y = self.x_old, self.y_old
            pieces[self.x_new][self.y_new].board_x, pieces[self.x_new][self.y_new].board_y = self.x_new, self.y_new
        return board, pieces

    def undo_move(self, board, pieces, p1, p2):
        if self.type == 'Castling':
            pieces[self.x_old][self.y_old] = p1
            pieces[self.x_new][self.y_new] = p2
            board[self.x_old][self.y_old] = p1.color + p1.name[0]
            board[self.x_old][self.y_old] = p1.color + p1.name[0]
            if self.y_old < self.y_new:
                for i in range(1, 8):
                    if self.y_old + i == self.y_new:
                        break
                    else:
                        pieces[self.x_old][self.y_old + i] = piece.piece(False)
                        board[self.x_old][self.y_old+i] = '_'
            else:
                for i in range(1, 8):
                    if self.y_new + i == self.y_old:
                        break
                    else:
                        pieces[self.x_old][self.y_new+i] = piece.piece(False)
                        board[self.x_old][self.y_new+i] = '_'
        else:
            pieces[self.x_old][self.y_old] = p1
            pieces[self.x_new][self.y_new] = p2
            if p1.name == 'Knight':
                board[self.x_old][self.y_old] = p1.color + 'N'
            else:
                board[self.x_old][self.y_old] = p1.color + p1.name[0]
            if p2.present:
                if p1.name == 'Knight':
                    board[self.x_old][self.y_old] = p2.color + 'N'
                else:
                    board[self.x_old][self.y_old] = p2.color + p2.name[0]
            else:
                board[self.x_new][self.y_new] = '_'
        return board, pieces

