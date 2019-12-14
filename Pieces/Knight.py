import pygame
from Images.load_img import Images
from Board.Move import Move


class Knight:
    def __init__(self, color):
        self.color = color
        if color == 'B':
            self.img = Images.BN
            self.img = pygame.transform.scale(self.img, (70, 70))
        else:
            self.img = Images.WN
            self.img = pygame.transform.scale(self.img, (70, 70))

    def find_move(self, board, x, y, c_board):
        moves = []
        moves.extend(self.capture_moves(board, x, y))
        moves.extend(self.normal_moves(board, x, y))
        return moves

    def capture_moves(self, board, x, y):
        moves = []
        if x-1 > -1 and y-2 > -1 and board[x-1][y-2].present and board[x-1][y-2].color != self.color:
            move = Move(x, y, x-1, y-2, board)
            if move.valid:
                moves.append(move)
        if x+1 < 8 and y-2 > -1 and board[x+1][y-2].present and board[x+1][y-2].color != self.color:
            move = Move(x, y, x+1, y-2, board)
            if move.valid:
                moves.append(move)
        if x+2 < 8 and y-1 > -1 and board[x+2][y-1].present and board[x+2][y-1].color != self.color:
            move = Move(x, y, x+2, y-1, board)
            if move.valid:
                moves.append(move)
        if x+2 < 8 and y+1 < 8 and board[x+2][y+1].present and board[x+2][y+1].color != self.color:
            move = Move(x, y, x+2, y+1, board)
            if move.valid:
                moves.append(move)
        if x-1 > -1 and y+2 < 8 and board[x-1][y+2].present and board[x-1][y+2].color != self.color:
            move = Move(x, y, x-1, y+2, board)
            if move.valid:
                moves.append(move)
        if x+1 < 8 and y+2 < 8 and board[x+1][y+2].present and board[x+1][y+2].color != self.color:
            move = Move(x, y, x+1, y+2, board)
            if move.valid:
                moves.append(move)
        if x-2 > -1 and y-1 > -1 and board[x-2][y-1].present and board[x-2][y-1].color != self.color:
            move = Move(x, y, x-2, y-1, board)
            if move.valid:
                moves.append(move)
        if x-2 > -1 and y+1 < 8 and board[x-2][y+1].present and board[x-2][y+1].color != self.color:
            move = Move(x, y, x-2, y+1, board)
            if move.valid:
                moves.append(move)
        return moves

    def normal_moves(self, board, x, y):
        moves = []
        if x-1 > -1 and y-2 > -1 and board[x-1][y-2].present == False:
            move = Move(x, y, x-1, y-2, board)
            if move.valid:
                moves.append(move)
        if x+1 < 8 and y-2 > -1 and board[x+1][y-2].present == False:
            move = Move(x, y, x+1, y-2, board)
            if move.valid:
                moves.append(move)
        if x+2 < 8 and y-1 > -1 and board[x+2][y-1].present == False:
            move = Move(x, y, x+2, y-1, board)
            if move.valid:
                moves.append(move)
        if x+2 < 8 and y+1 < 8 and board[x+2][y+1].present == False:
            move = Move(x, y, x+2, y+1, board)
            if move.valid:
                moves.append(move)
        if x-1 > -1 and y+2 < 8 and board[x-1][y+2].present == False:
            move = Move(x, y, x-1, y+2, board)
            if move.valid:
                moves.append(move)
        if x+1 < 8 and y+2 < 8 and board[x+1][y+2].present == False:
            move = Move(x, y, x+1, y+2, board)
            if move.valid:
                moves.append(move)
        if x-2 > -1 and y-1 > -1 and board[x-2][y-1].present == False:
            move = Move(x, y, x-2, y-1, board)
            if move.valid:
                moves.append(move)
        if x-2 > -1 and y+1 < 8 and board[x-2][y+1].present == False:
            move = Move(x, y, x-2, y+1, board)
            if move.valid:
                moves.append(move)
        return moves
