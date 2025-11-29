print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
choice1 = input("You're at a crossroad, where do you want to go? "
                "Type 'Left' or 'Right'.").lower()

if choice1 == "Left":
    choice2 = input("You've come to a lake."
                    "There is an island in the middle of the lake. "
                    "Type 'Wait' to wait for a boat. "
                    "Type 'Swim to swim across.").lower()

    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. "
                        "There is house with 3 doors. One Red, "
                        "One Yellow and One Blue. "
                        "Which color do you choose?").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over")
        elif choice3 == "yellow":
            print("You found the treasure. You win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell in to a hole. Game Over.")
