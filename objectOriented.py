#oop

# Classes and Objects



"""
Class
    Objects
        Attributes
            Method


Dog:
    Attributes:
        -Breed
        -Weight
        -Energy

Name: Bilbo Waggins
Breed: Labrador
Weight: 10lbs
Energy: Low



class Dog:
    energy = "high"

    def speak(self):
        print("woof")

bilbo_waggins = Dog()

print(bilbo_waggins.energy)
bilbo_waggins.speak()

chewbarka = Dog()
chewbarka.energy = "low"
print(chewbarka.energy)
chewbarka.speak()

######################################

class Dog:
    def __init__(self, name, breed, energy):
        self.name = name
        self.breed = breed
        self.energy = energy
dog1 = Dog("Ross Barkley", "Jack Russel", "High")

print(dog1.name)
print(dog1.breed)

########################

_money = 10000000000

class Feline:
    __family = "Felidae"

kitty = Feline()
print(kitty._Feline__family)




################

class Student:

    def __init__(self, name, age):
        self.name = name 
        self.age = age
        
Kane = Student("Kane", "27")
Alia = Student("Alia", "20")

print(getattr(Kane, "age"))

##########################

class Athlete:
    def __init__(self, name):
        self.name = name

class Footballer(Athlete):
    def __init__(self, name, team):
        super().__init__(name)
        self.team = team

player1 = Footballer("Jay", "Bolton Wanderers")

print(getattr(player1.team))

############################

class Animal:
    babies = 0

    def reproduce(self):
        self.babies += 1

class Dog(Animal):
    def reproduce(self):
        self.babies +=6


john = Dog()
john.reproduce()
print(john.babies)

"""
###########################
