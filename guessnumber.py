# The program works as follows:
# you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive).
# The computer makes guesses, and you give it input - is its guess too high or too low?
# Using bisection search, the computer will guess the user's secret number!
import math

low = 0
high = 100
guess = math.ceil((high + low) / 2)
print("Please think of a number between 0 and 100!")

while True:
    print ("Is your secret number " + str(guess) + '?')
    x = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if x == 'c':
        print("Game over. Your secret number was: " + str(guess))
        break
    elif x == 'h':
        high = guess
        guess = math.ceil((high + low) / 2)
    elif x == 'l':
        low = guess
        guess = math.ceil((high + low) / 2)
    else:
        print("Sorry, I did not understand your input.")
