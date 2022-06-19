"""Wordle
"""
import io
import random
import rich

class Wordle():
    """Main class"""
    @staticmethod
    def letter_correct(letter):
        """Return green letter"""
        return f'[black on green]{letter}[/]'

    @staticmethod
    def letter_present(letter):
        """Return yellow letter"""
        return f'[black on yellow]{letter}[/]'

    @staticmethod
    def letter_absent(letter):
        """Return gray letter"""
        return f'[black on gray]{letter}[/]'

    def validate(self, guess):
        """Validates guess"""
        coloring = []
        word_letters = list(self.word)
        for i in range(5):
            letter = guess[i]
            if letter in word_letters:
                word_letters.remove(letter)
                if letter == self.word[i]:
                    coloring.append(self.letter_correct(letter))
                else:
                    coloring.append(self.letter_present(letter))
            else:
                coloring.append(self.letter_absent(letter))
        return coloring

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

    def game_loop(self):
        """Main game loop"""
        while self.won is False:
            print("-" * 25)
            print('Try:', self.state)
            for guess in self.guesses:
                coloring = self.validate(guess)
                rich.print(''.join(coloring))
            guess = input()
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
            rich.print(''.join(coloring))
            self.state += 1
            if self.state > 6:
                print("Better luck next time! The word was", self.word)
                break

def main():
    """Main"""
    Wordle()

main()
