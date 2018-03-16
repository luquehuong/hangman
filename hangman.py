# Name:
# Section:
# 6.189 Project 1: Hangman template
# hangman_template.py

# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *
from hangman_lib import print_hangman_image
from os import sys, system

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

# actually load the dictionary of words and point to it with
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[randrange(0,len(words_dict))]
    return word

# end of helper code
# -----------------------------------


# CONSTANTS
#MAX_GUESSES = len(get_word())

# GLOBAL VARIABLES
secret_word = get_word()

EXTRA_GUESSES = 6
MAX_GUESSES = len(secret_word) + EXTRA_GUESSES
letters_guessed = []

# From part 3b:
def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    ####### YOUR CODE HERE ######
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

def print_guessed():
    '''
    Prints out the characters you have guessed in the secret word so far
    '''
    global secret_word
    global letters_guessed

    ####### YOUR CODE HERE ######
    print_letters = ""
    for letter in secret_word:
        if letter in letters_guessed:
            print_letters += letter
        else:
            print_letters += "-"
    return print_letters

def is_input_letter_valid(input_letter):
    if input_letter not in letters_guessed:
        if input_letter.isalpha() and len(input_letter) == 1:
            return True
        else:
            print("Please enter only one alphabetical letter.")
            return False
    else:
        print("You have guessed this letter already. Choose another one.")
        return False

#V: nested call
def play_new_game():
    global secret_word
    global letters_guessed

    while True:
        system('clear')

        new_game = input("Enter 'Y' if you want to play new game, press any key to exit... ")
        if new_game.lower() == 'y':
            print("""
                                        -------------------
            """)

            secret_word = get_word()
            letters_guessed = []

            play_hangman()
        else:
            break

def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    global MAX_GUESSES

    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0
    # V: const
    # V: need both?
    AVAILABLE_GUESSES = MAX_GUESSES

    # V: magic number 6
    print("My secret word has", len(secret_word), "letters. You have maximum", len(secret_word) + 6, "guesses.")

    for guess in range(0, MAX_GUESSES):
        input_letter = input("Guess one letter: ")
        # V: not
        # V: good func
        while not is_input_letter_valid(input_letter):
            input_letter = input("Guess one letter: ")
        letters_guessed.append(input_letter.lower())

        print(print_guessed())

        if letters_guessed[guess] not in secret_word:
            mistakes_made += 1
            print(print_hangman_image(mistakes_made))
            #V: requirement
            if mistakes_made == 6:
                print("You lose! The secret word is " + "'" + secret_word + "'.")
                return

        if word_guessed():
            print("Congratulations! Your guesses is exactly! The secret word is " + "'" + secret_word + "'.")
            return

        AVAILABLE_GUESSES -= 1
        print("You have", AVAILABLE_GUESSES, "guesses left.")

        if AVAILABLE_GUESSES == 0:
            print("You lose! The secret word is " + "'" + secret_word + "'.")
            return

play_new_game()

# play_new_game
# play_hangman
