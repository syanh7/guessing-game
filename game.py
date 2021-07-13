"""A number-guessing game."""

# Put your code here
import random


name = input("Howdy, what's your name?\n")

print("{}, I'm thinking of a number between 1 and 100".format(name))
print("Try to guess my number")

number = random.randint(1, 101)

guess = -1
tries = 0

while guess != number:
    guess = int(input("Your guess?\n"))
    tries += 1
    if guess < number:
        print("Your guess is too low, try again.")
    elif guess > number:
        print("Your guess is too high, try again.")
    else: 
        print(f"Well done, {name}! You found my number in {tries} tries!")







