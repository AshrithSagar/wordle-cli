"""Wordle
"""
import io
import random

def check_guess(word, guess):
    """Returns coloring.
    0: Green, 1: Yellow, 2: Gray"""
    coloring = []
    word_letters = list(word)
    for i in range(5):
        letter = guess[i]
        if letter in word_letters:
            word_letters.remove(letter)
            if letter == word[i]:
                coloring.append(0)
            else:
                coloring.append(1)
        else:
            coloring.append(2)
    return coloring

def main():
    """Main"""
    with io.open('five_letter_words.txt', 'r', encoding='utf8') as file:
        five_letter_words = file.readlines()
    word = random.choice(five_letter_words).rstrip('\n')
    # print("Word: ", word)

    won = False
    state = 1
    while won is False:
        print('Try:', state)
        guess = input()
        if len(guess) != 5:
            print("Try again. Enter 5 letter words.")
            continue
        if guess == word:
            won = True
            print('You win! Guessed it in', state, 'tries!')
            break
        coloring = check_guess(word, guess)
        print(coloring)
        state = state + 1
        if state > 6:
            print("Better luck next time! The word was", word)
            break

main()
