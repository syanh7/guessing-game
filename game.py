"""A number-guessing game."""

# Put your code here
import random




def game(name):
    print("{}, I'm thinking of a number between 1 and 100".format(name))
    print("Try to guess my number")

    number = random.randint(1, 101)

    guess = -1
    tries = 0

    while guess != number:
        
        try:
            guess = int(input("Your guess?\n"))
            if guess < number:
                print("Your guess is too low, try again.")
            elif guess > number:
                print("Your guess is too high, try again.")
            else: 
                print(f"Well done, {name}! You found my number in {tries} tries!")
        except:
            print("Your guess is not a number, please try again.")
            tries -= 1
        tries += 1
    
    return tries - 1




name = input("Howdy, what's your name?\n")

flag = 'y'

best_scores = []

while flag == 'y':
    tries = game(name)
    best_scores.append(tries)

    
    flag = input("Would you like to play again? Enter 'y' for yes, enter anything for no\n").lower()

print("best score is: ", min(best_scores))