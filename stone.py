# 1. Game requirements
# Objective: The user plays against the computer.
# 1. Ask the user to select Stone, Paper or Scissors.
# 2. Computer randomly selects one option.
# 3. Display both selections.
# 4. Compare the selections and decide the winner.
# 5. Display whether the user wins, loses or draws.
# 6. Ask whether the user wants to play again.

import random

def stonePaperScissors():

    choices = ["stone", "paper", "scissors"]

    while True:

        user_choice = input("Enter stone, paper or scissors: ").lower()

        if user_choice not in choices:
            print("Invalid choice!")
            continue

        computer_choice = random.choice(choices)

        print("Your choice:", user_choice)
        print("Computer choice:", computer_choice)

        if user_choice == computer_choice:
            print("Match Draw!")

        elif (
            (user_choice == "stone" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "stone") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win!")

        else:
            print("Computer wins!")

        play_again = input("Do you want to play again? (yes/no): ").lower()

        if play_again == "no":
            print("Thanks for playing!")
            break

        elif play_again == "yes":
            continue

        else:
            print("Invalid input. Exiting game!")
            break


stonePaperScissors()