import tkinter as tk
import random
import os
import time
from pygame import mixer

# Initialize Pygame Mixer for audio playback
mixer.init()

# Swear dictionary with audio filenames
swear_dict = {
    "Anger": ["Kurat!", "Persse!", "Sitapea!"],
    "Humour": ["Püha müristus!", "Vanaema solvaja!", "Tuharate nuusutaja!"],
    "Surprise": ["Tõsi või?", "Issand jumal!", "Taevas appi!"],
}

# Function to translate Estonian swears to English
def translate_swear(swear):
    translations = {
        "Kurat!": "Damn it!",
        "Persse!": "Asshole!",
        "Sitapea!": "Shithead!",
        "Püha müristus!": "Holy thunder!",
        "Taevas appi!": "Heaven help!",
        "Tõsi või?": "Is it true?",
        "Issand jumal!": "Lord God!",
        "Vanaema solvaja!": "Grandmother insulter!",
        "Tuharate nuusutaja!": "Buttock sniffer"
    }
    return translations.get(swear, "Unknown")

# Function to play a single swear
def play_swear(category):
    if category == "Random":
        category = random.choice(list(swear_dict.keys()))

    swear = random.choice(swear_dict[category])
    swear_text.set(swear)
    english_translation.set(translate_swear(swear))

    audio_file = f"audio/{swear}.mp3"
    if os.path.exists(audio_file):
        mixer.music.load(audio_file)
        mixer.music.play()

# Function to play Combo swears with delay
def play_combo():
    categories = ["Anger", "Surprise", "Humour"]
    for i, category in enumerate(categories):
        swear = random.choice(swear_dict[category])
        if i == 0:
            # Show first swear
            swear_text.set(swear)
            english_translation.set(translate_swear(swear))

        audio_file = f"audio/{swear}.mp3"
        if os.path.exists(audio_file):
            mixer.music.load(audio_file)
            mixer.music.play()
            while mixer.music.get_busy():
                time.sleep(0.1)
            time.sleep(0.5)

# GUI Setup
root = tk.Tk()
root.title("Estonian Swearing Machine")

# Fullscreen
root.attributes('-fullscreen', True)

# Load Estonian flag as background
bg_image = tk.PhotoImage(file="image/estonian_flag.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

swear_text = tk.StringVar()
english_translation = tk.StringVar()

# Frame for buttons (horizontal layout)
button_frame = tk.Frame(root, bg="", pady=20)
button_frame.pack(side=tk.TOP)

# Button style (larger font, fixed pixel size)
button_style = {
    "font": ("Arial", 24, "bold"),
    "fg": "white",
    "bg": "black",
    "relief": "raised",
    "bd": 6,
    "width": 12,
    "height": 2
}

# Button definitions
buttons = [
    ("Anger", lambda: play_swear("Anger")),
    ("Humour", lambda: play_swear("Humour")),
    ("Surprise", lambda: play_swear("Surprise")),
    ("Random", lambda: play_swear("Random")),
    ("Combo", play_combo),
    ("Too Far", lambda: play_swear("Anger"))
]

# Create buttons in a horizontal row
for text, command in buttons:
    btn = tk.Button(button_frame, text=text, command=command, **button_style)
    btn.pack(side=tk.LEFT, padx=10, pady=10)

# Display Area
tk.Label(root, textvariable=swear_text, font=("Arial", 50, "bold"), bg="white").pack(pady=30)
tk.Label(root, textvariable=english_translation, font=("Arial", 28, "italic"), bg="white").pack()

# Exit on ESC key
def exit_fullscreen(event):
    root.attributes('-fullscreen', False)

root.bind("<Escape>", exit_fullscreen)

root.mainloop()
