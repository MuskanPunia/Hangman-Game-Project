import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hangman Game")
        self.geometry("500x600")
        self.configure(bg="#ADD8E6")  # Set background color to light blue

        self.canvas = tk.Canvas(self, bg="#ADD8E6", width=300, height=300)  # Reduced canvas height
        self.canvas.pack(pady=20)

        self.themes = {
            "Colors": ["red", "blue", "green", "yellow", "orange", "purple", "black", "white"],
            "Animals": ["lion", "elephant", "tiger", "giraffe", "zebra", "monkey", "panda", "koala"],
            "Countries": ["Chile", "Brazil", "Norway", "Denmark", "Serbia", "Mexico", "Canada", "Japan"],
            "Flowers": ["rose", "tulip", "daisy", "sunflower", "lily", "orchid", "daffodil", "peony"],
            "Planets": ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"],
            "Companies": ["apple", "google", "amazon", "facebook", "microsoft", "tesla", "netflix", "ibm"],
            "Medical Science": ["anatomy", "biology", "chemistry", "physiology", "pharmacology", "genetics", "pathology", "immunology"],
            "Politics": ["democracy", "republic", "president", "parliament", "election", "government", "politics", "legislation"],
            "Commerce": ["market", "trade", "economy", "finance", "investment", "business", "entrepreneur", "consumer"]
        }

        self.selected_theme = ""
        self.word = ""
        self.remaining_attempts = 6
        self.guessed_letters = []

        self.create_widgets()

    def create_widgets(self):
        self.theme_label = tk.Label(self, text="Select a theme:", font=("Arial", 18, "bold"), bg="#ADD8E6", fg="#FFFFFF")
        self.theme_label.pack(pady=10)

        self.theme_buttons_frame = tk.Frame(self, bg="#ADD8E6")
        self.theme_buttons_frame.pack()

        for theme in self.themes:
            tk.Button(self.theme_buttons_frame, text=theme, font=("Arial", 12), bg="#FF4500", fg="#FFFFFF",
                      activebackground="#FFA500", activeforeground="#FFFFFF",
                      width=10, height=1,
                      command=lambda t=theme: self.select_theme(t)).pack(side=tk.LEFT, padx=5, pady=5)

        self.word_label = tk.Label(self, text="", font=("Arial", 24), bg="#ADD8E6", fg="#FFFFFF")
        self.word_label.pack(pady=20)

        self.remaining_attempts_label = tk.Label(self, text="", font=("Arial", 14), bg="#ADD8E6", fg="#FFFFFF")
        self.remaining_attempts_label.pack(pady=5)

        self.keyboard_frame = tk.Frame(self, bg="#ADD8E6")
        self.keyboard_frame.pack(pady=10)  # Reduced padding

        for char in "abcdefghijklmnopqrstuvwxyz":
            tk.Button(self.keyboard_frame, text=char.upper(), font=("Arial", 12), bg="#FFA500", fg="#000000",
                      activebackground="#FFD700", activeforeground="#000000",
                      width=3, height=1,
                      command=lambda c=char: self.guess_letter(c)).pack(side=tk.LEFT, padx=5, pady=5)

    def select_theme(self, theme):
        self.selected_theme = theme
        self.init_game()

    def init_game(self):
        if self.selected_theme:
            word = random.choice(self.themes[self.selected_theme])
            self.word = word.lower()
            self.hidden_word = ["_"] * len(self.word)
            self.update_word_label()
            self.remaining_attempts = 6
            self.update_remaining_attempts_label()
            self.guessed_letters = []
            self.canvas.delete("hangman")  # Clear previous hangman parts
            self.draw_hangman()

    def update_word_label(self):
        displayed_word = " ".join(self.hidden_word)
        self.word_label.config(text=displayed_word)

    def update_remaining_attempts_label(self):
        self.remaining_attempts_label.config(text=f"Remaining Attempts: {self.remaining_attempts}")

    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            messagebox.showinfo("Already Guessed", "You have already guessed this letter.")
            return

        self.guessed_letters.append(letter)

        if letter in self.word:
            for i, char in enumerate(self.word):
                if char == letter:
                    self.hidden_word[i] = self.word[i]
            self.update_word_label()
            if "_" not in self.hidden_word:
                messagebox.showinfo("Congratulations", "You have guessed the word!")
                self.restart_game()
        else:
            self.remaining_attempts -= 1
            self.update_remaining_attempts_label()
            if self.remaining_attempts == 0:
                messagebox.showinfo("Game Over", f"Sorry, you lost. The word was: {self.word}")
                self.restart_game()
            else:
                self.draw_hangman()

    def draw_hangman(self):
        if self.remaining_attempts == 6:
            # Draw gallows
            self.canvas.create_line(50, 250, 200, 250, width=5, fill="white", tags="hangman")
            self.canvas.create_line(125, 250, 125, 50, width=5, fill="white", tags="hangman")
            self.canvas.create_line(125, 50, 175, 50, width=5, fill="white", tags="hangman")
        elif self.remaining_attempts == 5:
            # Draw head
            self.canvas.create_oval(150, 100, 175, 125, outline="white", width=2, tags="hangman")
        elif self.remaining_attempts == 4:
            # Draw body
            self.canvas.create_line(162.5, 125, 162.5, 200, fill="white", width=2, tags="hangman")
        elif self.remaining_attempts == 3:
            # Draw left arm
            self.canvas.create_line(162.5, 150, 137.5, 175, fill="white", width=2, tags="hangman")
        elif self.remaining_attempts == 2:
            # Draw right arm
            self.canvas.create_line(162.5, 150, 187.5, 175, fill="white", width=2, tags="hangman")
        elif self.remaining_attempts == 1:
            # Draw left leg
            self.canvas.create_line(162.5, 200, 137.5, 225, fill="white", width=2, tags="hangman")
            self.canvas.create_line(162.5, 200, 137.5, 225, fill="white", width=2, tags="hangman")
        elif self.remaining_attempts == 0:
            # Draw right leg and display game over message
            self.canvas.create_line(162.5, 200, 187.5, 225, fill="white", width=2, tags="hangman")
            messagebox.showinfo("Game Over", f"Sorry, you lost. The word was: {self.word}")

    def restart_game(self):
        self.word_label.config(text="")
        self.remaining_attempts_label.config(text="")
        self.destroy()
        app = HangmanGame()
        app.mainloop()

if __name__ == "__main__":
    app = HangmanGame()
    app.mainloop()
