class States:
    def __init__(self, pieces):
        self.white_king_x = 0
        self.white_king_y = 0
        self.black_king_x = 0
        self.black_king_y = 0
        self.pieces = pieces
        self.update_pos()

    def update_pos(self):
        for i in range(8):
            for j in range(8):
                if self.pieces[i][j].name == 'King':
                    if self.pieces[i][j].color == 'B':
                        self.black_king_x = i
                        self.black_king_y = j
                    else:
                        self.white_king_x = i
                        self.white_king_y = j

    def check_condition(self, color):
        status = False
        status |= self.diagonal_attack(color)
        status |= self.straight_attack(color)
        return status

    def diagonal_attack(self, color):
        if color == 'W':
            x, y = self.white_king_x, self.white_king_y
        else:
            x, y = self.black_king_x, self.black_king_y
        i = 0
        while True:
            i += 1
            if x + i < 8 and y + i < 8:
                if self.pieces[x + i][y + i].present:
                    if self.pieces[x + i][y + i].color == color:
                        break
                    else:
                        if self.pieces[x + i][y + i].name in ['Queen', 'Bishop']:
                            return True
                        elif self.pieces[x + i][y + i].name == 'Pawn':
                            if i == 1:
                                return True
                            else:
                                return False
                        else:
                            break
                else:
                    continue
            else:
                break
        i = 0
        while True:
            i -= 1
            if x + i > -1 and y + i > -1:
                if self.pieces[x + i][y + i].present:
                    if self.pieces[x + i][y + i].color == color:
                        break
                    else:
                        if self.pieces[x + i][y + i].name in ['Queen', 'Bishop']:
                            return True
                        else:
                            break
                else:
                    continue
            else:
                break

        i = 0
        while True:
            i += 1
            if x + i < 8 and y - i > -1:
                if self.pieces[x + i][y - i].present:
                    if self.pieces[x + i][y - i].color == color:
                        break
                    else:
                        if self.pieces[x + i][y - i].name in ['Queen', 'Bishop']:
                            return True
                        elif self.pieces[x + i][y - i].name == 'Pawn':
                            if i == 1:
                                return True
                            else:
                                return False
                        else:
                            break
                else:
                    continue
            else:
                break
        i = 0
        while True:
            i -= 1
            if x + i > -1 and y - i < 8:
                if self.pieces[x + i][y - i].present:
                    if self.pieces[x + i][y - i].color == color:
                        break
                    else:
                        if self.pieces[x + i][y - i].name in ['Queen', 'Bishop']:
                            return True
                        else:
                            break
                else:
                    continue
            else:
                break

        return False

    def straight_attack(self, color):
        if color == 'W':
            x, y = self.white_king_x, self.white_king_y
        else:
            x, y = self.black_king_x, self.black_king_y
        i = 0
        while True:
            i += 1
            if x + i < 8:
                if self.pieces[x + i][y].present:
                    if self.pieces[x + i][y].color == color:
                        break
                    else:
                        if self.pieces[x + i][y].name in ['Queen', 'Rook']:
                            return True
                        else:
                            break
                else:
                    continue
            else:
                break
        i = 0
        while True:
            i -= 1
            if x + i > -1:
                if self.pieces[x + i][y].present:
                    if self.pieces[x + i][y].color == color:
                        break
                    else:
                        if self.pieces[x + i][y].name in ['Queen', 'Rook']:
                            return True
                        else:
                            break
                else:
                    continue
            else:
                break

        i = 0
        while True:
            i += 1
            if y + i < 8:
                if self.pieces[x][y + i].present:
                    if self.pieces[x][y + i].color == color:
                        break
                    else:
                        if self.pieces[x][y + i].name in ['Queen', 'Rook']:
                            return True
                        else:
                            break
                else:
                    continue
            else:
                break
        i = 0
        while True:
            i -= 1
            if y + i > -1:
                if self.pieces[x][y + i].present:
                    if self.pieces[x][y + i].color == color:
                        break
                    else:
                        if self.pieces[x][y + i].name in ['Queen', 'Rook']:
                            return True
                        else:
                            break
                else:
                    continue
            else:
                break
        return False
