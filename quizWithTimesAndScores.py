import random
import time

correctCount = 0
count = 0
numberOfQuestions = 5

startTime = time.time()

while count < numberOfQuestions:
    number1 = random.randint(0, 9)
    number2 = random.randint(0, 9)

    if number1 < number2:
        number1, number2 = number2, number1

    answer = eval(input(f"What is {number1} - {number2}? "))

    if number1 - number2 == answer:
        print("You are correct")
        correctCount += 1
        count += 1

    else:
        print(f"You are wrong! \n{number1} - {number2} = {number1 - number2}")
        count += 1
        
endTime = time.time()

testTime = int(endTime - startTime)

print(f"Correct count is {correctCount}, out of {numberOfQuestions} in {testTime} seconds.")
