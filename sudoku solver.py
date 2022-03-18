board = [[0, 0, 0, 1, 0, 0, 0, 0, 4],
         [8, 0, 0, 0, 0, 0, 2, 6, 0],
         [0, 0, 0, 0, 2, 3, 0, 5, 8],
         [0, 1, 0, 0, 0, 4, 0, 0, 0],
         [0, 0, 3, 0, 8, 0, 4, 0, 0],
         [0, 0, 0, 5, 0, 0, 0, 7, 0],
         [4, 7, 0, 9, 1, 0, 0, 0, 0],
         [0, 5, 1, 0, 0, 0, 0, 0, 2],
         [2, 0, 0, 0, 0, 5, 0, 0, 0]]


def displayBoard(bo):
    for i, value in enumerate(bo):
        if i % 3 == 0 and i != 0:
            print("---------------------")
            pass
        for j in range(len(value)):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            print(str(bo[i][j]) + " ", end="")
        print()


def possible(y, x, n):
    for i in range(9):
        if board[y][i] == n:
            return False
    for i in range(9):
        if board[i][x] == n:
            return False

    posx = (x // 3) * 3
    posy = (y // 3) * 3

    for i in range(3):
        for j in range(3):
            if board[i + posy][j + posx] == n:
                return False

    return True


ctr = 0


def solve():
    global board
    global ctr
    ctr = ctr + 1

    for y in range(9):
        print("y")
        for x in range(9):
            if board[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        board[y][x] = n
                        print("n")
                        solve()
                        print("n2")
                        board[y][x] = 0
                return
    displayBoard(board)


def main():
    displayBoard(board)
    print()
    solve()
    print(ctr)


if __name__ == '__main__':
    main()
