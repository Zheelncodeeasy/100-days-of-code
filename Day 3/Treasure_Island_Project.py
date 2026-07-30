print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

action = input("You are in a tunnel with your friends."
               "This tunnel has loads of treasure."
               "\nType left or right\n").lower()

if action == "left":
    action = input("You see a lake which might lead to other end\n"
                   "Type swim or wait\n").lower()
    if action == "wait":
        action = input("Now, beside the lake you see "
                       "red, blue and yellow doors\n"
                       "Type red, blue or yellow\n").lower()
        if action == "red":
            print("Sorry, you all get killed by a fire dragon\n"
                  "Game Over")
        elif action == "blue":
            print("Sorry, you all get drowned\n"
                  "Game Over")
        else:
            print("Congratulations! You have found the treasure\n"
                  "You win!")
    else:
        print("Oh no, you are attacked by dangerous monsters\n"
              "Game Over")
else:
    print("It's a dead end\nGame Over")




