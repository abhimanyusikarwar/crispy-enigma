print("Number Guessing Game")
print("Guess a number between")

import random
number = random.randint(1,9)

chances = 0
while chances < 5:
    print(chances)
    guess=int(input("Enter Guess : "))
    if guess < number :
        print("Guess a number higher than ",guess)
    elif guess > number:
        print("Guess a number smaller than ",guess)

    elif guess == number:
        print("Congratulation You won")
        break
        
    chances=chances+1    

if not chances < 5:
    print("You Lose!!!The number is ",number)
    

    