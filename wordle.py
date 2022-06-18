"""Wordle
"""
import io
import random
import rich

def letter_green(letter):
    """Return green letter"""
    return f'[black on green]{letter}[/]'

def letter_yellow(letter):
    """Return yellow letter"""
    return f'[black on yellow]{letter}[/]'

def letter_gray(letter):
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
                coloring.append(letter_green(letter))
            else:
                coloring.append(letter_yellow(letter))
        else:
            coloring.append(letter_gray(letter))
    return coloring

def main():
    """Main"""
    with io.open('five_letter_words.txt', 'r', encoding='utf8') as file:
        five_letter_words = file.read().splitlines()
    word = random.choice(five_letter_words)
    # print("Word: ", word)

    won = False
    state = 1
    guesses = []
    while won is False:
        print('Try:', state)
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

main()
