"""Wordle
"""
import io
import random
import time
from rich import print as rprint
from rich.console import Console
from rich.text import Text
from rich.panel import Panel

console = Console(height=8)

class Wordle():
    """Main class"""
    def __init__(self):
        """Initialise the game"""
        with io.open('five_letter_words.txt', 'r', encoding='utf8') as file:
            self.five_letter_words = file.read().splitlines()
        self.word = self.won = self.state = self.guesses = None

    def color(self, guess):
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

    def panel(self):
        """Show a colored panel"""
        coloring = Text()
        for guess in self.guesses:
            coloring.append(self.color(guess))
            coloring.append('\n')
        return Panel.fit(coloring, title="Wordle", subtitle="Try:"+str(self.state))

    def begin(self, show=False):
        """Begin"""
        self.word = random.choice(self.five_letter_words)
        if show is True:
            print("Word: ", self.word)
            input()
        self.won = False
        self.state = 1
        self.guesses = []
        self.game_loop()

    def game_loop(self):
        """Main game loop"""
        with console.screen() as screen:
            while self.won is False:
                screen.update(self.panel())
                guess = input().lower()
                if len(guess) != 5:
                    rprint("Try again. Enter 5 letter words.")
                    continue
                if guess in self.guesses:
                    rprint("You have already guessed that word.")
                    continue
                if guess not in self.five_letter_words:
                    rprint("Enter a valid word. Try again.")
                    continue
                self.guesses.append(guess)
                if guess == self.word:
                    self.won = True
                    rprint('You win! Guessed it in', self.state, 'tries!')
                    break
                self.state += 1
                if self.state > 6:
                    rprint("Better luck next time! The word was", self.color(self.word))
                    break
            input()

def main():
    """Main"""
    game = Wordle()
    game.begin()

main()
