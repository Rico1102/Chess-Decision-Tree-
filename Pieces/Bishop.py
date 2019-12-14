import pygame
from Images.load_img import Images
from Board.Move import Move


class Bishop:
    def __init__(self, color):
        self.color = color
        if color == 'B':
            self.img = Images.BB
            self.img = pygame.transform.scale(self.img, (70, 70))
        else:
            self.img = Images.WB
            self.img = pygame.transform.scale(self.img, (70, 70))

    def find_move(self, board, x, y, c_board):
        moves = []
        moves.extend(self.pri_diagonal(board, x, y))
        moves.extend(self.sec_diagonal(board, x, y))
        return moves

    def pri_diagonal(self, board, x, y):
        moves = []
        i = 0
        while True:
            i += 1
            if x+i < 8 and y+i < 8:
                if board[x+i][y+i].present:
                    if board[x+i][y+i].color == self.color:
                        break
                    else:
                        move = Move(x, y, x+i, y+i, board)
                        if move.valid:
                            moves.append(move)
                        break
                else:
                    move = Move(x, y, x+i, y+i, board)
                    if move.valid:
                        moves.append(move)
            else:
                break
        i = 0
        while True:
            i -= 1
            if x+i > -1 and y+i > -1:
                if board[x+i][y+i].present:
                    if board[x+i][y+i].color == self.color:
                        break
                    else:
                        move = Move(x, y, x+i, y+i, board)
                        if move.valid:
                            moves.append(move)
                        break
                else:
                    move = Move(x, y, x+i, y+i, board)
                    if move.valid:
                        moves.append(move)
            else:
                break
        return moves

    def sec_diagonal(self, board, x, y):
        moves = []
        i = 0
        while True:
            i += 1
            if x+i < 8 and y-i > -1:
                if board[x+i][y-i].present:
                    if board[x+i][y-i].color == self.color:
                        break
                    else:
                        move = Move(x, y, x+i, y-i, board)
                        if move.valid:
                            moves.append(move)
                        break
                else:
                    move = Move(x, y, x+i, y-i, board)
                    if move.valid:
                        moves.append(move)
            else:
                break
        i = 0
        while True:
            i -= 1
            if x+i > -1 and y-i < 8:
                if board[x+i][y-i].present:
                    if board[x+i][y-i].color == self.color:
                        break
                    else:
                        move = Move(x, y, x+i, y-i, board)
                        if move.valid:
                            moves.append(move)
                        break
                else:
                    move = Move(x, y, x+i, y-i, board)
                    if move.valid:
                        moves.append(move)
            else:
                break
        return moves
