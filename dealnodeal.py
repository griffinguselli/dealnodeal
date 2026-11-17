import random
import subprocess
import sys
removedcase = []
case = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
values = ["50c", "$1", "$10", "$50", "$100", "$500", "$1000", "$2000", "$2500", "$4000", "$5000", "$10000", "$20000", "$25000", "$30000" ]
oboard = dict(zip(case, values))
ovalues = values.copy()
random.shuffle(values)
board = dict(zip(case, values))

def printcases():
    subprocess.run("clear")
    for i in case:
        print(f"[{i}]", end=" ")
    print("\nRemoved Cases:")
    for i in removedcase:
        if i == maincase:
            print(f"[{i}]   -Main Case")
        else:
            print(f"[{i}]   {board[i]} || ", end=" ")
    print("")
    print("Remaining Values:")
    for i in ovalues:
        print(f"{i} || ", end="")
def removecases(ran):
    for _ in range(ran):
        removed =  input("\nPick Case To Remove:\n")
        try:
            case.remove(removed)
        except ValueError:
            print("ValueError... Quitting. Make Sure To Type In A Valid Number From List!")
            sys.exit()
        removedcase.append(removed)
        ovalues.remove(board[removed])
        printcases()

def convert(x):
    prize = board[x]
    if prize == "50c":
        r = 0.5
    else:
        r = int(prize.strip("$"))
    return r
def accept(o):
    a = input(f"Offer: {o}\nAccept (Y/N)?\n")
    if a.title == "Y":
        print(f"Congratualations! You made ${o}")
        sys.exit()
    
def makeoffer():
    o = 0
    for i in case:
        o += convert(i)
    o /= len(case)
    o = str(round(o, -1))
    print("")
    accept(o)

printcases()
maincase = input("\n What Case Do You Choose?\n")
case.remove(maincase)
removedcase.append(maincase)
printcases()

removecases(4)
makeoffer()
removecases(3)
makeoffer()
removecases(3)
makeoffer()
removecases(2)
makeoffer()
removecases(1)
o = board[case[0]]
print(f"\nYou Made {o}")

