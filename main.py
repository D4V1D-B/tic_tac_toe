from board import Board


def recup_move(joueur):
    #manque verif
    print('Tour Joueur',joueur,':')
    pos = input("Donnez la position où appliquer ce coup (x,y):")
    return (joueur, [int(i) for i in pos.split(',')])

if __name__ == "__main__":
    board = Board()
    while board.est_terminee() is False:
        for x in [1, 2]:
            print(board)
            joueur, position = recup_move(x)
            board.placer(joueur, position)
            if board.est_terminee():
                print(board)
                break
            
    
