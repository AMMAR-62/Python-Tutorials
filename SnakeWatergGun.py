import random
ls = ["Snake","Water","Gun"]
num = int(input("Enter the number of times you wanna play"))
while(num>0):
    num-=1
    choice  = random.choice(ls)
    Player = input("Plz select your Choice: ")
    if((Player=="Snake" and choice=="Water") or (Player=="Water" and choice=="Gun") or (Player=="Gun" and choice=="Snake")):
        print("You Win")
        print("I chose",choice)
    elif(Player == choice):
        print("It's a Draw")
        print("I chose",choice)
    else:
        print("You Lose")
        print("I chose",choice)

print("Thanks for Playing")  