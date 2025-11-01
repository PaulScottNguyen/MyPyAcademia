from random import randint #Library that will handle randomness

# Function to generate a random number based on the selected level
def get_secret_number(level):
    if level == 1:
        return randint(0, 10)
    elif level == 2:
        return randint(0, 100)
    elif level == 3:
        return randint(0, 1000)
    else:
        return None  # Invalid level

# Function to handle the guessing game
def guessing_game(secret_number):
    while True:
        TrialCounter = 1
        try:
            guess = int(input("Guess the number: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
        
        if guess > secret_number:
            print("Too high! Try again.")
            TrialCounter+1
        elif guess < secret_number:
            print("Too low! Try again.")
            TrialCounter+1
        else:
            print(f"Just right! You guessed it! The secret number was {secret_number}! You got it in {TrialCounter} times!")
            TrialCounter+1
            break  # Exit the loop when the guess is correct

# Main function to control the game flow
def main():
    try:
        level = int(input("Choose a difficulty level (1-3): "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 3.")
        return main()

    secret_number = get_secret_number(level)

    if secret_number is None:
        print("Invalid level! Please choose between 1 and 3.")
        return main()

    print(f"You chose level {level}. Let's start guessing!")
    guessing_game(secret_number)

if __name__ == "__main__":
    main()