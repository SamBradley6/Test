#loopingSubtractionQuiz

import random

number1 = random.randint(1, 101)
number2 = random.randint(1, 101)

if number1 < number2:
    number1, number2 = number2, number1

answer = eval(input(f"What is {number1} - {number2}? "))

while number1 - number2 != answer:
    answer = eval(input(f"Sorry try again: \nWhat is {number1} - {number2}? "))

print("Well done")