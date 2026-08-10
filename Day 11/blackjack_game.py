# import logo from art.py
import art
import random

# list of cards with their respective values
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_score(cards_list):
    # calculate scores
    score = sum(cards_list)

    # If ace in cards and score > 21, then replace with 1 else 11
    while score > 21 and 11 in cards_list:
        cards_list.remove(11)
        cards_list.append(1)
        score = sum(cards_list)
    return score


def play_blackjack():
    # print logo
    print(art.logo)

    # randomly draw 2 cards for user and computer
    user_cards = [random.choice(cards) for _ in range(2)]
    computer_cards = [random.choice(cards) for _ in range(2)]

    game_over = False

    while not game_over:
        final_user_score = calculate_score(user_cards)

        print(f"Your cards: {user_cards}, current score: {final_user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # exit loop when final score is gt or equal to 21
        if final_user_score >= 21:
            game_over = True
        else:
            user_choice = input("Type 'y' for another card, type 'n' to pass: ").strip().lower()
            if user_choice == 'y':
                user_cards.append(random.choice(cards))
            elif user_choice == 'n':
                game_over = True
            else:
                print(f"Please enter either 'y' or 'n'")

    # calculate final scores for user and computer
    final_comp_score = calculate_score(computer_cards)
    final_user_score = calculate_score(user_cards)

    # draw cards until the score is less than 17 and user score is less than equal to 21
    if final_user_score <= 21:
        while final_comp_score < 17:
            computer_cards.append(random.choice(cards))
            final_comp_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}, final score: {final_user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {final_comp_score}")



    if final_user_score == 21 and len(user_cards) == 2:  # this checks if [10,11] == [10,11] -> draw else "blackjack"
        if final_comp_score == 21 and len(computer_cards) == 2:
            print("It's a draw! 🙃") # draw
        else:
            print("You Win with a Blackjack! 😎") # user has a blackjack
    elif final_comp_score == 21 and len(computer_cards) == 2:
        print("Lose, opponent has a Blackjack! 😱") # computer has a blackjack
    elif final_user_score > 21:
        print("You went over. You lose! 😭") # Computer wins
    elif final_comp_score > 21:
        print("Opponent went over. You win! 😁") # User wins
    elif final_user_score == final_comp_score:
        print("It's a draw! 🙃")    # [7,7,7] == [4,7,10] -> Draw
    elif final_user_score > final_comp_score:
        print("You win! 😃")  # User wins
    else:
        print("You lose! 😤") # computer wins



def blackjack_game_start():
    while True:
        # take input from user to play the game
        user_inp = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").strip().lower()
        print("\n" * 50)

        if user_inp == "y":
            play_blackjack()
        elif user_inp == "n":
            break
        else:
            print("Invalid input, please enter 'y' or 'n'")

# start the game
if __name__ == "__main__":
    blackjack_game_start()
