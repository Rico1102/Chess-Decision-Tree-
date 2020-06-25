import pygame
import Images
from Board.Move import Move


class Pawn:
    def __init__(self, color):
        self.color = color
        self.first_move = True
        if color == 'B':
            self.img = Images.load_img.Images.BP
            self.img = pygame.transform.scale(self.img, (70, 70))
        else:
            self.img = Images.load_img.Images.WP
            self.img = pygame.transform.scale(self.img, (70, 70))

    def find_move(self, board, x, y, c_board):
        moves = []
        moves.extend(self.straight_move(board, x, y))
        moves.extend(self.diagonal_move(board, x, y))
        return moves

    def straight_move(self, board, x, y):
        moves = []
        if self.first_move:  # First Pawn Move
            if self.color == 'W':
                if x+2 < 8 and board[x+2][y].present == False and board[x+1][y].present == False:
                    move = Move(x, y, x + 2, y, board)
                    if move.valid:
                        moves.append(move)
            else:
                if x-2 > -1 and board[x-2][y].present == False and board[x-1][y].present == False:
                    move = Move(x, y, x - 2, y, board)
                    if move.valid:
                        moves.append(move)
        if self.color == 'W':
            if x+1 < 8 and board[x+1][y].present == False:
                move = Move(x, y, x + 1, y, board)
                if move.valid:
                    moves.append(move)
        else:
            if x-1 > -1 and board[x-1][y].present == False:
                move = Move(x, y, x - 1, y, board)
                if move.valid:
                    moves.append(move)
        return moves

    def diagonal_move(self, board, x, y):
        moves = []
        if self.color == 'W':
            if x+1 < 8 and y+1 < 8 and board[x+1][y+1].present and board[x+1][y+1].color=='B':
                move = Move(x, y, x + 1, y + 1, board)
                if move.valid:
                    moves.append(move)
        else:
            if x-1 > -1 and y-1 > -1 and board[x-1][y-1].present and board[x-1][y-1].color=='W':
                move = Move(x, y, x - 1, y - 1, board)
                if move.valid:
                    moves.append(move)
        if self.color == 'W':
            if x+1 < 8 and y-1 > -1 and board[x+1][y-1].present and board[x+1][y-1].color=='B':
                move = Move(x, y, x + 1, y - 1, board)
                if move.valid:
                    moves.append(move)
        else:
            if x-1 > -1 and y+1 < 8 and board[x-1][y+1].present and board[x-1][y+1].color=='W':
                move = Move(x, y, x - 1, y + 1, board)
                if move.valid:
                    moves.append(move)
        return moves
