import random
import tkinter as tk
from tkinter import messagebox


def choose_word():
    words = ["apple", "banana", "orange", "grape", "watermelon", "pineapple", "strawberry"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        elif len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts left.")
            if attempts == 0:
                print("Sorry, you ran out of attempts! The word was:", word)
                break
        else:
            print("Correct!")

        displayed = display_word(word, guessed_letters)
        print(displayed)

        if "_" not in displayed:
            print("Congratulations, you guessed the word!")
            break

if __name__ == "__main__":
    hangman()
class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.word = self.choose_word()
        self.guessed_letters = []
        self.attempts = 6

        self.displayed_word = tk.StringVar()
        self.displayed_word.set(self.display_word())

        self.label_word = tk.Label(master, textvariable=self.displayed_word, font=("Arial", 24))
        self.label_word.pack(pady=10)

        self.entry_guess = tk.Entry(master, font=("Arial", 18))
        self.entry_guess.pack(pady=5)

        self.button_guess = tk.Button(master, text="Guess", font=("Arial", 18), command=self.make_guess)
        self.button_guess.pack(pady=5)

    def choose_word(self):
        words = ["apple", "banana", "orange", "grape", "watermelon", "pineapple", "strawberry"]
        return random.choice(words)

    def display_word(self):
        displayed_word = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                displayed_word += letter
            else:
                displayed_word += "_"
        return displayed_word

    def make_guess(self):
        guess = self.entry_guess.get().lower()
        self.entry_guess.delete(0, tk.END)

        if guess in self.guessed_letters:
            messagebox.showwarning("Warning", "You already guessed that letter!")
            return
        elif len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Warning", "Please enter a single letter.")
            return

        self.guessed_letters.append(guess)

        if guess not in self.word:
            self.attempts -= 1
            if self.attempts == 0:
                messagebox.showinfo("Game Over", f"Sorry, you ran out of attempts! The word was: {self.word}")
                self.master.destroy()
            else:
                messagebox.showinfo("Incorrect", f"Incorrect! You have {self.attempts} attempts left.")
        else:
            messagebox.showinfo("Correct", "Correct!")

        self.displayed_word.set(self.display_word())

        if "_" not in self.displayed_word.get():
            messagebox.showinfo("Congratulations", "Congratulations, you guessed the word!")
            self.master.destroy()

def main():
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
