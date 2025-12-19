import random

def number_guessing_game(low=1, high=100, max_attempts=7):
    secret = random.randint(low, high)
    attempts = 0
    print(f"I'm thinking of a number between {low} and {high}. You have {max_attempts} attempts!\n")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts+1}: Your guess? "))
        except ValueError:
            print("Please enter a valid integer (e.g., 23).")
            continue

        attempts += 1

        if guess < low or guess > high:
            print(f"Out of range! Guess between {low} and {high}.")
            continue

        if guess == secret:
            print(f"Congratulations! You guessed the number {secret} in {attempts} attempts 🎉")
            break
        elif guess < secret:
            print("Too low, try a higher number.")
        else:
            print("Too high, try a lower number.")
    else:
        print(f"Sorry, you're out of attempts. The correct number was {secret}.")

if __name__ == "__main__":
    number_guessing_game(low=1, high=100, max_attempts=8)