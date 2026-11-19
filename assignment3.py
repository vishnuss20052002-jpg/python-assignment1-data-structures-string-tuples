import random

secret_number = random.randint(1, 10)

attempts = 3

while attempts > 0:
    guess = int(input("Guess the number (between 1 and 10): "))

    if guess < 1 or guess > 10:
        print("Your guess is out of range. Please guess a number between 1 and 10.")
        continue

    attempts = attempts - 1

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break

    elif guess > secret_number:
        print("Too high. Try again.")

    else:
        print("Too low. Try again.")

else:
    print("Better luck next time!")



#Multiplication Table Generator

num = int(input("enter the number for which you want the multiplication table:"))
for i in range(1,11):
    print(num,"x",i,"=", num*i)


#BMI CALCULATOR

def calculate_bmi(weight, height):
    bmi = weight / (height**2)
    return bmi
weight = float (input("enter your weight in kg:"))
height = float (input("enter your height in meters:"))

result = calculate_bmi(weight,height)
print("your bmi is:",round(result,2))

    
