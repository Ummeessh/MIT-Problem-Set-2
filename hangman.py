# Problem Set 2, hangman.py
# Name: Umesh Pariyar
# Collaborators: None
# Time spent:

import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    return random.choice(wordlist)

wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

def get_word_progress(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            secret_word = secret_word.replace(letter, "*")
    return secret_word

def get_available_letters(letters_guessed):
    return "".join(letter for letter in string.ascii_lowercase if letter not in letters_guessed)

def get_valid_letter(secret_word, letters_guessed):
    hint_letters = [letter for letter in secret_word if letter not in letters_guessed]
    return random.choice(hint_letters) if hint_letters else None

def check_guess(secret_word, guess):
    return True if guess in secret_word else False

def hangman(secret_word, with_help):
    print(f"Welcome to Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    
    guess_count = 10
    guess_list = []

    while True:
        guess = ""
        available_letters = get_available_letters(guess_list)
        progress = get_word_progress(secret_word, guess_list)
        print("-" * 10)

        if has_player_won(secret_word, guess_list):
            total_score = ( guess_count + 4 * len(set(get_word_progress(secret_word, guess_list))) + (3 * len(secret_word)) )
            print("Congratulations, you won!")
            print(f"The word was: {secret_word}")
            print(f"Your total score for this game is: {total_score}")
            break
        elif guess_count == 0:
            print(f"Sorry, you ran out of guesses. The word was '{secret_word}'.")
            break

        print(f"You have {guess_count} guesses left.")
        print(f"Available letters: {available_letters}")
        print(f"Current progress: {progress}")

        guess = input("Please guess a letter (or '!' for a hint): ").lower()

        if not guess.isalpha() and guess != "!":
            print("Oops! That is not a valid letter. Please input a letter.")
            continue

        if guess in guess_list:
            print("You have already guessed this before.")
            continue

        if with_help and guess == "!":
            help_letter = get_valid_letter(secret_word, guess_list)
            if help_letter:
                print(f"Letter revealed: {help_letter}")
                guess_list.append(help_letter)
                guess_count -= 3
            else:
                print("No more letters to reveal.")
            continue

        if guess != "!":
            guess_list.append(guess)
            progress = get_word_progress(secret_word, guess_list)

            if check_guess(secret_word, guess):
                print(f"Good guess: {progress}")
            else:
                print(f"Oops! That letter is not in my word: {progress}")
                if guess in "aeiou":
                    guess_count -= 2
                else:
                    guess_count -= 1

if __name__ == "__main__":
    # secret_word = "hi"
    # with_help = False
    # hangman(secret_word, with_help)
    pass