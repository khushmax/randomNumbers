import random

print("Guessing Number Game")

rightNumber = random.randint(1,9)


chances = 0
while chances < 5:
    guess = int(input("guess you number between 1 and 9 and share :"))

    if(rightNumber == guess):
        print("you are right")
        break

    elif(rightNumber > guess):
        print("the number is less")

    elif(rightNumber < guess):
        print("the number is more")

    chances = chances+1








    

    
    
