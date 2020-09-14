import random

# Python Web Development Techdegree
# Project 1 - Number Guessing Game

best = 10

def start_game(best_score):
    print("==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==\n      Welcome to the Number Guessing Game!\n==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==")
    
    answer = random.randint(1,10)
    guess = int(input("Please enter a number between 1 and 10: "))
    tries = 1

    while guess != answer:
        if guess < answer:
            print("It is higher.")
        elif guess > answer:
            print("It is lower.")
        tries += 1
        guess = int(input("Try again. Please enter a number between 1 and 10: "))
    
    if guess == answer:
        print("You guessed the number in {} tries!".format(tries))
        if best_score < tries:
            print("The best score is {}".format(best_score))
            restart_game(best_score)
        elif best_score > tries:
            print("Contratulations! You beat the best score of {}".format(best_score))
            best = tries
            restart_game(tries)

def restart_game(best_score):
    play_again = input("Would you like to play again? (y/n) ")
    try:
        if play_again.lower() == "y":
            start_game(best_score)
        if play_again.lower() == "n":
            print("Thanks for playing!")
    except ValueError:
        print("Oh no! You did not enter a Y or N")

start_game(best)
