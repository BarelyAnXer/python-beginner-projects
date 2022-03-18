from tkinter import *
from random import choice
from tkinter import messagebox

root = Tk()
FONT = "Times 60"
pressed = [" "] * 9
buttons = pressed.copy()
answer = False
root.geometry("600x475")
possibile = []
with open('score.txt', 'r') as file:
    # read a list of lines into data
    score = file.readlines()
playerScore = score[0]
compScore = score[1]


def setX(pos):
    global answer
    global playerScore
    global compScore
    global pressed
    global buttons



    if buttons[pos]["text"] == "":
        buttons[pos]["text"] = "X"
        pressed[pos] = "X"
        if isThereWinner(pressed, "X"):
            print("you won")
            playerScore = int(playerScore) + 1
            playerScore = str(playerScore) + "\n"
            score[0] = playerScore
            print(score[0])
            with open('score.txt', 'w') as file:
                file.writelines(score)
            messagebox.showinfo("nice", "magling kang bata ka")
            answer = messagebox.askquestion("isa pa?", "gust mo pa ba maglaro?")
            if answer == "yes":
                pressed = [" "] * 9
                buttons = pressed.copy()
                gui()
        else:
            setO(bestMove())
        if isThereWinner(pressed, "O"):
            print("you won O")
            compScore = int(compScore) + 1
            compScore = str(compScore) + "\n"
            score[1] = compScore
            print(score[1])
            with open('score.txt', 'w') as file:
                file.writelines(score)
            messagebox.showinfo("dum fk", "natalo ka iwwww")
            answer = messagebox.askquestion("isa pa?", "gust mo pa ba maglaro?")
            if answer == "yes":
                pressed = [" "] * 9
                buttons = pressed.copy()
                gui()

            else:
                exit(0)
    print("pressed ", pressed)

def setO(pos):
    global buttons
    global pressed
    ctr = 0
    buttons[pos]["text"] = "O"
    pressed[pos] = "O"
    for i in pressed:
        if i == " ":
            ctr += 1
    print(ctr)
    if ctr == 0:
        if ctr == 0:
            messagebox.showinfo("TIE", "its a tie tie tie")
            answer = messagebox.askquestion("isa pa?", "gust mo pa ba maglaro?")
            if answer == "yes":
                pressed = [" "] * 9
                buttons = pressed.copy()
                gui()
            else:
                exit(0)


def possibleMoves():
    global possibile
    possibile = []
    for i, value in enumerate(pressed):
        if value == " ":
            possibile.append(i)

    print(possibile)
    return possibile


def bestMove():
    move = 0
    for let in ["O", "X"]:
        for i in possibleMoves():
            boardCopy = pressed.copy()
            boardCopy[i] = let
            if isThereWinner(boardCopy, let):
                move = i
                return move
    if 4 in possibleMoves():
        return 4
    cornorsOpen = []
    for i in possibleMoves():
        if i in [0, 2, 6, 8]:
            cornorsOpen.append(i)

    if len(cornorsOpen) > 0:
        return choice(cornorsOpen)

    edgesOpen = []
    for i in possibleMoves():
        if i in [1, 3, 5, 7]:
            cornorsOpen.append(i)

    if len(edgesOpen) > 0:
        return choice(cornorsOpen)

    if 4 in possibleMoves():
        return 4

    return 0


def isThereWinner(board, le):
    return (board[0] == le and board[1] == le and board[2] == le) or (
            board[3] == le and board[4] == le and board[5] == le) or (
                   board[6] == le and board[7] == le and board[8] == le) or (

                   board[0] == le and board[3] == le and board[6] == le) or (
                   board[1] == le and board[4] == le and board[7] == le) or (
                   board[2] == le and board[5] == le and board[8] == le) or (

                   board[0] == le and board[4] == le and board[8] == le) or (
                   board[2] == le and board[4] == le and board[6] == le)


def gui():
    global playerScore
    global compScore
    for pos in range(len(buttons)):
        bcall = lambda bpos=pos: setX(bpos)
        buttons[pos] = Button(root, command=bcall, text="", width=3, font=FONT)
        buttons[pos].grid(row=pos // 3, column=pos % 3)

    fr1 = Frame(root).grid(row="1", column="4")
    l1 = Label(fr1, text="Your Score: {}".format(playerScore), width=20, font="Times 12").grid(row="0", column="4",
                                                                                               sticky="s")
    l2 = Label(fr1, text="Computer Score: {}".format(compScore), width=20, font="Times 12").grid(row="1", column="4",
                                                                                                 sticky="n")


def main():
    gui()


main()
root.mainloop()
