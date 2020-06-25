from Board.Board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.play_game()

    def check_all_moves(self, color):
        moves = []
        for i in self.board.pieces:
            for j in i:
                if j.present and j.color == color:
                    moves.extend(j.get_moves(self.board.pieces, self.board.board))
        return moves

    def play_game(self):
        i = 0
        while True:
            if i % 2 == 0:
                color, opponent = 'B', 'W'
            else:
                color, opponent = 'W', 'B'
            status = self.board.play_game(color)
            if not status:
                break
            moves = self.check_all_moves(opponent)
            if len(moves) == 0:
                print('Color ', color, ' won')
                break
            i += 1

