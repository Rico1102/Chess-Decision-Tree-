from Pieces.piece import piece
import pygame


class Board:
    def __init__(self):
        pygame.init()
        self.BROWN = (102, 51, 0)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.canvas = pygame.display.set_mode((600, 600))
        self.board = [['WR', 'WN', 'WB', 'WK', 'WQ', 'WB', 'WN', 'WR'],
                      ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],
                      ['-', '-', '-', '-', '-', '-', '-', '-'],
                      ['-', '-', '-', '-', '-', '-', '-', '-'],
                      ['-', '-', '-', '-', '-', '-', '-', '-'],
                      ['-', '-', '-', '-', '-', '-', '-', '-'],
                      ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],
                      ['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR']]
        self.pieces = [[], [], [], [], [], [], [], []]
        self.moves = []
        cnt = 0
        for i in self.board:
            for j in i:
                if j == '-':
                    self.pieces[cnt].append(piece(False))
                else:
                    self.pieces[cnt].append(piece(True, j[0], j[1]))
            cnt += 1
        self.update_board()
        self.play_game()

    def create_rect(self, x, y, color):  # Creates squares
        pygame.draw.rect(self.canvas, color, [x, y, 70, 70])

    def draw_board(self):
        for i in range(0, 8):
            for j in range(0, 8):
                if (j % 2) ^ (i % 2):
                    self.pieces[i][j].pos_y = i * 70 + 20
                    self.pieces[i][j].pos_x = j * 70 + 20
                    self.pieces[i][j].board_x = i
                    self.pieces[i][j].board_y = j
                    self.create_rect(i * 70 + 20, j * 70 + 20, self.WHITE)
                else:
                    self.pieces[i][j].pos_y = i * 70 + 20
                    self.pieces[i][j].pos_x = j * 70 + 20
                    self.pieces[i][j].board_x = i
                    self.pieces[i][j].board_y = j
                    self.create_rect(i * 70 + 20, j * 70 + 20, self.BROWN)

    def update_board(self):
        self.draw_board()
        self.place_pieces()
        pygame.display.update()

    def place_pieces(self):
        for i in self.pieces:
            for j in i:
                if j.present:
                    j.draw_piece(self.canvas)

    def play_game(self):
        run = True
        click_x = 0
        click_y = 0
        board_x = 0
        board_y = 0
        click = False
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.update_board()
                    pos = pygame.mouse.get_pos()
                    click_y = (pos[0] - 20) // 70
                    click_x = (pos[1] - 20) // 70
                    print(click_x, click_y, click)
                    if click:
                        if self.check_move(click_x, click_y):
                            for i in self.moves:
                                if i.x_new == click_x and i.y_new == click_y:
                                    self.board, self.pieces = i.make_move(self.board, self.pieces)
                                    self.update_board()
                                    click = False
                                    self.moves.clear()
                                    break
                            continue
                        else:
                            click = False
                            self.moves.clear()
                    if click == False and self.check_pos(click_x, click_y):
                        click = True
                        # print(click_x, click_y, click)
                        self.moves = self.pieces[click_x][click_y].get_moves(self.pieces)
                        # print(self.pieces[click_x][click_y].type.first_move)
                        for i in self.moves:
                            # print(i.x_old, i.y_old, i.x_new, i.y_new)
                            i.show_move(self.canvas)
                            # print(i.x_new, i.y_new)
                            if self.check_pos(i.x_new, i.y_new):
                                self.pieces[i.x_new][i.y_new].draw_piece(self.canvas)
                            pygame.display.update()

    def check_pos(self, x, y):
        return self.pieces[x][y].present

    def check_move(self, x, y):
        for i in self.moves:
            if i.x_new == x and i.y_new == y:
                return True
        return False
