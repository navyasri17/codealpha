import os
import random
import string

def create_default_words_file():
    default_words = ["python", "hangman", "challenge", "codealpha", "developer"]
    with open('words.txt', 'w') as f:
        f.write('\n'.join(default_words))

def load_words():
    if not os.path.exists('words.txt'):
        print("⚠️ 'words.txt' not found. Creating a default one...")
        create_default_words_file()

    with open('words.txt', 'r') as f:
        return f.read().splitlines()

def play_game():
    words = load_words()
    word = random.choice(words).lower()
    guessed = ['_'] * len(word)
    attempts = 6
    guessed_letters = set()

    print("\n🔤 Welcome to Hangman!\n")
    while attempts > 0 and '_' in guessed:
        print("Word:", ' '.join(guessed))
        print("Guessed letters:", ' '.join(sorted(guessed_letters)))
        guess = input("Enter a letter: ").lower().strip()

        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print("Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
            print("✅ Good guess!")
        else:
            attempts -= 1
            print(f"❌ Wrong guess. Attempts left: {attempts}")

    if '_' not in guessed:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n💀 Out of attempts. The word was:", word)

if __name__ == "__main__":
    play_game()
