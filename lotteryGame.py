#lotteryGame

import random
number = random.randint(10,99)

slot1 = number // 10 
slot2 = number % 10

guess = eval(input("Choose a number between 10 and 100: "))

guess1 = guess // 10
guess2 = guess % 10

if guess == number:
    print("You win £10,000")
elif guess1 == slot1 or guess2 == slot2:
    print("You win £1000")
elif guess1 == slot1 or slot2:
    print("You win £100")
elif guess2 == slot1 or slot2:
    print("You win £100")
else:
    print("You win nothing")

print("Number chosen was:", number,)