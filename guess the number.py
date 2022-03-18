from random import randint

life = 5
x = randint(0, 50)
print(x)

# its not magic its hardwork and english ng puyat
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def guess():
    global x
    global life
    print(bcolors.WARNING + "life {}".format(life) + bcolors.ENDC)
    while life != 0:
        try:
            input1 = int(input("enter your guess "))
        except ValueError:
            guess()
            break
            # pag inalis mo yung break may probelma
            # di mo parin nasosolllve bakit
            # nagawa molng yan dahil sa panghuhula

            # ok gets kona palitan mo ng continue yang guess() at break para umulit sa simulang ng loop

            #pero di mo parin alam bakit gumagana yung guess() +   break
        if x > input1:
            print("higher")
            life -= 1
        elif x < input1:
            print("lower")
            life -= 1
        elif x == input1:
            print("nice")
            break
        print(bcolors.WARNING + "life {}".format(life) + bcolors.ENDC)
    else:
        print("you lost")

guess()
