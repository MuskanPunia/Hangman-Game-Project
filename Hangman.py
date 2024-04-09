import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hangman Game")
        self.geometry("500x600")
        self.themes_colors = {
            "Colors": "#ADD8E6",  # Light blue
            "Animals": "#90EE90",  # Light green
            "Countries": "#FFA07A",  # Light salmon
            "Fruits": "#FFD700",  # Gold
            "Planets": "#AFEEEE"  # Pale turquoise
        }
        self.configure(bg="#ADD8E6")  # Default background color
        self.canvas = tk.Canvas(self, bg="#ADD8E6", width=300, height=300)  # Reduced canvas height
        self.canvas.pack(pady=20)
        self.themes = {
            "Colors": {"red": "It is a color associated with love and passion.",
                       "blue": "It is the color of the sky on a clear day.",
                       "green": "It is the color of grass and leaves.",
                       "yellow": "It is the color of the sun.",
                       "orange": "It is a fruit and a color.",
                       "purple": "It is often associated with royalty.",
                       "black": "It is the absence of light.",
                       "white": "It is the color of purity and innocence."},
            "Animals": {"lion": "It is known as the king of the jungle.",
                        "elephant": "It is the largest land animal.",
                        "tiger": "It has stripes and is orange in color.",
                        "giraffe": "It has a long neck and spots.",
                        "zebra": "It has black and white stripes.",
                        "monkey": "It is a primate known for its agility.",
                        "panda": "It is black and white and eats bamboo.",
                        "koala": "It is a marsupial native to Australia."},
            "Countries": {"Chile": "It is known for its long and narrow shape.",
                          "Brazil": "It is the largest country in South America.",
                          "Norway": "It is located in Northern Europe and is known for its fjords.",
                          "Denmark": "It is a Scandinavian country known for its high standard of living.",
                          "Serbia": "It is a country located in Southeast Europe.",
                          "Mexico": "It is known for its rich culture and cuisine.",
                          "Canada": "It is the second-largest country in the world by land area.",
                          "Japan": "It is an island country in East Asia."},
            "Fruits": {"apple": "It is a popular fruit that comes in various colors.",
                       "banana": "It is a long yellow fruit that grows on trees.",
                       "strawberry": "It is a small red fruit with seeds on its surface.",
                       "pineapple": "It is a tropical fruit with a spiky exterior and sweet interior.",
                       "grape": "It is a small round fruit often used to make wine.",
                       "watermelon": "It is a large fruit with green skin and red juicy flesh.",
                       "kiwi": "It is a small green fruit with brown skin and tiny black seeds.",
                       "orange": "It is a citrus fruit known for its vitamin C content."},
            "Planets": {"mercury": "It is the smallest planet in our solar system.",
                        "venus": "It is often called Earth's twin due to its similar size and composition.",
                        "earth": "It is the third planet from the sun and the only known planet with life.",
                        "mars": "It is often called the red planet.",
                        "jupiter": "It is the largest planet in our solar system.",
                        "saturn": "It is known for its rings made of ice and dust.",
                        "uranus": "It is tilted on its side, giving it unique seasons.",
                        "neptune": "It is the farthest planet from the sun."}
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

        self.hint_label = tk.Label(self, text="", font=("Arial", 14), bg="#ADD8E6", fg="#FFFFFF")
        self.hint_label.pack(pady=5)

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
        self.configure(bg=self.themes_colors[theme])
        self.init_game()

    def init_game(self):
        if self.selected_theme:
            word, hint = random.choice(list(self.themes[self.selected_theme].items()))
            self.word = word.lower()
            self.hidden_word = ["_"] * len(self.word)
            self.update_word_label()
            self.remaining_attempts = 6
            self.update_remaining_attempts_label()
            self.guessed_letters = []
            self.canvas.delete("hangman")  # Clear previous hangman parts
            self.draw_hangman()
            self.display_hint(hint)

    def display_hint(self, hint):
        self.hint_label.config(text=f"Hint: {hint}")

    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            messagebox.showinfo("Already Guessed", "You have already guessed this letter.")
            return;

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
            elif self.remaining_attempts == 3:
                self.display_hint(random.choice(list(self.themes[self.selected_theme].values())))
            else:
                self.draw_hangman()

    def update_word_label(self):
        displayed_word = " ".join(self.hidden_word)
        self.word_label.config(text=displayed_word)

    def update_remaining_attempts_label(self):
        self.remaining_attempts_label.config(text=f"Remaining Attempts: {self.remaining_attempts}")

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

