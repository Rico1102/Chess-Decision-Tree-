import pygame
from Images.load_img import Images
from Board.Move import Move
from Pieces import King


class Rook:
    def __init__(self, color):
        self.color = color
        self.castling = True
        if color == 'B':
            self.img = Images.BR
            self.img = pygame.transform.scale(self.img , (70 , 70))
        else:
            self.img = Images.WR
            self.img = pygame.transform.scale(self.img , (70 , 70))


    def find_move(self, board, x, y, c_board):
        moves = []
        moves.extend(self.horizontal_mov(board, x, y))
        moves.extend(self.vertical_mov(board, x, y))
        moves.extend(self.castling_mov(board, x, y))
        return moves

    def horizontal_mov(self, board, x, y):
        moves = []
        i = 0
        while True:
            i += 1
            if x+i < 8:
                if board[x+i][y].present:
                    if board[x+i][y].color == self.color:
                        break
                    else:
                        move = Move(x, y, x+i, y, board)
                        if move.valid:
                            moves.append(move)
                        break
                else:
                    move = Move(x, y, x+i, y, board)
                    if move.valid:
                        moves.append(move)
            else:
                break
        i = 0
        while True:
            i -= 1
            if x+i > -1:
                if board[x+i][y].present:
                    if board[x+i][y].color == self.color:
                        break
                    else:
                        move = Move(x, y, x+i, y, board)
                        if move.valid:
                            moves.append(move)
                        break
                else:
                    move = Move(x, y, x+i, y, board)
                    if move.valid:
                        moves.append(move)
            else:
                break
        return moves

    def vertical_mov(self, board, x, y):
        moves = []
        i = 0
        while True:
            i += 1
            if y+i < 8:
                if board[x][y+i].present:
                    if board[x][y+i].color == self.color:
                        break
                    else:
                        move = Move(x, y, x, y+i, board)
                        if move.valid:
                            moves.append(move)
                        break
                else:
                    move = Move(x, y, x, y+i, board)
                    if move.valid:
                        moves.append(move)
            else:
                break
        i = 0
        while True:
            i -= 1
            if y+i > -1:
                if board[x][y+i].present:
                    if board[x][y+i].color == self.color:
                        break
                    else:
                        move = Move(x, y, x, y+i, board)
                        if move.valid:
                            moves.append(move)
                        break
                else:
                    move = Move(x, y, x, y+i, board)
                    if move.valid:
                        moves.append(move)
            else:
                break
        return moves

    def castling_mov(self, board, x, y):
        moves = []
        if self.castling:
            i = 0
            while True:
                i += 1
                if y+i < 8:
                    if board[x][y+i].present:
                        if board[x][y+i].name != 'King':
                            break
                        else:
                            if board[x][y+i].name == 'King':
                                if board[x][y+i].type.castling:
                                    move = Move(x, y, x, y+i, board)
                                    if move.valid:
                                        moves.append(move)
                                else:
                                    break
                                break
                else:
                    break
            i = 0
            while True:
                i -= 1
                if y+i < 8:
                    if board[x][y+i].present:
                        if board[x][y+i].name != 'King':
                            break
                        else:
                            if board[x][y+i].name == 'King':
                                if board[x][y+i].type.castling:
                                    move = Move(x, y, x, y+i, board)
                                    if move.valid:
                                        moves.append(move)                                
                                else:
                                    break
                                break
                else:
                    break
        return moves
