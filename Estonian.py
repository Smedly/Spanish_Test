import tkinter as tk
from tkinter import PhotoImage
from pygame import mixer
import random

# Initialize audio mixer
mixer.init()

# Swear words dictionary (category: [swears])
swears = {
    "Anger": ["Kuradi!", "Persse!", "Sita kah!"],
    "Humour": ["Püha müristus!", "Taevas appi!"],
    "Surprise": ["Tõsi või?", "Issand jumal!"],
}

# Function to play a selected swear word
def play_swear(category):
    if category in swears:
        word = random.choice(swears[category])
        label_text.set(word)
        # Play the corresponding audio file (placeholder)
        mixer.Sound(f"sounds/{word}.wav").play()

# UI Setup
root = tk.Tk()
root.title("ESTONIAN SWEARING MACHINE")
root.geometry("480x320")

# Load Estonian flag as background
bg_image = PhotoImage(file="image/estonian_flag.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

label_text = tk.StringVar()
swear_label = tk.Label(root, textvariable=label_text, font=("Arial", 14, "bold"), bg="white")
swear_label.pack(pady=10)

# Button styles
button_style = {
    "font": ("Arial", 12, "bold"),
    "fg": "white",
    "bg": "black",
    "relief": "raised",
    "bd": 5,
    "width": 15,
    "height": 2
}

# Create buttons
buttons = [
    ("Anger", lambda: play_swear("Anger")),
    ("Humour", lambda: play_swear("Humour")),
    ("Surprise", lambda: play_swear("Surprise")),
    ("Random", lambda: play_swear(random.choice(list(swears.keys()))))
]

for text, command in buttons:
    btn = tk.Button(root, text=text, command=command, **button_style)
    btn.pack(pady=5)

root.mainloop()