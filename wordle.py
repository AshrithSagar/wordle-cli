"""Wordle
"""
import io
import random
import rich

def letter_correct(letter):
    """Return green letter"""
    return f'[black on green]{letter}[/]'

def letter_present(letter):
    """Return yellow letter"""
    return f'[black on yellow]{letter}[/]'

def letter_absent(letter):
    """Return gray letter"""
    return f'[black on gray]{letter}[/]'

def check_guess(word, guess):
    """Validates guess"""
    coloring = []
    word_letters = list(word)
    for i in range(5):
        letter = guess[i]
        if letter in word_letters:
            word_letters.remove(letter)
            if letter == word[i]:
                coloring.append(letter_correct(letter))
            else:
                coloring.append(letter_present(letter))
        else:
            coloring.append(letter_absent(letter))
    return coloring

def game_start():
    """Initialise the game"""
    with io.open('five_letter_words.txt', 'r', encoding='utf8') as file:
        five_letter_words = file.read().splitlines()
    word = random.choice(five_letter_words)
    # print("Word: ", word)
    return five_letter_words, word

def game_loop(five_letter_words, word):
    """Main game loop"""
    won = False
    state = 1
    guesses = []
    while won is False:
        print('Try:', state)
        for guess in guesses:
            coloring = check_guess(word, guess)
            rich.print(''.join(coloring))
        guess = input()
        if len(guess) != 5:
            print("Try again. Enter 5 letter words.")
            continue
        if guess in guesses:
            print("You have already guessed that word.")
            continue
        if guess not in five_letter_words:
            print("Enter a valid word. Try again.")
            continue
        guesses.append(guess)
        if guess == word:
            won = True
            print('You win! Guessed it in', state, 'tries!')
            break
        coloring = check_guess(word, guess)
        rich.print(''.join(coloring))
        state = state + 1
        if state > 6:
            print("Better luck next time! The word was", word)
            break

def main():
    """Main"""
    five_letter_words, word = game_start()
    game_loop(five_letter_words, word)

main()
