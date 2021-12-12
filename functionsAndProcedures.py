##Functions

#Procedures
def greet(firstname, lastname):
    print(f"Hello {firstname} {lastname}")

greet("Steve", "Rogers")

#Functions

def greet(firstname, lastname):
    return f"Hello {firstname} {lastname}"

print(greet("Steve", "Rogers"))

name = greet("Steve", "Rogers")

print(name)

## Procedure
def greet():
    name = input("What's your name? ")
    print(f"Hello {name}")

greet()
    
# Function
def greet(name):
    return f"Hello {name}"

name = input("What is your name? ")
greet(name)

## Default Values
#########################################
def greet(name, greeting="Hello"):
    return f"{greeting} {name}"

greetingforme = greet("Billy", greeting="Yo")

print(greetingforme)

##########################################
print("\n")
def add_calc(number1, number2):
    answer = number1 + number2
    return answer

added_number = add_calc(5,5)
print(added_number*100/50**2)