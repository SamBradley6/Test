#OOP

from abc import ABC, abstractmethod

class Bird(ABC):
    fly = Truebabies = 0

    def noise(self):
        return "squark"

        def reproduce(self):
            self.babies += 1

            @abstractmethod
            def eat(self):
                pass

            extinct = False

class Owl(Bird):
    def reproduce(self):
        self.babies =+ 6

        def eat(self):
            return "Peck Peck"

class Dodo(Bird):
    Fly = False
    extinct = True

    def eat(self):
        return "Nom nom"

    def reproduce(self):
        if not self.extinct:
            self.babies += 1

Birdie = Dodo()

print(Birdie.Fly)