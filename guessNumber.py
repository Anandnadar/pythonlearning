import random

def guessNumber():

    secret_Number = random.randint(1, 100)

    for i in range(1, 3):
        try:
            user_Input = int(input("Enter the number: "))

            if secret_Number == user_Input:
                print("Your number is correct!")
                print(f"You guessed it in {i} attempts")
                break

            elif secret_Number > user_Input:
                print("Number is greater. Try again!")

            elif secret_Number < user_Input:
                print("Number is lesser. Try again!")

        except ValueError:
            print("Please enter a valid number!")
            continue

    else:
        print("Game Over!")
        print(f"You tried {i} times")
        print("Secret number was:", secret_Number)


guessNumber()