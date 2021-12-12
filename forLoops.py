#Loops

my_fruit = ["Apple", "Banana", "Orange"]

for fruit in my_fruit:
    print(fruit)

for number in range(17):
    print(number)

for char in "Hello world":
    print(char)

for word in "Hello world, this is a nice day".split():
    print(word)

diction= {"key" : "value"}

print("\n")
for key in diction:
    print(key)

for value in {"key" : "value"}.values():
    print(value)

for key, value in diction.items():
    print(key, value)


print("\n\n\n\n\n")


result = []
for x in range(5):
    result.append(x)
    print(result)

print([x for x in range(5)])

for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(10):
    if i == 5:
        continue
    print(i)

for number1 in range(13):
    for number2 in range(13):
        print(number1, "x", number2, "=", number1 * number2)

for i in range(5, 11):
    print(i)

for i in range(10, 21, 2):
    print(i)