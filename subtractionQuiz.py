#subtraction quiz

import random

number1 = random.randint(1, 9)
number2 = random.randint(1, 9)

if number1 < number2:
    number1, number2 = number2, number1

answer = eval(input(f"What is {number1} - {number2}? "))

if number1 - number2 == answer:
    print("Well done!")
else:
    print(f"Your wrong, {number1} - {number2} = {number1 - number2}")