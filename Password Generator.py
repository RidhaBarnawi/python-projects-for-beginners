import string
import random

#function to get the password length from user
def password_length():
    try:
        length = int(input("passwords length: "))   #take input and convert to integer
        if length >= 8:  #check if the number is greater than or equal to 8
            return length  #return the length
        else:
            print("make sure u entered more than 7")  #message for invalid numbers
            password_length()  #call the function again
    except ValueError:  #handle invalid input (non-numeric)
        print("invalid input")  #error message

#function to get how many passwords the user wants
def passwords_number():
    try:
        qty = int(input("number of passwords: "))  #take input and convert to integer
        if qty > 0:  #check if number is positive
            return qty  #return the quantity
        else:
            print("enter a number greater than 0 ")  #message for invalid number
    except ValueError:  #handle invalid input (non-numeric)
        print("invalid input")  #error message

#function to generate passwords using letters, digits and symbols
def password_generator(length, qty):
    all_chars = string.ascii_letters + string.digits + "!"  #define all possible characters
    for i in range(qty):  #loop for number of passwords
        random_string = ''.join(random.choice(all_chars) for _ in range(length))  #generate random password
        print(random_string)  #print the password

#main function to run the other functions
def main():
    length = password_length()  #call the function to get password length
    qty = passwords_number()  #call the function to get quantity

    print("here are your passwords: ")  #message before showing passwords
    password_generator(length, qty)  #call the generator function

#run the main function when the script is executed
if __name__=="__main__":
    main()