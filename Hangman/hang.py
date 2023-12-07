import random

def choose_word():
    words = ['apple', 'banana', 'orange', 'grape', 'strawberry', 'watermelon', 'kiwi', 'peach']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"Attempts left: {attempts}")
            if attempts == 0:
                print("You're out of attempts! The word was:", word)
                break
        else:
            print("Good job! That letter is in the word.")
        
        word_display = display_word(word, guessed_letters)
        print(word_display)

        if '_' not in word_display:
            print("Congratulations! You guessed the word:", word)
            break

if __name__ == "__main__":
    hangman()
