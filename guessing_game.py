import random

# Python Web Development Techdegree
# Project 1 - Number Guessing Game

high_score = 10

def start_game():
    print("==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==\n      Welcome to the Number Guessing Game!\n==*==*==*==*==*==*==*==*==*==*==*==*==*==*==*==")
    
    answer = random.randint(1,10)
    guess = int(input("Please enter a number between 1 and 10: "))
    tries = 1
    
    while guess != answer:
        if guess < answer:
            print("It is higher.")
            tries += 1
        elif guess > answer:
            print("It is lower.")
            tries += 1
        guess = int(input("Try again. Please enter a number between 1 and 10: "))
    if guess == answer:
            print("You guessed the number in {} tries!".format(tries))
            if high_score < tries:
                print("The best score is {}".format(high_score))
            elif high_score > tries:
                print("Contratulations! You beat the best score of {}".format(high_score))
                high_score = tries

def restart_game():
    play_again = input("Would you like to play again? (y/n) ")
    if play_again == "y":
        start_game()
    if play_again == "n":
        print("Thanks for playing!")

start_game()
restart_game()