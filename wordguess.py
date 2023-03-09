from termcolor import colored, cprint
import os; clear = lambda: os.system("cls||clear")

class Wordle:
    def __init__(self, word: str, chances=None) -> None:
        if chances is None:
            self.chances = len(word)
        else:
            self.chances = chances
        self.word = word.upper()
        self.history = []

    def __str__(self) -> str:
        colored_history = []
        for guess in self.history:
            colored_guess = ""
            for letter, true_letter in zip(guess, self.word):
                if letter == true_letter:
                    background = "on_green"
                elif letter in self.word:
                    background = "on_yellow"
                else:
                    background = "on_dark_grey"
                letter = " " + letter + " "
                colored_guess += colored(letter, "white", background, attrs=["bold"])
            colored_history.append(colored_guess)
        empty_guesses = self.chances - len(colored_history)
        if empty_guesses > 0:
            empty_line = colored(" - " * len(self.word), "white", "on_dark_grey", attrs=["bold"])
            for _ in range(empty_guesses):
                colored_history.append(empty_line)
        return "\n" + ("\n".join(colored_history)) + "\n"

    def play(self) -> None:
        while True:
            clear()
            print(self)
            guess = input(f"> ").upper()
            while len(guess) != len(self.word):
                clear()
                cprint(f"Guess must have", "yellow", end=" ")
                cprint(f"{len(self.word)}", "blue", attrs=["bold", "underline"], end=" ")
                cprint(f"letters!", "yellow")
                print(self)
                guess = input(f"> ").upper()
            self.history.append(guess)
            if guess == self.word:
                clear()
                cprint("Awesome!", "green", attrs=["bold"])
                print(self)
                break
            if len(self.history) == self.chances:
                clear()
                cprint(f"Game over! Secret word:", color="yellow", end=" ")
                cprint(self.word.title(), "blue", attrs=["bold", "underline"])
                print(self)
                break


if __name__ == "__main__":
    from random import choice
    words = ["young", "study", "table", "local", "money", "heart"]
    Wordle(word=choice(words)).play()
