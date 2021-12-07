#if and else statement
import math
radius = eval(input ("Enter the radius: "))

if radius < 0:
    print("Incorrect Input")
else: 
    area = radius * radius * math.pi
    print("Area is: ",area,)