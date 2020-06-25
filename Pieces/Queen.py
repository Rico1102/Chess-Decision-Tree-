import pygame
import Images
from Pieces import piece


class Queen:
    def __init__(self, color):
        self.color = color
        if color == 'B':
            self.img = Images.load_img.Images.BQ
            self.img = pygame.transform.scale(self.img, (70, 70))
        else:
            self.img = Images.load_img.Images.WQ
            self.img = pygame.transform.scale(self.img, (70, 70))

    def find_move(self, board, x, y, c_board):
        moves = []
        moves.extend(self.get_rook_moves(board, x, y, c_board))
        moves.extend(self.get_bishop_moves(board, x, y, c_board))
        return moves

    def get_rook_moves(self, board, x, y, c_board):
        moves = []
        rook = piece.piece(True, self.color, 'R')
        rook.type.castling = False
        rook.board_x = x
        rook.board_y = y
        moves.extend(rook.get_moves(board, c_board))
        return moves

    def get_bishop_moves(self, board, x, y, c_board):
        moves = []
        bishop = piece.piece(True, self.color, 'B')
        bishop.board_x = x
        bishop.board_y = y
        moves.extend(bishop.get_moves(board, c_board))
        return moves
