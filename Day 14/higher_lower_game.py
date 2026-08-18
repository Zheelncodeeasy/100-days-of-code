# import libraries
from art import logo, vs
from game_data import data
from random import choice

# fetch data
def get_data():
    """ Returns random game_data"""
    return choice(data)

# def format data
def format_data(item):
    """Returns formatted data"""
    return f"{item['name']}, a {item['description']}, from {item['country']}"

# check result
def check_result(a_followers_count:int, b_followers_count:int, user_guess:str):
    """Returns True if user guesses correct"""
    if a_followers_count > b_followers_count:
        return user_guess == "a"
    elif a_followers_count < b_followers_count:
        return user_guess == "b"
    return False

# take user input
def game():

    # initialising variables
    score = 0

    # flag
    game_over = False

    a = get_data()
    b = get_data()

    # keep running until game over
    while not game_over:

        # replace a with b and fetch new data for b
        if score > 0:
            a = b
            b = get_data()

        # check for duplicate data for a and b
        while b == a:
            b = get_data()

        print("\n" * 30)
        print(logo)

        # print statement when score greater than 0
        if score > 0:
            print(f"You are right. Your current score is {score}")

        # print formatted data
        print(f"Compare A: {format_data(a)}")
        print(vs)
        print(f"Against B: {format_data(b)}")

        # ask for user input
        user_inp = input("Choose your answer: Type 'A' or 'B': ").strip().lower()

        # store the follower count
        a_followers = a["follower_count"]
        b_followers = b["follower_count"]

        # check result
        is_correct = check_result(a_followers, b_followers, user_inp)

        # increase the score if the guess is correct else break
        if is_correct:
            score += 1
        else:
            print("\n" * 30)
            print(logo)
            print(f"I am sorry, you are wrong. Final score is {score}")
            game_over = True


if __name__ == "__main__":
    game()













