import random
print("Let's Play ROCK PAPER SCISSORS")
print("Enter the Number of Rounds You Want to Play")
a=int(input())
print("There Will be "+str(a)+ " Rounds")
print("Type :\nR- For Rock\nP-Paper\nS-Scissors\nQ-TO Quit the Game in the Middle")
s=["R","P","S"]
c=0
f=0
z=1
while True:
    print("Round - "+str(z))
    b=input("You Have Choosen :\n").upper()
    if b=="Q":
        print("The Game has Ended")
        print(f'You Have Won {c} Times')
        print(f'System Has Won {f} Times')
        break
    elif b not in s:
        print("It's a Foul.")
        print("Enter A Valid Input.")
        continue
    else:
        x=random.randint(0,2)
        computer_guess=s[x]
        print("Computer has Choosen :\n"+str(computer_guess))
        if b=="R" and computer_guess=="S":
            print("You Won..!")
            c+=1
        elif b=="S" and computer_guess=="P":
            print("You Won..!")
            c+=1
        elif b=="R" and computer_guess=="S":
            print("You Won..!")
            c+=1
        elif b == computer_guess:
            print("It's a Tie")
            f+=0.5
            c+=0.5
        else:
            print("System Won")
            f+=1
    z+=1
    if z>a:
        print("The Game has Ended")
        print(f'You Have Secured a Score of {c}.')
        print(f'System Has Secured a Score of {f}.')
        print("Thank You For Playing...")
        break