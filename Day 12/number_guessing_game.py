from random import randint
import art

#global constants
EASY_LEVEL_TRIES = 10
HARD_LEVEL_TRIES = 5

def guess_number(num_to_guess: int, tries: int):
    """
    prints whether the number guessed is correct, high or low.
    """
    while tries > 0:
        print(f"You have {tries} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        # checks whether your guess matches the guessed_number
        if guess > num_to_guess:
            print("Too high!")
            print("Guess again.")
        elif guess < num_to_guess:
            print("Too low!")
            print("Guess again.")
        else:
            print(f"You Got it. The number was {num_to_guess}")
            break
        tries -= 1

    if tries == 0:
        print("You have completed all attempts, try again!")
        print(f"The number to be guessed was {num_to_guess}")


def number_guessing_game():
    """
    this function starts the number guessing game
    """
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # generates random numbers between 1 and 100
    number_to_guess = randint(1, 100)

    # two levels : easy and hard
    choice = input("Choose a difficult. Type 'easy' or 'hard': ").strip().lower()

    if choice == "easy":
    # number of attempts to guess : easy level
        guess_number(number_to_guess,  EASY_LEVEL_TRIES)
    elif choice == "hard":
        guess_number(number_to_guess, HARD_LEVEL_TRIES)
    else:
        print("Kindly provide a valid input.")


if __name__ == "__main__":
    number_guessing_game()