from board import Board

if __name__ == "__main__":
    board = Board()
    print(board)
    board.placer(1, [0, 0])
    print(board)
    board.placer(2, [1, 0])
    print(board)
