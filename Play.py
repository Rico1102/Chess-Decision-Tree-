from Mode import MultiPlayer, SinglePlayer, Online
import pygame


class Menu:
    def __init__(self):
        pygame.init()
        self.board = pygame.display.set_mode((600, 600))
        self.place_buttons()
        self.run()

    def place_buttons(self):
        fontobj = pygame.font.Font('freesansbold.ttf', 20)
        textSurfaceObj = fontobj.render('THANKS FOR USING INDIAN RAILWAYS DATABASE!!!', True, Red)

    def run(self):
        pass


game = SinglePlayer.Game()
