"""A number-guessing game."""

# Put your code here
import random




def game(name):
    print("{}, I'm thinking of a number between 1 and 100".format(name))
    
    limit = int(input("How many tries would you like?\n"))

    number = random.randint(1, 100)

    guess = -1
    tries = 0



    while guess != number:
        
        try:
            guess = int(input("Your guess? You have {} guesses remaining\n".format(limit - tries)))
            if guess < number:
                print("Your guess is too low, try again.")
                tries += 1
            elif guess > number:
                print("Your guess is too high, try again.")
                tries += 1
            else: 
                tries += 1
                print(f"Well done, {name}! You found my number in {tries} tries!")
                return tries
                
        except:
            print("Your guess is not a number, please try again.")

        if tries == limit:
            print("Too many tries! The number was ", number)
            return "You didn't win any rounds"

     
    # return tries




name = input("Howdy, what's your name?\n")

flag = 'y'

best_scores = []

while flag == 'y':
    tries = game(name)
    best_scores.append(tries)

    
    flag = input("Would you like to play again? Enter 'y' for yes, enter anything for no\n").lower()

if min(best_scores).isnumeric():
    print("best score is: ", min(best_scores))
else:
    print("you never won")