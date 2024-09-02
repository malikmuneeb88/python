'''We are going to write a program that generates a random number and asks the user to guess it.
If the player's guess is higher than the actual number, the program displays “Lower number please”. Similarly, if the user’s guess is too low, the program prints “higher number please”.
When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.
Hint: Use the random module.'''

# import random

# randNumber = random.randint(1, 100)
# # print(randNumber)

# userGuess = None
# Guesses = 0

# while(userGuess != randNumber):
#     userGuess = int(input("Enter Your Guess : "))
#     Guesses += 1 
    
#     if(userGuess == randNumber):
#         print("You guessed it right")

#     else:
#         if(userGuess > randNumber):
#             print("You guessed it wrong! Enter smaller Number")
    
#         else:
#             print("You guessed it wrong! Enter Larger Number")


# print(f"You guess the number in {Guesses} guesses")

# try:
#     with open("HiScore.txt", "r") as f:
#         HiScore = int(f.read().strip())  # strip() to remove any extra spaces or newlines
# except (FileNotFoundError, ValueError):
#     HiScore = None  # Set to None if file doesn't exist or content isn't valid integer

# if HiScore is None or Guesses < HiScore:
#     print("Congratulations! You've set a new high score!")
#     with open("HiScore.txt", "w") as f:
#         f.write(str(Guesses))  # Write the new high score
# else:
#     print(f"High Score remains: {HiScore}")







import random 

randNumber = random.randint(1, 50)
userGuess = None
Guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter the number you Guess :"))
    Guesses += 1

    if(userGuess == randNumber):
        print("You Guessed it right")

    else:
        if(userGuess > randNumber):
            print("You Guessed it wrong ! Enter Smaller number")
        else:
            print("You Guessed it wrong ! Enter Larger number")

print(f"You Guessed the number in {Guesses} guesses")