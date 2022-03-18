from random import choice

board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]


def displayBoard():
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-----")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-----")
    print(board[7] + "|" + board[8] + "|" + board[9])
    print()


def isSpaceFree(pos):
    if board[pos] == " ":
        return True


def userInput(pos):
    board[pos] = "X"


def compInput():
    state =""
    temp = bestMove()
    if temp == 0:
        print("tie")
        exit()
    else:
        print(temp)
        board[temp] = "O"
        print("O placed in {}".format(temp))


def possibleMoves():
    possibile = []
    for i, value in enumerate(board):
        if value == " " and i != 0:
            possibile.append(i)

    return possibile


def bestMove():
    move = 0
    for let in ["O", "X"]:
        for i in possibleMoves():
            boardCopy = board.copy()
            boardCopy[i] = let
            if isThereWinner(boardCopy, let):
                move = i
                return move

    cornorsOpen = []
    for i in possibleMoves():
        if i in [1, 3, 7, 9]:
            cornorsOpen.append(i)

    if len(cornorsOpen) > 0:
        return choice(cornorsOpen)

    if 5 in possibleMoves():
        return 5

    edgesOpen = []
    for i in possibleMoves():
        if i in [2, 4, 6, 8]:
            cornorsOpen.append(i)

    if len(edgesOpen) > 0:
        return choice(cornorsOpen)

    if 5 in possibleMoves():
        return 5

    return 0


def isBoardFull():
    ctr = int()
    for i in board:
        if i == " ":
            ctr += 1
        else:
            pass

    return True if ctr == 1 else False
    # chagne this to board.count later


def isThereWinner(board, le):
    return (board[1] == le and board[2] == le and board[3] == le) or (
            board[4] == le and board[5] == le and board[6] == le) or (
                   board[7] == le and board[8] == le and board[9] == le) or (

                   board[1] == le and board[4] == le and board[7] == le) or (
                   board[2] == le and board[5] == le and board[8] == le) or (
                   board[3] == le and board[6] == le and board[9] == le) or (

                   board[1] == le and board[5] == le and board[9] == le) or (
                   board[3] == le and board[5] == le and board[7] == le)


def main():
    displayBoard()
    while True:
        if isThereWinner(board, "X"):
            print("X won")
            break
        else:
            temp = int(input("player X enter pos "))
            if isSpaceFree(temp):
                userInput(temp)
                displayBoard()
                if isThereWinner(board, "X"):
                    print("X won")
                    break
            else:
                print("space is occupied")
                continue

        if isThereWinner(board, "O"):
            print("O won")
            break
        else:
            compInput()
            displayBoard()
            if isThereWinner(board, "O"):
                print("O won")
                break

        if isBoardFull():
            print("its a tie")
            break


main()
