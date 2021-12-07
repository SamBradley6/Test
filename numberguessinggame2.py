#guess number

import random
number = random.randint(0,101)
print("Magic Number Game")


guess = input("Enter your guess between 0 and 100: ")


if guess < number:
    print("Too high try again")
elif guess > number:
    print("Too low try again.")
else:
    print("You guessed correctly! Well done")
