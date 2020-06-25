import pygame
import os


class Images:
    current_path = os.path.dirname(__file__)
    pygame.init()
    temp = pygame.display.set_mode((0, 0))
    BB = pygame.image.load(os.path.join(current_path, "BB.png")).convert_alpha()
    BP = pygame.image.load(os.path.join(current_path, "BP.png")).convert_alpha()
    BK = pygame.image.load(os.path.join(current_path, "BK.png")).convert_alpha()
    BQ = pygame.image.load(os.path.join(current_path, "BQ.png")).convert_alpha()
    BR = pygame.image.load(os.path.join(current_path, "BR.png")).convert_alpha()
    BN = pygame.image.load(os.path.join(current_path, "BN.png")).convert_alpha()
    WB = pygame.image.load(os.path.join(current_path, "WB.png")).convert_alpha()
    WP = pygame.image.load(os.path.join(current_path, "WP.png")).convert_alpha()
    WK = pygame.image.load(os.path.join(current_path, "WK.png")).convert_alpha()
    WQ = pygame.image.load(os.path.join(current_path, "WQ.png")).convert_alpha()
    WR = pygame.image.load(os.path.join(current_path, "WR.png")).convert_alpha()
    WN = pygame.image.load(os.path.join(current_path, "WN.png")).convert_alpha()
    pygame.quit()
