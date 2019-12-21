from Board.Board import Board
from Client.Client import Client
from Board.Move import Move


class Game:
    def __init__(self):
        self.board = Board()
        self.client = Client()
        self.client.connect('127.0.0.1', 5100)
        self.num = self.client.assign()
        if self.num == 0:
            self.color, self.opponent = 'B', 'W'
        else:
            self.color, self.opponent = 'W', 'B'
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
        i = 0
        status = False
        while True:
            if i % 2 == self.num:
                status, move = self.board.play_game(self.color, 'Online')
                msg = self.move_msg(move, status)
                self.client.send(msg)
            else:
                msg = self.client.receive()
                print(msg)
                status, move = self.msg_move(msg)
                move.make_move(self.board.board, self.board.pieces)
                self.board.update_board()
            if not status:
                self.client.close()
                break
            # x = input("Wait...")
            moves = self.check_all_moves(self.opponent)
            if len(moves) == 0:
                print('Color ', self.color, ' won')
                break
            i += 1
