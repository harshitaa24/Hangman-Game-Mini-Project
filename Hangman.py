import tkinter as tk
from tkinter import messagebox
import random

# Word dictionary with hints
words = {
    'adventure': 'I take you far, through risk and thrill',
    'spaceship': 'I leave the ground on a cosmic trip.',
    'magnetism': 'I pull with force you cannot see',
    'feedback': 'You say what’s right — or what went wrong',
    'nightmare': 'I haunt your dreams, then fade by dawn.',
    'headline': 'I shout the news in bold up top.',
    'checkmate': 'Game is done — the king can’t run',
    'playground': 'I am fun and loud, with slides and swings.',
    'slideshow': 'Pictures change with every click.',
    'starfish': 'I live in seas with arms, not fists.',
    'roadtrip': 'A car, a map, adventure lists.',
    'clockwise': 'I spin the way most hands agree.',
    'fireplace': 'I crackle warm, where stories be.',
    'crossword': 'Words in grids, both down and right.',
    'seaplane': 'I land on waves, then fly again.'
}

# Random word selection
secretWord, hint = random.choice(list(words.items()))
guessedWord = ['_'] * len(secretWord)
guesses = []
remainingTries = 6

# Hangman drawing
hangman_drawing = [
    "   ________ ",
    "  |/      | ",
    "  |       O ",
    "  |      /|\\",
    "  |      / \\",
    "  |",
    "  |"
]


def update_guessedWord(guess):
    global guessedWord
    for i in range(len(secretWord)):
        if secretWord[i] == guess:
            guessedWord[i] = guess


def make_a_guess():
    global remainingTries

    guess = guess_entry.get().lower()

    if len(guess) != 1 or not guess.isalpha():
        messagebox.showwarning("Invalid Input", "Please enter a single letter.")
        return

    if guess in guesses:
        messagebox.showwarning("Already guessed", f"You already guessed '{guess}'.")
        return

    guesses.append(guess)

    if guess in secretWord:
        update_guessedWord(guess)
    else:
        remainingTries -= 1

    word_label.config(text=" ".join(guessedWord))
    tries_label.config(text=f"Tries Remaining: {remainingTries}")
    hangman_label.config(text="\n".join(hangman_drawing[:6 - remainingTries]))

    if remainingTries == 0:
        window.configure(bg="#F74937")
        messagebox.showinfo("Game Over", f"Oops! Game over. The word was '{secretWord}'.")
        reset_game()

    elif '_' not in guessedWord:
        window.configure(bg="#4BF53A")
        messagebox.showinfo("You Win!", "Congratulations! You've guessed the word.")
        reset_game()

    guess_entry.delete(0, tk.END)


def reset_game():
    global secretWord, guessedWord, guesses, remainingTries, hint

    window.configure(bg="white")

    secretWord, hint = random.choice(list(words.items()))
    guessedWord = ['_'] * len(secretWord)
    guesses = []
    remainingTries = 6

    word_label.config(text=" ".join(guessedWord))
    tries_label.config(text=f"Tries Remaining: {remainingTries}")
    hangman_label.config(text="\n".join(hangman_drawing[:remainingTries]))
    hint_label.config(text=f"Hint: {hint}")


# GUI
window = tk.Tk()
window.title("Hangman Game")
window.configure(bg="white")

hint_label = tk.Label(window, text=f"Hint: {hint}", font=('Helvetica', 14, 'italic'))
hint_label.pack(pady=5)

word_label = tk.Label(window, text=" ".join(guessedWord), font=('Helvetica', 16))
word_label.pack(pady=20)

tries_label = tk.Label(window, text=f"Tries Remaining: {remainingTries}", font=('Helvetica', 14))
tries_label.pack(pady=10)

guess_entry = tk.Entry(window, font=('Helvetica', 14))
guess_entry.pack(pady=20)

guess_button = tk.Button(window, text="Guess", font=('Helvetica', 14),
                         command=make_a_guess, bg="#00BFFF")
guess_button.pack(pady=10)

hangman_label = tk.Label(window,
                         text="\n".join(hangman_drawing[:remainingTries]),
                         font=('Courier', 12))
hangman_label.pack(pady=20)

window.mainloop()
