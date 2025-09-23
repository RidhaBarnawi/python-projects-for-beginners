import time  #imported this library to work with time delays


#function to run a timer for the given number of seconds
def Timer(seconds):
    time.sleep(seconds)  #pause the program for the entered seconds
    print(f"the timer finished after {seconds} seconds!!")  #message after timer ends

#function to get user input for the timer
def UserInput():
    try:  #used try to handle exceptions
        seconds = int(input("enter your time in seconds: "))  #take user input and convert to integer
        if seconds > 0:  #check if the number is positive
            Timer(seconds)  #call the timer function
            RestTime()  #ask the user if they want to restart
        else:
            print("please enter a positive number")  #message for invalid numbers
    except ValueError:  #handle invalid input (non-numeric)
        print("Invalid input. Please enter a number")

#function to ask the user if they want to restart the timer
def RestTime():
    Restart_Time = input("do you want to play timer again?(n/y): ").lower()  #take input and convert to lowercase
    if Restart_Time == "y":
        UserInput()  #restart timer
    elif Restart_Time == "n":
        print("thanks for using our timer")  #exit message
    else:
        print("invalid choice")  #message for invalid input


#start the program by calling the main function
UserInput()

