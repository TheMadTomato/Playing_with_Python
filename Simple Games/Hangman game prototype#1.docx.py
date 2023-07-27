import random
import nltk

# Download the list of English words
nltk.download('words')

# Welcome the player and prepare him to enter
print("Welcome to the hangman game, season1 (^o^)\n What would you like to be called? (>w<)")
name=input(">>>")
print('Hello', name, 'are you ready?')



# the list of words that the game will use
# Load the list of 200000+ English words
words=nltk.corpus.words.words()

# choose a random word from the list
word = words[random.randint(0, len(words) -1)]

# it define the number of allowed incorrect responses
lives = 6

# The first is for correct leter and ther second is for incorrect letter
C_letter = []
I_letter = []

# To track whether the game is over
game_over = False

# Main loop
while not game_over:
 # Display the current state of the word, using underscores for letters that have not been guessed
    display_word = ''
    for letter in word:
        if letter in C_letter:
            display_word += letter
        else:
            display_word += '_'

    # Display your remainig guesses
    print(f'{name} have {lives} lives left. (^—^)')
    print(display_word)

    #aske player to start guessing
    guess = input('Guess a letter ヽ(^o^)丿 : ')

    # Check if the letter is in the wor
    if guess in word:
        # if the letter has already been guessed, display an error message
        # if the letter has not been guessed, add it to the list of correct letter
        if guess in C_letter:
            print('You already guessed that letter. -.-')
        else:
            C_letter.append(guess)

        # check if the player won
            if set(C_letter) == set(word):
                print(f"Congratulation {name}, you won. \(^.^)/")
                game_over = True
    else:
        # if the letter is not in the word, add it to the list of incorrect letters
        # and decrease the number of remaining guesses
        I_letter.append(guess)
        lives -= 1
    if lives == 0:
        print(f"Sorry {name}, You lost. (T^T)")
        game_over = True

# Display the word when the game is over
print(f'{name} the word was {word}')

