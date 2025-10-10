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

# Function to translate Estonian swears to English
def translate_swear(swear):
    translations = {
        "Kurat!" : "Damn it!", "Persse!" : "Asshole!", "Sitapea!" : "Shithead!",
        "Püha müristus!" : "Holy thunder!", "Taevas appi!" : "Heaven help!",
        "Tõsi või?" : "Is it true?", "Issand jumal!" : "Lord God!",
        "Vanaema solvaja!" : "Grandmother insulter!", "Tuharate nuusutaja!" : "Buttock sniffer"
    }
    return translations.get(swear, "Unknown")

# Function to play a single swear
def play_swear(category):
    if category == "Random":
        category = random.choice(list(swear_dict.keys()))
    swear = random.choice(swear_dict[category])
    swear_text.set(swear)
    english_translation.set(translate_swear(swear))
    play_audio(swear)

# Function to play audio
def play_audio(swear):
    audio_file = f"audio/{swear}.mp3"
    if os.path.exists(audio_file):
        mixer.music.load(audio_file)
        mixer.music.play()

"""
# Combo function: play 3 swears in order and display formatted text
def play_combo():
    categories = ["Anger", "Surprise", "Humour"]
    estonian_line = []
    english_line = []

    for category in categories:
        swear = random.choice(swear_dict[category])
        estonian_line.append(swear)
        english_line.append(translate_swear(swear))
        play_audio(swear)
        while mixer.music.get_busy():
            time.sleep(0.05)

    swear_text.set("   ".join(estonian_line))
    english_translation.set("   ".join(english_line))

    """

def play_combo():
    swear1 = random.choice(swear_dict["Anger"])
    swear2 = random.choice(swear_dict["Surprise"])
    swear3 = random.choice(swear_dict["Humour"])
    
    # Display all three words in a single row
    swear_text.set(f"{swear1} {swear2} {swear3}")
    
    # Display translations centered below
    english_translation.set(f"{translate_swear(swear1)}    {translate_swear(swear2)}    {translate_swear(swear3)}")

    # Play each swear immediately after the previous one finishes
    root.after(1, lambda: mixer.music.load(f"audio/{swear1}.mp3"))
    root.after(2, lambda: mixer.music.play())
    root.after(800, lambda: mixer.music.load(f"audio/{swear2}.mp3"))  # Adjusted timing for faster playback
    root.after(801, lambda: mixer.music.play())
    root.after(1600, lambda: mixer.music.load(f"audio/{swear3}.mp3"))
    root.after(1601, lambda: mixer.music.play())


# GUI setup
root = tk.Tk()
root.title("ESM Compact Modoe")
root.attributes('-fullscreen', True)

# Set small fixed size for 3.5” display (adjust if needed)
root.geometry("480x320")
root.configure(bg="black")

# Load background image (Estonian flag)
bg_image = tk.PhotoImage(file="image/estonian_flag.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#title_label = tk.Label(root, text="ESTONIAN SWEARING MACHINE", font=("Arial", 56, "bold"), fg="white", bg="black")
#title_label.grid(row=0, column=0, columnspan=3, pady=20)  # Center it across 3 columns

# Variables for swear text and translation
swear_text = tk.StringVar()
english_translation = tk.StringVar()

# Button style
button_style = {
    "font": ("Arial", 14, "bold"),
    "fg": "white",
    "bg": "black",
    "relief": "raised",
    "bd": 4,
    "width": 10,
    "height": 2
}

# Create buttons
buttons = [
    ("Anger", lambda: play_swear("Anger"), 3, 0),
    ("Humour", lambda: play_swear("Humour"), 3, 1),
    ("Surprise", lambda: play_swear("Surprise"), 3, 2),
#   ("Random", lambda: play_swear("Random"), 6, 0),
    ("Combo", lambda: play_combo, 4, 0),
    ("Too Far", lambda: play_swear("Anger"), 4, 1)
    ("Menu", lambda: play_swear("Anger"), 4, 2)
]

for text, command, row, col in buttons:
    btn = tk.Button(root, text=text, command=command, **button_style)
    btn.grid(row=row, column=col, padx=10, pady=10, columnspan=1)

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)


# Display Area
tk.Label(root, textvariable=swear_text, font=("Arial", 28, "bold"), bg="white").grid(row=6, column=0, columnspan=3, pady=5)
tk.Label(root, textvariable=english_translation, font=("Arial", 24, "italic"), bg="white").grid(row=7, column=0, columnspan=3)

root.mainloop()
