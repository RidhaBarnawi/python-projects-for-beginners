import random  #library to generate random choices

#counters for wins and losses
Win_Counter = 0
Lose_Counter = 0

#dictionary that maps each choice to what it beats
Winning_Array = {"r": "s", "p": "r", "s": "p"}

while True:  #main game loop
    Guess = {"r": "Rock", "p": "Paper", "s": "Scissors"}  #mapping shorthand letters to their full names
    Comp_Choice = random.choice(list(Guess))  #computer makes a random choice from r, p, s
    answer = input("Rock, Paper, or Scissors? (r/p/s): ").lower()  #ask the player for their input

    #check if the player entered a valid choice and show both picks
    if answer == "r":
        print(f"you chose {Guess[answer]}")
        print(f"computer chose {Guess[Comp_Choice]}")
    elif answer == "p":
        print(f"you chose {Guess[answer]}")
        print(f"computer chose {Guess[Comp_Choice]}")
    elif answer == "s":
        print(f"you chose {Guess[answer]}")
        print(f"computer chose {Guess[Comp_Choice]}")
    else:
        print("invalid choice")
        continue

    #decide round result using Winning_Array
    if Winning_Array[answer] == Comp_Choice:
        Win_Counter += 1
    elif Comp_Choice == answer:
        print("it's a tie")
    else:
        Lose_Counter += 1

    #check if player or computer reached 2 wins (best of three)
    if Win_Counter == 2:
        print("congrats!!")
    elif Lose_Counter == 2:
        print("you lose")
    else:
        continue

    #ask the player if they want to continue or quit
    Continue_Game = input("do you want to play again?(n/y): ").lower()
    if Continue_Game == "y":
        #reset counters for a new game
        Win_Counter = 0
        Lose_Counter = 0
        pass
    elif Continue_Game == "n":
        print("thanks for playing")
        break
    else:
        print("invalid choice")
        break


