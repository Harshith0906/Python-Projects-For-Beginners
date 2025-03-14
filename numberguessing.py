import random
print("Enter the maximum range")
y=int(input())
#random.randrange(0,11)->here 11 is excluded or
x=random.randint(0,y)#here 10 is inculded

print("You Will have 3 Chances to Guess")
c=3
while True:
    print("Guess The Number : ")
    g=int(input())
    if x==g:
        print("Your Guess is Correct..!")
        break
    else:
        print("OOPS..!")
        print("It's a Wrong Guess "+ "Try Again...")
        c=c-1
        print("You Have Only "+ str(c) +" Chances")
        if c==0:
            print("Better Luck Next Time")
            print("Your Chances are Up")
            break