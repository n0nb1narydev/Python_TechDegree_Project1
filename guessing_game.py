import random

# Python Web Development Techdegree
# Project 1 - Number Guessing Game

best = 10

def start_game(best_score):
    print("==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==\n      Welcome to the Number Guessing Game!\n==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==")
    print("Can you beat the best score of {} guesses?".format(best_score))
    answer = random.randint(1,10)
    tries = 0
    guess = 0
    

    while guess != answer:
        try:
            guess = int(input("Please enter a number between 1 and 10: "))
            if guess > 10 or guess < 1:
                raise ValueError("Enter a valid number between 1 and 10")

        except ValueError as err:
            print("Enter a valid number between 1 and 10")
        else:
            if guess < answer:
                print("It is higher.")
            elif guess > answer:
                print("It is lower.")
            tries += 1    

    if guess == answer:
        print("You guessed the number in {} tries!".format(tries))
        if best_score <= tries:
            print("The best score is {}.".format(best_score))
            restart_game(best_score)
        elif best_score > tries:
            print("Contratulations! You beat the best score of {}".format(best_score))
            best = tries
            restart_game(tries)

def restart_game(best_score):
        play_again = input("Would you like to play again? (y/n) ")
        if play_again.lower() == "y":
            start_game(best_score)
        elif play_again.lower() == "n":
            print("Thanks for playing!")
        else:
            print("Please enter a Y for yes or N for no.")
            restart_game(best)

start_game(best)
