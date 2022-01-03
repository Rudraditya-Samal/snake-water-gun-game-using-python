from random import choice

l = ["s","w","g"]

computer = 0
player = 0

a = 10

Rounds = 0

while (a > Rounds):
    c_c = choice(l)
    p_c = input("Enter s for snake w for water and g for gun\n").lower()
    if p_c=="s" and c_c=="s":
        print("tie")
        print("Computer's choice: snake\n")
        Rounds = Rounds+1
    elif p_c=="w" and c_c=="s":
        print("You lost")
        print("Computer's choice: snake\n")
        computer = computer+1
        Rounds = Rounds+1
    elif p_c=="g" and c_c=="s":
        print("You won")
        print("Computer's choice: snake\n")
        player = player+1
        Rounds = Rounds+1
    elif p_c=="s" and c_c=="w":
        print("You won")
        print("Computer's choice: water\n")
        player = player+1
        Rounds = Rounds+1
    elif p_c=="w" and c_c=="w":
        print("tie")
        print("Computer's choice: water\n")
        Rounds = Rounds+1
    elif p_c=="g" and c_c=="w":
        print("You lost")
        print("Computer's choice: water\n")
        computer = computer+1
        Rounds = Rounds+1
    elif p_c=="s" and c_c=="g":
        print("You lost")
        print("Computer's choice: gun\n")
        computer = computer+1
        Rounds = Rounds+1
    elif p_c=="w" and c_c=="g":
        print("You won")
        print("Computer's choice: gun\n")
        player = player+1
        Rounds = Rounds+1
    elif p_c=="g" and c_c=="g":
        print("tie")
        print("Computer's choice: gun\n")
        Rounds = Rounds+1
    else:
        print("Invalid Input")

f_playerPoints = f"Your points:\t{player}"
f_computerPoints = f"Computer's points\t{computer}\n"
print(f_playerPoints)
print(f_computerPoints)

if player>computer:
    print("You won and computer losed!!!")
elif computer>player:
    print("computer won and You losed!!!")
else:
    print("Its Finally Tie!!!")
    