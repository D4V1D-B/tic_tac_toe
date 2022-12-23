class Board():
    def __init__(self) -> None:
        self.board = self.makeBoard()

    def __str__(self) -> str:
        return self.board

    def makeBoard(self):
        plateau = []
        ligne = [' ', ' ', ' ']
        for x in range(3):
            plateau.append(ligne)
        return plateau
