<<<<<<< HEAD
#prime numbers

numberOfPrimes = 50
numberOfPrimesPerLine = 10
count = 0
number = 2

print("Ther first 50 primes are:")

while count < numberOfPrimes:
    isPrime = True
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            isPrime = False
            break
        divisor += 1
    if isPrime:
        count += 1
        print(format(number, "5d"), end = "")
        if count % numberOfPrimesPerLine == 0:
            print()
    
=======
#prime numbers

numberOfPrimes = 50
numberOfPrimesPerLine = 10
count = 0
number = 2

print("Ther first 50 primes are:")

while count < numberOfPrimes:
    isPrime = True
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            isPrime = False
            break
        divisor += 1
    if isPrime:
        count += 1
        print(format(number, "5d"), end = "")
        if count % numberOfPrimesPerLine == 0:
            print()
    
>>>>>>> 8f156222f8b950afe728ac9f1e56ac389ed97268
    number += 1