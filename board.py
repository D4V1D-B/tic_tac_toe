class Board():
    def __init__(self) -> None:
        self.board = self.makeBoard()

    def __str__(self) -> str:
        string = (f'{self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]}'+
        f'\n---------'+
        f'\n{self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]}'+
        f'\n---------'+
        f'\n{self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]}')
        return string + '\n'

    def makeBoard(self):
        plateau = []
        for _ in range(3):
            plateau.append([' ', ' ', ' '])
        return plateau

    def placer(self, joueur, position):
        #manque verif
        if joueur is 1:
            self.board[position[1]][position[0]] = 'X'
        if joueur is 2:
            self.board[position[1]][position[0]] = 'O'

    def est_terminee(self):
        #ligne et colonne
        for joue in ['O', 'X']:
            for x in range(0,2):
                #ligne
                if self.board[x][0] is joue and self.board[x][1] is joue and self.board[x][2] is joue:
                    return True
                #colonne
                if self.board[0][x] is joue and self.board[1][x] is joue and self.board[2][x] is joue:
                    return True
            #diago 1
            if self.board[0][0] is joue and self.board[1][1] is joue and self.board[2][2] is joue:
                return True
            #diago 2
            if self.board[2][0] is joue and self.board[1][1] is joue and self.board[0][2] is joue:
                return True
        return False
