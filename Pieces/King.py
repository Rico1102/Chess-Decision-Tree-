import pygame
from Images.load_img import Images
from Board.Move import Move


class King:
    def __init__(self, color):
        self.color = color
        self.castling = True
        if color == 'B':
            self.img = Images.BK
            self.img = pygame.transform.scale(self.img, (70, 70))
        else:
            self.img = Images.WK
            self.img = pygame.transform.scale(self.img, (70, 70))

    def find_move(self, board, x, y, c_board):
        moves = []
        moves.extend(self.one_step_move(board, x, y))
        moves.extend(self.castling_move(board, x, y))
        return moves

    def one_step_move(self, board, x, y):
        moves = []
        if x + 1 < 8 and (not board[x + 1][y].present or board[x + 1][y].color != self.color):
            move = Move(x, y, x + 1, y, board)
            if move.valid:
                moves.append(move)
        if x - 1 > -1 and (not board[x - 1][y].present or board[x - 1][y].color != self.color):
            move = Move(x, y, x - 1, y, board)
            if move.valid:
                moves.append(move)
        if y + 1 < 8 and (not board[x][y + 1].present or board[x][y + 1].color != self.color):
            move = Move(x, y, x, y + 1, board)
            if move.valid:
                moves.append(move)
        if y - 1 > -1 and (not board[x][y - 1].present or board[x][y - 1].color != self.color):
            move = Move(x, y, x, y - 1, board)
            if move.valid:
                moves.append(move)
        if x + 1 < 8 and y + 1 < 8 and (not board[x + 1][y + 1].present or board[x + 1][y + 1].color != self.color):
            move = Move(x, y, x + 1, y + 1, board)
            if move.valid:
                moves.append(move)
        if x + 1 < 8 and y - 1 > -1 and (not board[x + 1][y - 1].present or board[x + 1][y - 1].color != self.color):
            move = Move(x, y, x + 1, y - 1, board)
            if move.valid:
                moves.append(move)
        if x - 1 > -1 and y + 1 < 8 and (not board[x - 1][y + 1].present or board[x - 1][y + 1].color != self.color):
            move = Move(x, y, x - 1, y + 1, board)
            if move.valid:
                moves.append(move)
        if x - 1 > -1 and y - 1 > -1 and (not board[x - 1][y - 1].present or board[x - 1][y - 1].color != self.color):
            move = Move(x, y, x - 1, y - 1, board)
            if move.valid:
                moves.append(move)
        return moves

    def castling_move(self, board, x, y):
        moves = []
        if self.castling:
            i = 0
            while True:
                i += 1
                if y + i < 8:
                    # print(board[x][y+i].name)
                    if board[x][y + i].present:
                        if board[x][y + i].name != 'Rook':
                            break
                        else:
                            if board[x][y + i].name == 'Rook':
                                if board[x][y + i].type.castling:
                                    # print(board[x][y+i].name, x, y+i, x, y+i-2)
                                    move = Move(x, y, x, y + i, board)
                                    # print(move.valid)
                                    if move.valid:
                                        # print(board[x][y+i].name)
                                        moves.append(move)
                                else:
                                    break
                                break
                else:
                    break
            i = 0
            while True:
                i -= 1
                if y + i < 8:
                    if board[x][y + i].present:
                        if board[x][y + i].name != 'Rook':
                            break
                        else:
                            if board[x][y + i].name == 'Rook':
                                if board[x][y + i].type.castling:
                                    move = Move(x, y, x, y + i, board)
                                    if move.valid:
                                        moves.append(move)
                                else:
                                    break
                                break
                else:
                    break
        return moves
