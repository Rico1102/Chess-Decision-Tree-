import queue
import threading

from Board.Board import Board
from Board.Move import Move
from Client.Client import Client


class Game:
    def __init__(self):
        self.client = Client()
        self.client.connect('54.85.92.234', 5100)
        self.num = self.client.assign()
        if self.num % 2 == 0:
            self.color, self.opponent = 'B', 'W'
        else:
            self.color, self.opponent = 'W', 'B'
        print("Finding Opponent!!!")
        self.client.find_opponent()
        self.board = Board()
        self.play_game()

    def check_all_moves(self, color):
        moves = []
        for i in self.board.pieces:
            for j in i:
                if j.present and j.color == color:
                    moves.extend(j.get_moves(self.board.pieces, self.board.board))
        return moves

    def move_msg(self, move, status):
        if status:
            msg = '1_'
            msg += str(move.x_old) + '_' + str(move.y_old) + '_' + str(move.x_new) + '_' + str(move.y_new)
        else:
            msg = '0'
        print('Send msg ', msg)
        return msg

    def msg_move(self, msg):
        pos = [0, 0, 0, 0, 0]
        c = ""
        cnt = 0
        for i in msg:
            if i == '_':
                pos[cnt] = int(c)
                cnt += 1
                c = ""
            else:
                c += i
        pos[cnt] = int(c)
        move = Move(pos[1], pos[2], pos[3], pos[4], self.board.pieces)
        print('Move ', pos[1], pos[2], pos[3], pos[4])
        return pos[0], move

    def play_game(self):
        i = 1
        status = False
        s_status = True
        waiting_for_opponent = False
        msg = ""
        thread = None
        q = queue.Queue()
        while True:
            if not waiting_for_opponent:
                if i % 2 == self.num % 2:
                    print("My Turn")
                    status, move = self.board.play_game(self.color, 'Online')
                    msg = self.move_msg(move, status)
                    print('Sent -> ', msg)
                    self.client.send(msg)
                    i += 1
                    if not status:
                        self.client.close()
                        self.board.destroy_board()
                        break
                else:
                    print("Opponent's Turn")
                    thread = threading.Thread(target=self.client.receive, args=(q,))
                    waiting_for_opponent = True
                    thread.start()
                    continue
                moves = self.check_all_moves(self.opponent)
                if len(moves) == 0:
                    print('Color ', self.color, ' won')
                    break
            elif waiting_for_opponent and thread.is_alive():
                if s_status:
                    s_status = self.board.keep_screen_alive()
                    if not s_status:
                        print(s_status)
                        self.board.destroy_board()
            elif waiting_for_opponent and not thread.is_alive():
                waiting_for_opponent = False
                if not s_status:
                    msg = self.move_msg("", 0)
                    self.client.send(msg)
                    break
                i += 1
                msg = q.get()
                print('Received -> ', msg)
                status, move = self.msg_move(msg)
                if not status:
                    print("Opponent Left")
                    self.client.close()
                    if s_status:
                        self.board.destroy_board()
                    break
                move.make_move(self.board.board, self.board.pieces)
                self.board.update_board()
