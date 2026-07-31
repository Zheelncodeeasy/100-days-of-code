import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# 0 - rock
# 1 - paper
# 2 - scissors

user_choice = int(input("What do you choose?" 
                        "Type 0 for rock, 1 for paper, 2 for scissors: "))

# generating random integers from 0 to 2 where 0 and 2 are both inclusive
computer_choice = random.randint(0,2)
choices_lst = [rock, paper, scissors]

if user_choice < 0 or user_choice >=3:
    print("The choice is invalid!, Try again.")
elif user_choice == computer_choice:
    print(choices_lst[user_choice])
    print("Computer chose:\n ", choices_lst[computer_choice])
    print("It's a draw!")
elif (
        (user_choice == 0 and computer_choice == 2) or
        (user_choice == 1 and computer_choice == 0) or
        (user_choice == 2 and computer_choice == 1)
    ):
    print(choices_lst[user_choice])
    print("Computer chose:\n", choices_lst[computer_choice])
    print("You Win!")
else:
    print(choices_lst[user_choice])
    print("Computer chose:\n", choices_lst[computer_choice])
    print("You Lose!")







