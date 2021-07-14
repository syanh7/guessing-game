"""A number-guessing game."""

# Put your code here
import random




def game(name):
    
    
    limit = int(input("How many tries would you like?\n"))

    lower = int(input("Enter a starting number\n"))
    upper = int(input("Enter a ending number\n"))

    print("{}, I'm thinking of a number between {} and {}".format(name, lower, upper))

    number = random.randint(lower, upper)

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

def computer():
    print("Select a number between 1 and 100 in your head")
    lower = 1
    upper = 100
    guess = random.randint(lower, upper)


    while True:
        print(f"Is your number {guess}?")
        userResponse = int(input("[1] Too high, [2] Too low, [3] You won!\n"))
        if userResponse == 1:
            upper = guess
        elif userResponse == 2:
            lower = guess
        else:
            print("The computer wins!")
            break
        guess = random.randint(lower, upper)
 
    
    




def main():
    name = input("Howdy, what's your name?\n")
    option = options()

    if option == 1:
        flag = 'y'

        best_scores = []

        while flag == 'y':
            tries = game(name)
            if type(tries) is int:
                best_scores.append(tries)

            flag = input("Would you like to play again? Enter 'y' for yes, enter anything for no\n").lower()

        if len(best_scores) > 0:
            print("best score is: ", min(best_scores))
        else:
            print("you never won")
    else:
        computer()

    



def options():
    return int(input("Enter [1] to guess the number or [2] to have the computer guess your number\n"))


main()




#test