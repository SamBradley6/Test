#BMI
weight = eval(input("Enter weight in pounds: "))
height = eval(input("Enter your height in inches: "))

kgperpound = 0.45359237
metersperinch = 0.0254

weightinKG = weight * kgperpound
heightinmeters = height * metersperinch

bmi = weightinKG / (heightinmeters ** 2)

print("BMI is", format(bmi, ".2f"))

if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You are healthy")
elif bmi < 30:
    print("You are overweight")
else:
    print("You are obese")