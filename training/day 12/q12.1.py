import random


def guess_game():
    # Generate a random number between 1 and 50
    secret_number = random.randint(1, 50)
    chances = 5

    print("Welcome to the Guess Game!")
    print("Guess a number between 1 and 50. You have 5 chances.")

    while chances > 0:
        try:
            # Get user's guess
            guess = int(input("Enter your guess: "))

            # Check if the guess is within the valid range
            if guess < 1 or guess > 50:
                print("Think in limits 1-50 only!")
                continue

            # Decrement the chances
            chances -= 1

            # Check if the guess is correct
            if guess == secret_number:
                print("Congratulations! You guessed the correct number!")
                return

            # Provide hints based on the guess
            if guess > secret_number:
                print("Hint: Think of a lower number!")
            else:
                print("Hint: Think of a higher number!")

            # Print remaining chances
            print("Chances remaining:", chances)

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print("Out of chances! The secret number was:", secret_number)


# Run the game
guess_game()
