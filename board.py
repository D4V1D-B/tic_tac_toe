class Board():
    def __init__(self) -> None:
        self.board = self.makeBoard()

    def __str__(self) -> str:
        string = ''
        for y in self.board:
            for x in y:
                string += '| '+ x +' |'
            string += '\n------------\n'
        return string

    def makeBoard(self):
        plateau = []
        ligne = [' ', ' ', ' ']
        for x in range(3):
            plateau.append(ligne)
        return plateau

    def placer(self, joueur, position):
        if joueur is 1:
            self.board[2][0] = 'X'
        if joueur is 2:
            self.board[position[1]][position[0]] = 'O'
