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
            "Colors": {"red": "is associated with fire", "blue": "is the color of the sky", "green": "is the color of grass", "yellow": "is the color of the sun", "orange": "is a citrus color", "purple": "is a royal color", "black": "is the color of darkness", "white": "is the color of purity"},
            "Animals": {"lion": "roars loudly", "elephant": "has a long trunk", "tiger": "has stripes", "giraffe": "has a long neck", "zebra": "has black and white stripes", "monkey": "loves bananas", "panda": "is black and white", "koala": "loves eucalyptus leaves"},
            "Countries": {"Chile": "is in South America", "Brazil": "is known for its rainforests", "Norway": "is in Europe", "Denmark": "is in Scandinavia", "Serbia": "is in Eastern Europe", "Mexico": "is in North America", "Canada": "is known for its maple leaf", "Japan": "is in Asia"},
            "Flowers": {"rose": "is a symbol of love", "tulip": "comes in many colors", "daisy": "has white petals", "sunflower": "is yellow and tall", "lily": "is often used in weddings", "orchid": "has delicate petals", "daffodil": "blooms in spring", "peony": "has large colorful flowers"},
            "Planets": {"mercury": "is closest to the sun", "venus": "is known as the morning star", "earth": "is the only known planet with life", "mars": "is known as the red planet", "jupiter": "is the largest planet", "saturn": "has beautiful rings", "uranus": "is tilted on its side", "neptune": "is blue and cold"},
            "Companies": {"apple": "makes iPhones", "google": "owns the search engine", "amazon": "is an online marketplace", "facebook": "is a social media platform", "microsoft": "makes Windows", "tesla": "makes electric cars", "netflix": "streams movies and TV shows", "ibm": "is a technology company"},
            "Medical Science": {"anatomy": "is the study of body structure", "biology": "is the study of living organisms", "chemistry": "deals with the composition of substances", "physiology": "is the study of how the body functions", "pharmacology": "is the study of drugs", "genetics": "is the study of genes", "pathology": "is the study of diseases", "immunology": "is the study of the immune system"},
            "Politics": {"democracy": "is a form of government by the people", "republic": "is a state where supreme power is held by the people", "president": "is the head of state", "parliament": "is the legislative body", "election": "is the process of choosing a leader", "government": "is the system by which a state or community is controlled", "politics": "is the activities associated with governance", "legislation": "is the making or enactment of laws"},
            "Commerce": {"market": "is where goods are bought and sold", "trade": "involves the exchange of goods and services", "economy": "is the system of production, distribution, and consumption", "finance": "deals with the management of money", "investment": "involves putting money into financial schemes", "business": "involves providing goods or services to customers", "entrepreneur": "is a person who starts a business", "consumer": "is a person who buys goods or services for personal use"}
        }

        self.selected_theme = ""
        self.word = ""
        self.word_hint = ""
        self.remaining_attempts = 6
        self.guessed_letters = []
        self.hint_counter = 0

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
            word_hint_pair = random.choice(list(self.themes[self.selected_theme].items()))
            self.word = word_hint_pair[0]
            self.word_hint = f"{word_hint_pair[0]}: {word_hint_pair[1]}"  # Updated to include colon between word and hint
            self.hidden_word = ["_"] * len(self.word)
            self.update_word_label()
            self.remaining_attempts = 6
            self.update_remaining_attempts_label()
            self.guessed_letters = []
            self.canvas.delete("hangman")  # Clear previous hangman parts
            self.draw_hangman()
            self.hint_counter = 0  # Reset hint counter

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

        if letter in self.word.lower():
            for i, char in enumerate(self.word.lower()):
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
                self.hint_counter += 1
                if self.hint_counter == 3:  # Check if three wrong attempts have been made
                    self.show_hint()
                    self.hint_counter = 0  # Reset hint counter

    def show_hint(self):
        # Displaying the correct hint with the word
        messagebox.showinfo("Hint", self.word_hint)

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

