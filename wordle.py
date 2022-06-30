"""Wordle
"""
import io
import random
import signal
import sys
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
        self.alphabets = "abcdefghijklmnopqrstuvwxyz"
        self.word = self.won = self.state = self.guesses = self.clues = None

    def color(self, guess):
        """Validates guess"""
        coloring = Text()
        word_letters = list(self.word)
        for i in range(5):
            letter = guess[i]
            if letter in word_letters:
                word_letters.remove(letter)
                if letter == self.word[i]:
                    self.clues['correct'].append(letter)
                    coloring.append(letter, style="black on green")
                else:
                    self.clues['present'].append(letter)
                    coloring.append(letter, style="black on yellow")
            else:
                self.clues['absent'].append(letter)
                coloring.append(letter, style="black on gray")
        return coloring

    def keyboard(self):
        """Return coloring of the alphabets"""
        coloring = Text()
        for letter in self.alphabets:
            if letter in self.clues['correct']:
                coloring.append(letter, style="black on green")
            elif letter in self.clues['present']:
                coloring.append(letter, style="black on yellow")
            elif letter in self.clues['absent']:
                coloring.append(letter, style="black on gray")
            else:
                coloring.append(letter, style="black on white")
        return coloring

    def panel(self):
        """Show a colored panel"""
        coloring = Text()
        for guess in self.guesses:
            coloring.append(self.color(guess))
            coloring.append('\n')
        return Panel.fit(coloring,
            title="Wordle",
            subtitle="Try:"+str(self.state))

    def begin(self, show=False):
        """Begin"""
        self.word = random.choice(self.five_letter_words)
        rprint("Word:", self.word)
        if show is True:
            input()
        self.won = False
        self.state = 1
        self.guesses = []
        self.clues = {'correct':[], 'present':[], 'absent':[]}
        self.game_loop()

    def game_loop(self):
        """Main game loop"""
        endtitles = Text()
        with console.screen() as screen:
            while True:
                screen.update(self.panel())
                rprint(self.keyboard())
                rprint(endtitles)
                guess = input().lower()
                if self.won:
                    break
                else:
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
                        if self.state == 1:
                            endtitles.append('You win! Guessed it in 1 try!')
                        else:
                            endtitles.append('You win! Guessed it in '
                                + str(self.state)
                                + ' tries!')
                        continue
                    self.state += 1
                    if self.state > 6:
                        self.state = 6
                        self.won = True
                        endtitles.append("Better luck next time! The word was "
                            + str(self.color(self.word)))

def signal_handler(sig, frame):
    """Signal handler"""
    del sig, frame
    sys.exit(0)

def main():
    """Main"""
    signal.signal(signal.SIGINT, signal_handler)

    game = Wordle()
    game.begin()

main()
