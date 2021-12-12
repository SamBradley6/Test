<<<<<<< HEAD
#List examples and collections

cool_cows = ["Winnie the Moo", "Moolan", "Milkshake", "Mooana"]

print(cool_cows[2])
print(cool_cows[-1])
print(cool_cows[1:3])

cool_cows[0] = "Aladdin but a cow"

print(cool_cows)
del cool_cows[0]
print(cool_cows)

if "Moolan" in cool_cows:
    print(True)

cool_sheep = ["Baaaart", "Baaaarnaby"]
cool_pigs = ["Chris P. Bacon", "Hamlet", "Hogwarts"]
cool_animals = [cool_cows, cool_sheep, cool_pigs]

print(cool_animals)
print(cool_animals[2][2])

farm = ["Pepperidge Farm", ["Winnie the Moo", "Moolan"], 1850]
print("\n")
print(farm[0])
print(farm[1])
print(farm[2])

my_fruit = ["Apple", "Banana", "Orange"]
print(my_fruit)
my_fruit.append("Grapefruit")
print(my_fruit)
my_fruit.remove("Banana")
print(my_fruit)
my_fruit.pop(0)
print(my_fruit)
my_fruit.insert(0, "Mango")
print(my_fruit)
my_fruit.extend(["Grapefruit", "Kiwi"])
print(my_fruit)
print(my_fruit.index("Grapefruit"))
print(my_fruit.count("Grapefruit"))

print(my_fruit)
my_fruit.reverse()
print(my_fruit)

print(" | ".join(my_fruit))

print("\n\n\n")

##Tuples

cool_cows = "Winnie the Moo", "Moolan", "Milkshake", "Mooana"
print(cool_cows[0])
print("Hello World"[3:8])
farm = "Pepperidge Farm", ["Winnie", "Moo"], 1850
print(farm)
farm_name, cool_cows, farm_size = farm
print(farm_size)


print("\n\n\n")

##Dictionaries

noises = {"cow" : "moo", "sheep" : "baa" }
print(noises["cow"])
noises["chicken"] = "cluck"
print(noises["chicken"])
noises["sheep"] = "meh"
print(noises)
print(noises.keys())
print(noises.values())
print(noises.items())

print("\n\n\n")

if "moo" in noises.values():
    print(True)
else:
    print(False)

print("\n\n\n")

my_words = {"hello" : "hola", "thank-you" : "gracias"}

print(my_words.get("hello"))
my_words.pop("hello")
print(my_words)
my_words.update({"beer" : "cerveza", "hello" :"ey"})
print(my_words)











=======
#List examples and collections

cool_cows = ["Winnie the Moo", "Moolan", "Milkshake", "Mooana"]

print(cool_cows[2])
print(cool_cows[-1])
print(cool_cows[1:3])

cool_cows[0] = "Aladdin but a cow"

print(cool_cows)
del cool_cows[0]
print(cool_cows)

if "Moolan" in cool_cows:
    print(True)

cool_sheep = ["Baaaart", "Baaaarnaby"]
cool_pigs = ["Chris P. Bacon", "Hamlet", "Hogwarts"]
cool_animals = [cool_cows, cool_sheep, cool_pigs]

print(cool_animals)
print(cool_animals[2][2])

farm = ["Pepperidge Farm", ["Winnie the Moo", "Moolan"], 1850]
print("\n")
print(farm[0])
print(farm[1])
print(farm[2])

my_fruit = ["Apple", "Banana", "Orange"]
print(my_fruit)
my_fruit.append("Grapefruit")
print(my_fruit)
my_fruit.remove("Banana")
print(my_fruit)
my_fruit.pop(0)
print(my_fruit)
my_fruit.insert(0, "Mango")
print(my_fruit)
my_fruit.extend(["Grapefruit", "Kiwi"])
print(my_fruit)
print(my_fruit.index("Grapefruit"))
print(my_fruit.count("Grapefruit"))

print(my_fruit)
my_fruit.reverse()
print(my_fruit)

print(" | ".join(my_fruit))

print("\n\n\n")

##Tuples

cool_cows = "Winnie the Moo", "Moolan", "Milkshake", "Mooana"
print(cool_cows[0])
print("Hello World"[3:8])
farm = "Pepperidge Farm", ["Winnie", "Moo"], 1850
print(farm)
farm_name, cool_cows, farm_size = farm
print(farm_size)


print("\n\n\n")

##Dictionaries

noises = {"cow" : "moo", "sheep" : "baa" }
print(noises["cow"])
noises["chicken"] = "cluck"
print(noises["chicken"])
noises["sheep"] = "meh"
print(noises)
print(noises.keys())
print(noises.values())
print(noises.items())

print("\n\n\n")

if "moo" in noises.values():
    print(True)
else:
    print(False)

print("\n\n\n")

my_words = {"hello" : "hola", "thank-you" : "gracias"}

print(my_words.get("hello"))
my_words.pop("hello")
print(my_words)
my_words.update({"beer" : "cerveza", "hello" :"ey"})
print(my_words)











>>>>>>> 8f156222f8b950afe728ac9f1e56ac389ed97268
