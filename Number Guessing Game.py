import random  #imported this library to generate random numbers


Random_Number=random.randint(1, 100)  #used this to generate a random number between 1 and 100
attempt = 0  #new variable for the attempts counter

try:  #used try to handle exceptions
    n = int(input("Choose the number of tries you prefer: "))  #new variable to get the number of attempts the user prefers
except ValueError:  #with the try to handle exceptions
    print("Invalid number")

for i in range(n):  #for loop to give the user more than one attempt

    attempt = (i + 1)
    try:  #used try to handle exceptions
        Guess = int(input("Guess the number between 1 and 100: "))#take the user`s guess
    except ValueError:  #with the try to handle exceptions
        print("invalid number")
        break

#if-else statement to check if the guess equals the random number
    if Random_Number > Guess:
        print("Guess higher ")
    elif Random_Number < Guess:
        print("Guess lower ")
    elif Random_Number == Guess:
        print("Congrats, that is the correct answer!!")
        print(f"you got it in: {attempt} tries")
        break


print(f" the number was: {Random_Number}")  #this gives the number after the attempts are over