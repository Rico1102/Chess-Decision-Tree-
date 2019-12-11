import pygame


class Move:
    def __init__(self, x_old, y_old, x_new, y_new, board):
        self.x_old = x_old
        self.x_new = x_new
        self.y_old = y_old
        self.y_new = y_new
        self.board = board
        self.type = self.get_type()
        self.valid = self.check_validity
        self.RED = (255, 77, 77)
        self.GREEN = (77, 255, 77)

    def get_type(self):
        if self.board[self.x_new][self.y_new].present == True and self.board[self.x_old][self.y_old].color != \
                self.board[self.x_new][self.y_new].color:
            return 'Capture'
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
        else:
            x = self.y_new * 70 + 20
            y = self.x_new * 70 + 20
            create_rect(x, y, self.RED, canvas)

    def make_move(self, board, pieces):
        if pieces[self.x_new][self.y_new].present:
            board[self.x_new][self.y_new] = '-'
            pieces[self.x_new][self.y_new].present = False
        if board[self.x_old][self.y_old][1] == 'P':
            pieces[self.x_old][self.y_old].type.first_move = False
        board[self.x_old][self.y_old], board[self.x_new][self.y_new] = board[self.x_new][self.y_new], board[self.x_old][
            self.y_old]
        pieces[self.x_old][self.y_old], pieces[self.x_new][self.y_new] = pieces[self.x_new][self.y_new], \
                                                                         pieces[self.x_old][self.y_old]
        return board, pieces


def create_rect(x, y, color, canvas):
    pygame.draw.rect(canvas, color, [x, y, 70, 70])
