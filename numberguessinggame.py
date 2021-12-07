#Number Guessing Game
import random
number = random.randint(0, 100)

print("Guess a magic number between 1 and 100")

guess = -1

while guess != number:
    guess = eval(input("Enter your guess: "))
    if guess == number:
        print("Well done you legend!")
    elif guess > number:
        print("Too high, sucker!")
    else:
        print("Too low")