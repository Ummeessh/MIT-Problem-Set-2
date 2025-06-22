# Problem Set 2, hangman.py
# Name: Umesh Pariyar
# Collaborators: None
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True
    


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for letter in secret_word:
        if letter not in letters_guessed:
            secret_word = secret_word.replace(letter, "*")
    return secret_word


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    return "".join(letter for letter in string.ascii_lowercase if letter not in letters_guessed)

def get_valid_letter(secret_word, letters_guessed):
    hint_letters = [letter for letter in secret_word if letter not in letters_guessed]

    return random.choice(hint_letters) if hint_letters else None

def check_guess(secret_word, guess):
    return True if guess in secret_word else False

def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print(f"Welcome to Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    
    guess_count = 10
    guess_list = []
    while True:
        guess = ""

        available_letters = get_available_letters(guess_list)

        print("-"*6)

        if has_player_won(secret_word, guess_list):
            total_score = ( guess_count + 4 * len(set(get_word_progress(secret_word, guess_list))) + (3 * len(secret_word)) )
            print("Congratulations, you won!")
            print(f"Your total score for this game is: {total_score}")
            break
        elif guess_count == 0:
            print(f"Sorry you ran out of guesses. The word was {secret_word}")
            break

        print(f"You have {guess_count} guesses left.")
        print(f"Available letters: {available_letters}")

        guess = input("Please guess a letter: ").lower()

        if not guess.isalpha() and guess != "!":
            print(f"Oops! That is not a valid letter. Please input a letter from the alphabet: {get_word_progress}") 
            continue
        
        if guess in guess_list:
            print(f"You have already guessed this before.")
            continue

        if with_help and guess == "!":
            help_letter = get_valid_letter(secret_word, guess_list)
            guess_count -= 3
            print(f"Letter revealed: {help_letter}")
            guess_list.append(help_letter)
            print(get_word_progress(secret_word, guess_list))
          
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
        
        

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.
    # secret_word = "hi"
    # with_help = False
    # hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass