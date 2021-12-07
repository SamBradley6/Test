#Create a Boolean variable.
# If it is true print("The truth has been spoken") 
# and if it is false print("Liar Liar")

#print("Give me a number between 5 and 30 that is divisible by 4")
#answer = eval(input("Enter and your answer: "))

#if answer > 30 or answer < 5:
#    print("Liar Liar")
#if answer % 4 != 0:
#    print("Liar Liar")
#if answer > 5 and answer < 30 and answer % 4 == 0: 
#    print("The truth has been spoken")


#Set a variable to a monetary figure.
# Write some code to say you're rich if it the variable
# is over a certain amount or if it is below then print
# "you're poor"

#networth = eval(input("What is your net worth? \n£" ))
#if networth >= 50000: 
#    print("You're rich!")
#if networth < 50000:
#    print("You're poor")


#Using a variable and the 'and' operator, set the variable 
#to a deposit amount and create a variable as a password.
#if the deposit is less than a certain amount and if the
#password matches then print("Thank you for deposit") or 
#else print("Failed to make deposit")

print("Deposit amount: £500")
password = eval(input("Enter password: "))
deposit = eval(input("Enter deposit amount \n£"))
actualpassword = "password123"

if password == actualpassword and deposit == 500:
    print("Thank you for the deposit")

else: print("Failed to make deposit")

# Do number 3 again but use 'if not' and use '!=' and use 
#'or' operator

#Prompt the user to input age. Create an if elif else statement
# printing text such as 'you are above 85', 'between 50 and 85',
# between 20 and 50', below 20'

#age = eval(input("What is your age?"))
#if age > 85:
#    print("You are above 85")
#elif 50 < age <= 85:
#    print("Your age is between 50 and 85")
#elif 20 < age <= 50:
#    print("Your age is between 20 and 50")
#else:
#    print("Your age is below 20")
