from Board import Board
from Board import states
import threading
import copy


class Game:
    def __init__(self):
        self.is_AI_thinking = False
        self.cnt = 0
        self.board = Board.Board()
        self.que = []
        self.piece_table = {'Pawn': [0, 0, 0, 0, 0, 0, 0, 0,
                                     50, 50, 50, 50, 50, 50, 50, 50,
                                     10, 10, 20, 30, 30, 20, 10, 10,
                                     5, 5, 10, 25, 25, 10, 5, 5,
                                     0, 0, 0, 20, 20, 0, 0, 0,
                                     5, -5, -10, 0, 0, -10, -5, 5,
                                     5, 10, 10, -20, -20, 10, 10, 5,
                                     0, 0, 0, 0, 0, 0, 0, 0],
                            'Knight': [-50, -40, -30, -30, -30, -30, -40, -50,
                                       -40, -20, 0, 0, 0, 0, -20, -40,
                                       -30, 0, 10, 15, 15, 10, 0, -30,
                                       -30, 5, 15, 20, 20, 15, 5, -30,
                                       -30, 0, 15, 20, 20, 15, 0, -30,
                                       -30, 5, 10, 15, 15, 10, 5, -30,
                                       -40, -20, 0, 5, 5, 0, -20, -40,
                                       -50, -90, -30, -30, -30, -30, -90, -50],
                            'Bishop': [-20, -10, -10, -10, -10, -10, -10, -20,
                                       -10, 0, 0, 0, 0, 0, 0, -10,
                                       -10, 0, 5, 10, 10, 5, 0, -10,
                                       -10, 5, 5, 10, 10, 5, 5, -10,
                                       -10, 0, 10, 10, 10, 10, 0, -10,
                                       -10, 10, 10, 10, 10, 10, 10, -10,
                                       -10, 5, 0, 0, 0, 0, 5, -10,
                                       -20, -10, -90, -10, -10, -90, -10, -20],
                            'Rook': [0, 0, 0, 0, 0, 0, 0, 0,
                                     5, 10, 10, 10, 10, 10, 10, 5,
                                     -5, 0, 0, 0, 0, 0, 0, -5,
                                     -5, 0, 0, 0, 0, 0, 0, -5,
                                     -5, 0, 0, 0, 0, 0, 0, -5,
                                     -5, 0, 0, 0, 0, 0, 0, -5,
                                     -5, 0, 0, 0, 0, 0, 0, -5,
                                     0, 0, 0, 5, 5, 0, 0, 0],
                            'Queen': [-20, -10, -10, -5, -5, -10, -10, -20,
                                      -10, 0, 0, 0, 0, 0, 0, -10,
                                      -10, 0, 5, 5, 5, 5, 0, -10,
                                      -5, 0, 5, 5, 5, 5, 0, -5,
                                      0, 0, 5, 5, 5, 5, 0, -5,
                                      -10, 5, 5, 5, 5, 5, 0, -10,
                                      -10, 0, 5, 0, 0, 0, 0, -10,
                                      -20, -10, -10, 70, -5, -10, -10, -20],
                            'King': [-30, -40, -40, -50, -50, -40, -40, -30,
                                     -30, -40, -40, -50, -50, -40, -40, -30,
                                     -30, -40, -40, -50, -50, -40, -40, -30,
                                     -30, -40, -40, -50, -50, -40, -40, -30,
                                     -20, -30, -30, -40, -40, -30, -30, -20,
                                     -10, -20, -20, -20, -20, -20, -20, -10,
                                     20, 20, 0, 0, 0, 0, 20, 20,
                                     20, 30, 10, 0, 0, 10, 30, 20]}
        self.play_game()

    def get_piece_val(self, x, y, color):
        # print(x, y)
        i = x * 8 + y
        if color == 'W':
            i = (7 - x)*8 + y
        score = 0
        if color == 'W':
            score -= self.piece_table[self.board.pieces[x][y].name][i]
        else:
            try:
                score += self.piece_table[self.board.pieces[x][y].name][i]
            except KeyError:
                print(x, y, self.board.board[x][y], self.board.pieces[x][y].name)
                print(self.cnt)
                for j in self.board.board:
                    print(j, ',')
        # print(i)
        return score

    def evaluate(self, color):
        st = states.States(self.board.pieces)
        if not st:
            if color == 'W':
                return -20000
            else:
                return 20000
        piece_wt = {'King': 2000,
                    'Queen': 900,
                    'Rook': 500,
                    'Bishop': 330,
                    'Knight': 320,
                    'Pawn': 100}
        mat_wt = 0
        mob = 0
        for i in range(8):
            for j in range(8):
                if self.board.pieces[i][j].present:
                    if self.board.pieces[i][j].color == color:
                        mob += self.get_piece_val(i, j, self.board.pieces[i][j].color)
                        mat_wt -= piece_wt[self.board.pieces[i][j].name]
                    else:
                        mob += self.get_piece_val(i, j, self.board.pieces[i][j].color)
                        mat_wt += piece_wt[self.board.pieces[i][j].name]
                    # print(self.board.pieces[i][j].name[0], self.board.pieces[i][j].color, mob)
        # print(mat_wt, mob)
        return mat_wt + mob

    def copy(self, val):
        fin_copy = []
        for i in val:
            fin_copy.append(i.copy())
        return fin_copy

    def min_max(self, color, opponent, alpha, beta, depth, maximizing_player, flag=False):
        # if flag and depth % 2 == 1:
        #     print("Intermediate Move", depth)
        #     for i in self.board.board:
        #         print(i)
        if depth == 3:
            return -self.evaluate(opponent)
        if maximizing_player:
            best = -10000000
        else:
            best = 10000000
        moves = self.check_all_moves(color)
        for i in moves:
            p1, p2 = i.copy_piece()
            if i.type == 'Castling':
                print('Depth : ', depth)
                print('Moves : ', i.x_old, i.y_old, i.x_new, i.y_new)
                for j in self.que:
                    print("Step X", len(self.que), color)
                    for k in j:
                        print(k)
            self.que.append(self.copy(self.board.board))
            self.board.board, self.board.pieces = i.make_move(self.board.board, self.board.pieces)
            result = self.min_max(opponent, color, alpha, beta, depth + 1, not maximizing_player, flag)
            self.board.board, self.board.pieces = i.undo_move(self.board.board, self.board.pieces, p1, p2)
            self.que.pop()
            if maximizing_player:
                best = max(best, result)
                alpha = max(alpha, best)
            else:
                best = min(best, result)
                beta = min(beta, best)
            if beta <= alpha:
                return best
        return best

    def AI_move(self, color, opponent):
        self.is_AI_thinking = True
        moves = []
        best = -10000000
        moves = self.check_all_moves(color)
        best_move = moves[0]
        self.que.append(self.copy(self.board.board))
        for i in moves:
            p1, p2 = i.copy_piece()
            if i.type == 'Castling':
                print('Found', 0)
            self.board.board, self.board.pieces = i.make_move(self.board.board, self.board.pieces)
            self.que.append(self.copy(self.board.board))
            if i.x_old == 0 and i.y_old == 4 and i.y_new == 5:
                result = self.min_max(opponent, color, -10000000, 10000000, 1, False, True)
            else:
                result = self.min_max(opponent, color, -10000000, 10000000, 1, False)
            self.board.board, self.board.pieces = i.undo_move(self.board.board, self.board.pieces, p1, p2)
            self.que.pop()
            if result > best:
                best = result
                best_move = i
        self.is_AI_thinking = False
        self.que.pop()
        print(len(self.que))
        print('AI Move : ', best_move.type, best_move.x_old, best_move.y_old, best_move.x_new, best_move.y_new)
        # print("Before Move")
        # for i in self.board.board:
        #     print(i)
        self.board.board, self.board.pieces = best_move.make_move(self.board.board, self.board.pieces)
        # print("After Move")
        # for i in self.board.board:
        #     print(i)
        self.board.update_board()

    def check_all_moves(self, color):
        moves = []
        for i in self.board.pieces:
            for j in i:
                if j.present and j.color == color:
                    prev = len(moves)
                    moves.extend(j.get_moves(self.board.pieces, self.board.board))
        return moves

    def show_animation(self):
        green = (51, 255, 51)
        num = 0
        x = 0
        y = 0
        while self.is_AI_thinking:
            num += 1
            if num % 6 == 0:
                x += 1
                if x == 8:
                    x = 0
                    y += 1
                if y == 8:
                    x = 0
                    y = 0
                self.board.create_rect(x * 70 + 20, y * 70 + 20, green, 60, 60)
                # self.board.update_display()

    def play_game(self):
        i = 0
        while True:
            if i % 2 == 0:
                color, opponent = 'B', 'W'
                status = self.board.play_game(color)
                for j in self.board.board:
                    print(j)
            else:
                color, opponent = 'W', 'B'
                status = True
                t1 = threading.Thread(target=self.AI_move, args=(color, opponent,))
                t1.start()
                t1.join()
                if self.is_AI_thinking:
                    self.show_animation()
            if not status:
                break
            moves = self.check_all_moves(opponent)
            if len(moves) == 0:
                print('Color ', color, ' won')
                break
            i += 1
            # for j in self.board.pieces:
            #     for k in j:
            # print(k.name, end=" ")
            # print()
