"""Wordle
"""
import io
import random
from rich import print as rprint
from rich.console import Console
from rich.text import Text
from rich.panel import Panel

console = Console()

class Wordle():
    """Main class"""
    def __init__(self):
        """Initialise the game"""
        with io.open('five_letter_words.txt', 'r', encoding='utf8') as file:
            self.five_letter_words = file.read().splitlines()
        self.word = random.choice(self.five_letter_words)
        # print("Word: ", self.word)
        self.won = False
        self.state = 1
        self.guesses = []
        self.game_loop()

    def validate(self, guess):
        """Validates guess"""
        coloring = Text()
        word_letters = list(self.word)
        for i in range(5):
            letter = guess[i]
            if letter in word_letters:
                word_letters.remove(letter)
                if letter == self.word[i]:
                    # letter correct
                    coloring.append(letter, style="black on green")
                else:
                    # letter present
                    coloring.append(letter, style="black on yellow")
            else:
                # letter absent
                coloring.append(letter, style="black on gray")
        return coloring

    def game_loop(self):
        """Main game loop"""
        while self.won is False:
            print("-" * 25)
            print('Try:', self.state)
            coloring = Text()
            for guess in self.guesses:
                coloring.append(self.validate(guess))
                coloring.append('\n')
            rprint(Panel(coloring))
            guess = input().lower()
            if len(guess) != 5:
                print("Try again. Enter 5 letter words.")
                continue
            if guess in self.guesses:
                print("You have already guessed that word.")
                continue
            if guess not in self.five_letter_words:
                print("Enter a valid word. Try again.")
                continue
            self.guesses.append(guess)
            if guess == self.word:
                self.won = True
                print('You win! Guessed it in', self.state, 'tries!')
                break
            coloring = self.validate(guess)
            rprint(coloring)
            self.state += 1
            if self.state > 6:
                print("Better luck next time! The word was", self.word)
                break

def main():
    """Main"""
    Wordle()

main()
