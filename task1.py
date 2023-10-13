#!python3

'''
Create a number guessing game
There is a limit of 10 guesses
The program will ask the user to enter an integer from 1 to 100
The program will then tell the user if the number is too high, too low or correct.
If the number is correct, the program will end
If the 10 guesses are used up, the program will say that the user has lost
'''
import random
number = random.randint(1,100)

q = "Guess a number between 1 and 100: "
for total_guesses in range(10):
    guess = int(input(q))
    if guess < number:
        print("Your number was too low, guess again")
    elif guess > number:
        print("Your number was too high, guess again")
    else:
        break
if guess == number:
    print("Your guess was correct")

print("you ran out of tries.")
