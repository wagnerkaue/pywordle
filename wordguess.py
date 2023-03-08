from random import choice
from termcolor import colored, cprint
import os
clear =  lambda: os.system('cls||clear')

def formatted(guess: str, word: str):
    guess = guess.upper()
    word  = word.upper()
    formatted = ""
    for letter, true_letter in zip(guess, word):
        if letter == true_letter:
            background = "on_green"
        elif letter in word:
            background = "on_yellow"
        else:
            background = "on_dark_grey"
        letter = " " + letter + " "
        formatted += colored(text=letter, color='white', on_color=background, attrs=['bold'])
    return formatted

def display(history, word, chances):
    print()
    for guess in history:
        print(formatted(guess, word))
    empty_words = chances - len(history)
    if empty_words > 0:
        for _ in range(empty_words):
            print(formatted('-' * len(word), word))
    print()


def wordguess(word: str, chances: int):
    clear()
    history = []
    while True:
        display(history, word, chances)
        guess = input(f'> ')
        while len(guess) != len(word):
            clear()
            cprint(f"Word must have", "red", attrs=['bold'], end=' ')
            cprint(f"{len(word)}", 'yellow', attrs=['bold'], end=' ')
            cprint(f"letters!", "red", attrs=['bold'])
            display(history, word, chances)
            guess = input(f'> ')
        history.append(guess)
        clear()
        if guess == word:
            match len(history):
                case 1:
                    message = "Now that's what i'm talking about!"
                case 2:
                    message = "Awesome!"
                case 3:
                    message = "Fantastic!"
                case 4:
                    message = "Nice!"
                case 5:
                    message = "Phew!"
            cprint(message, "green", attrs=["bold"])
            display(history, word, chances)
            break
        if len(history) == chances: 
            cprint(f"Game over! Secret word:", color="red", attrs=["bold"], end=" ")
            cprint(word.title(), "yellow", attrs=["bold", "underline"])
            display(history, word, chances)
            break

if __name__ == "__main__":
    from random import choice
    words = ['senso', 'nobre', 'sutil', 'poder', 'moral', 'casal', 'ideia']
    play_again = True
    while play_again:
        wordguess(choice(words), 5)
        again = input("[Y/N] Play again? ").upper()
        if again in ("N", "NO"):
            play_again = False
        else:
            play_again = True
