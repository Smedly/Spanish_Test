"""
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
bg_image = PhotoImage(file="estonian_flag.png")
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
"""

import tkinter as tk
import random
import os
from pygame import mixer

# Initialize Pygame Mixer for audio playback
mixer.init()

# Swear dictionary with audio filenames
swear_dict = {
    "Anger": ["Kuradi!", "Persse!", "Sita kah!"],
    "Humour": ["Püha müristus!", "Taevas appi!", "Vanaema solvaja!"],
    "Surprise": ["Tõsi või?", "Issand jumal!"],
}

# Function to play audio and display text
def play_swear(category):
    if category == "Random":
        category = random.choice(list(swear_dict.keys()))
    
    swear = random.choice(swear_dict[category])
    swear_text.set(swear)
    english_translation.set(translate_swear(swear))
    
    audio_file = f"audio/{swear}.mp3"  # Ensure the audio files are in an 'audio' folder
    print(f"Looking for file: {audio_file}")

    if os.path.exists(audio_file): 
        mixer.music.load(audio_file)
        mixer.music.play()

# Function to translate Spanish swears to English
def translate_swear(swear):
    translations = {
        "Kuradi!" : "Damn it!", "Persse!" : "Asshole!", "Sitapea!" : "Shithead!",
        "Püha müristus!" : "Holy thunder!", "Taevas appi!" : "Heaven help!",
        "Tõsi või?" : "Is it true?", "Issand jumal!" : "Lord God!",
        "Vanaema solvaja!" : "Grandmother insulter!", "Tuharate nuusutaja!" : "Buttock sniffer"
    }
    return translations.get(swear, "Unknown")

# GUI Setup
root = tk.Tk()
root.title("Estonian Swearing Machine")
root.geometry("400x300")

# Load Estonian flag as background
bg_image = tk.PhotoImage(file="image/estonian_flag.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

label_text = tk.StringVar()
swear_label = tk.Label(root, textvariable=label_text, font=("Arial", 14, "bold"), bg="white")
swear_label.pack(pady=10)

swear_text = tk.StringVar()
english_translation = tk.StringVar()

"""
# Buttons
categories = ["Anger", "Humour", "Surprise", "Random"]
for i, category in enumerate(categories):
    btn = tk.Button(root, text=category, command=lambda c=category: play_swear(c), 
                    width=50, height=15, relief="raised", bd=5)
    btn.grid(row=0, column=i, padx=5, pady=10)

# Display Area
tk.Label(root, textvariable=swear_text, font=("Arial", 20, "bold")).grid(row=1, column=0, columnspan=4, pady=10)
tk.Label(root, textvariable=english_translation, font=("Arial", 14, "italic")).grid(row=2, column=0, columnspan=4)
"""

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