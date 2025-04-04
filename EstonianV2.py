import tkinter as tk
import random
import os
from pygame import mixer

# Initialize Pygame Mixer for audio playback
mixer.init()

# Swear dictionary with audio filenames
swear_dict = {
    "Anger": ["Kurat!", "Persse!", "Sitapea!"],
    "Humour": ["Püha müristus!", "Vanaema solvaja!", "Tuharate nuusutaja!"],
    "Surprise": ["Tõsi või?", "Issand jumal!", "Taevas appi!"],
}

# Function to play audio and display text
def play_swear(category):
    if category == "Random":
        category = random.choice(list(swear_dict.keys()))
    
    swear = random.choice(swear_dict[category])
    swear_text.set(swear)
    english_translation.set(translate_swear(swear))
    
    audio_file = f"audio/{swear}.mp3"  # Ensure the audio files are in an 'audio' folder
    # print(f"Looking for file: {audio_file}")

    if os.path.exists(audio_file): 
        mixer.music.load(audio_file)
        mixer.music.play()

# Function to translate Spanish swears to English
def translate_swear(swear):
    translations = {
        "Kurat!" : "Damn it!", "Persse!" : "Asshole!", "Sitapea!" : "Shithead!",
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

swear_text = tk.StringVar()
english_translation = tk.StringVar()

# Button styles
button_style = {
    "font": ("Arial", 18, "bold"),
    "fg": "white",
    "bg": "black",
    "relief": "raised",
    "bd": 5,
    "width": 40,
    "height": 10
}

# Create buttons
buttons = [
    ("Anger", lambda: play_swear("Anger"), 0, 0),
    ("Humour", lambda: play_swear("Humour"), 0, 1),
    ("Surprise", lambda: play_swear("Surprise"), 0, 2),
    ("Random", lambda: play_swear(random.choice(list(swear_dict.keys()))), 1, 0),
    ("Combo", lambda: play_swear("Anger"), 1, 1),
    ("Too Far", lambda: play_swear("Anger"), 1, 2)
]


# c=0
# r=0

for text, command, row, col in buttons:
    btn = tk.Button(root, text=text, command=command, **button_style)
    btn.grid(row=row, column=col, padx=5, pady=10)

#    c = c+1
#    if c == 1:
#        c = 0
#        r = r+1

# Display Area
tk.Label(root, textvariable=swear_text, font=("Arial", 20, "bold")).grid(row=2, column=0, columnspan=4, pady=10)
tk.Label(root, textvariable=english_translation, font=("Arial", 14, "italic")).grid(row=3, column=0, columnspan=4)

root.mainloop()