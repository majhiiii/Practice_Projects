import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    secret_number = random.randint(1, 100)  # Generate a random number between 1 and 100 orelse your can your desired number
    attempts = 0
    
    while True:
        guess = int(input("Enter your guess (between 1 and 100): "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts!")
            break

if __name__ == "__main__":
    number_guessing_game()
