import tkinter as tk
import random
import os
import time
from pygame import mixer

# Initialize Pygame Mixer
mixer.init()

# Swear dictionary
swear_dict = {
    "Anger": ["Kurat!", "Persse!", "Sitapea!"],
    "Humour": ["Püha müristus!", "Vanaema solvaja!", "Tuharate nuusutaja!"],
    "Surprise": ["Tõsi või?", "Issand jumal!", "Taevas appi!"],
}

# Translations
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

# Play a single swear
def play_swear(category):
    if category == "Random":
        category = random.choice(list(swear_dict.keys()))
    swear = random.choice(swear_dict[category])
    swear_text.set(swear)
    english_translation.set(translate_swear(swear))
    play_audio(swear)

def play_audio(swear):
    audio_file = f"audio/{swear}.mp3"
    if os.path.exists(audio_file):
        mixer.music.load(audio_file)
        mixer.music.play()

# Combo mode: plays 3 swears (Anger, Surprise, Humour) with shorter delay and shows all
def play_combo():
    categories = ["Anger", "Surprise", "Humour"]
    display_lines = []
    for category in categories:
        swear = random.choice(swear_dict[category])
        display_lines.append(f"{swear} – {translate_swear(swear)}")
        play_audio(swear)
        while mixer.music.get_busy():
            time.sleep(0.05)
        time.sleep(0.1)  # 250ms pause
    # Show all 3 on screen
    swear_text.set("\n".join(display_lines))
    english_translation.set("")

# GUI setup
root = tk.Tk()
root.title("Estonian Swearing Machine")
root.attributes('-fullscreen', True)

# Background image
bg_image = tk.PhotoImage(file="image/estonian_flag.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

swear_text = tk.StringVar()
english_translation = tk.StringVar()

# 2 rows of buttons using grid
button_style = {
    "font": ("Arial", 24, "bold"),
    "fg": "white",
    "bg": "black",
    "relief": "raised",
    "bd": 6,
    "width": 16,
    "height": 4
}

# Frame for buttons
button_frame = tk.Frame(root, bg="", pady=20)
button_frame.pack()

# First row
buttons_row1 = [
    ("Anger", lambda: play_swear("Anger")),
    ("Humour", lambda: play_swear("Humour")),
    ("Surprise", lambda: play_swear("Surprise")),
]

# Second row
buttons_row2 = [
    ("Random", lambda: play_swear("Random")),
    ("Combo", play_combo),
    ("Too Far", lambda: play_swear("Anger")),
]

# Place buttons in grid
for i, (text, command) in enumerate(buttons_row1):
    tk.Button(button_frame, text=text, command=command, **button_style).grid(row=0, column=i, padx=10, pady=10)

for i, (text, command) in enumerate(buttons_row2):
    tk.Button(button_frame, text=text, command=command, **button_style).grid(row=1, column=i, padx=10, pady=10)

# Display
tk.Label(root, textvariable=swear_text, font=("Arial", 40, "bold"), bg="white", justify="center").pack(pady=30)
tk.Label(root, textvariable=english_translation, font=("Arial", 28, "italic"), bg="white").pack()

# Escape key exits fullscreen
def exit_fullscreen(event):
    root.attributes('-fullscreen', False)

root.bind("<Escape>", exit_fullscreen)

root.mainloop()
