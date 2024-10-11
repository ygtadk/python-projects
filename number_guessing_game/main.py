import random
import math

def number_guessing_game():
    """
    It plays a game of guessing a number in the range specified by the user.
    It shows in how many attempts you guessed correctly and gives you choice of guess limit.
    """

    # Get limits from user input
    lower_limit = int(input("> Enter the lower limit of the range : "))
    upper_limit = int(input("> Enter the upper limit of the range : "))

    # Check correctness of limits
    if lower_limit >= upper_limit:
        print("- Limits must be defined differently and from smallest to largest.")
        exit()

    # Define variables
    random_number = random.randint(lower_limit, upper_limit)
    guess = 0
    number_of_tries = 0

    print(f"- OK! I kept a number between {lower_limit} and {upper_limit}.")

    # Define a loop for compare guessed number and kept number
    while guess != random_number:
        number_of_tries += 1
        # Get guess from user input
        guess = int(input("> Your guess is : "))

        if guess < random_number:
            print("- Try Again! You guessed too small.")
        elif guess > random_number:
            print("- Try Again! You guessed too high.")
        elif guess < lower_limit or guess > upper_limit:
            print("- Your guess must be within limits.")

    print(f"- Congratulations, correct guess! You found the number {random_number} in {number_of_tries} tries.")
    
    # Bonus challenge ; machine tells you the minimum number of guess
    print(f"- Also I thought you would succeed after {int(math.floor(math.log(upper_limit - lower_limit + 1, 2.0)))} guesses.\n")

# Call the function and play game
if __name__ == "__main__":
    number_guessing_game()