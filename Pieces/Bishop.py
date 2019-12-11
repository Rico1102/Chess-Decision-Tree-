import pygame
from Images.load_img import Images


class Bishop:
    def __init__(self, color):
        self.color = color
        if color == 'B':
            self.img = Images.BB
            self.img = pygame.transform.scale(self.img, (70, 70))
        else:
            self.img = Images.WB
            self.img = pygame.transform.scale(self.img, (70, 70))

    def find_move(self, board, x, y):
        pass
