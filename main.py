from board import Board


def recup_move(joueur):
    #manque verif
    pos = input("Donnez la position où appliquer ce coup (x,y):")
    return (joueur, [int(i) for i in pos.split(',')])

if __name__ == "__main__":
    board = Board()
    while board.est_terminee() is False:
        print(board)
        print('Tour Joueur 1:')
        joueur, position = recup_move(1)
        board.placer(joueur, position)
        print(board)
        print('Tour Joueur 2:')
        joueur, position = recup_move(2)
        board.placer(joueur, position)
    
