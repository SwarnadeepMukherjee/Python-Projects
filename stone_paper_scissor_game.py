import random

def sps(comp, player):
    if ((player==1) and (comp==1)):
        print("Tie")
    elif ((player==1) and (comp==2)):
        print("You Lose!!")
    elif ((player==1) and (comp==3)):
        print("You Win!!")
    elif ((player==2) and (comp==1)):
        print("You Win!!")
    elif ((player==2) and (comp==2)):
        print("Tie")
    elif ((player==2) and (comp==3)):
        print("You Lose!!")
    elif ((player==3) and (comp==1)):
        print("You Lose!!")
    elif ((player==3) and (comp==2)):
        print("You Win!!")
    elif ((player==3) and (comp==3)):
        print("Tie")
    else:
        print("INVALID INPUT")

print("Welcome to:   !! STONE, PAPER & SCISSOR !!")
print("")
print("      Credits: Swarnadeep Mukherjee")
print("To Exit:- 1.Press Enter ; 2.Press Ctrl+C")
print("")
comp=random.randint(1,3)
player=int(input("Stone(1), Paper(2) and Scissor(3): "))
sps(comp, player)
print("")
repeat=input("Do you want to play multiple times? (Y/N): ")

while ((repeat!='Y') or (repeat!='y')):
    if ((repeat=='y') or (repeat=='Y')):
        del comp, player
        comp=random.randint(1,3)
        player=int(input("Stone(1), Paper(2) and Scissor(3): "))
        sps(comp, player)
    elif ((repeat=='N') or (repeat=='n')):
        print("Thank You For Playing Our Game")
    else:
        print("INVALID INPUT")