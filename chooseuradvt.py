name=input("Enter your Name: ")
print("Welcome",name,"to this Adventure")
answer=input("You are on a dirty road,It has came to and end and you can go left or right\n Which way you like to go?\n").lower()
if answer=="left":
    q=input("You came to a river,you can walk around it or swim across it?Type Walk to walk around and Swim to swim across\n").lower()
    if q=="walk":
        print("You walked for many miles,ran out of water and lost the game.")
    elif q=="swim":
        print("You swam across and you were eaten by an aligator.")
    else:
        print("You have choosen a wrong option.You lose")

elif answer=="right":
    p=input("You come to a bridge,it looks wobbly,do you want cross it or head back,(Cross/Back)").lower()
    if p=="cross":
        answer=input("You crossed the bridge and meet a stranger.(Yes/NO)").lower()
        if answer=="yes":
            print("You Talk to the Stranger and they give you the lift.")
            print("YOU WIN....")
        elif answer=="no":
            print("You ignored the stranger and they are offended and you loose.")
        else:
            print("You have choosen a wrong option.You lose")

    elif p=="back":
        print('You go back,You loose.')
    else:
        print("You have choosen a wrong option.You lose")
else:
    print("You have choosen a wrong option.You lose")
print("Thank You for Playing",name)