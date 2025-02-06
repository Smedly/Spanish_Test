import tkinter as tk
import random
import os
from pygame import mixer

# Initialize Pygame Mixer for audio playback
mixer.init()

# Swear dictionary with audio filenames
swear_dict = {
    "Anger": ["Pendejo", "Chingada_madre", "Hijo_de_puta", "Chupamelo", "Pinche_culero"],
    "Humour": ["Huevon", "Cabron", "No_mames", "Guey", "No_manches"],
    "Surprise": ["Mierda", "Mamon", "Cojones", "Carajo", "Maldito"]
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
        "Pendejo": "Dipshit", "Chingada_madre": "Mother fucker", "Hijo_de_puta": "Son of a bitch",
        "Chupamelo": "Suck my dick", "Pinche_culero": "Fucking asshole",
        "Huevon": "Lazy ass", "Cabron": "Sucker", "No_mames": "You’re kidding me",
        "Guey": "Dude!", "No_manches": "No way!",
        "Mierda": "Shit", "Mamon": "Prick", "Cojones": "Balls", "Carajo": "Damnit", "Maldito": "Damn"
    }
    return translations.get(swear, "Unknown")

# GUI Setup
root = tk.Tk()
root.title("Spanish Swearing Machine")
root.geometry("400x300")

swear_text = tk.StringVar()
english_translation = tk.StringVar()

# Buttons
categories = ["Anger", "Humour", "Surprise", "Random"]
for i, category in enumerate(categories):
    btn = tk.Button(root, text=category, command=lambda c=category: play_swear(c), 
                    width=15, height=2, relief="raised", bd=5)
    btn.grid(row=0, column=i, padx=5, pady=10)

# Display Area
tk.Label(root, textvariable=swear_text, font=("Arial", 20, "bold")).grid(row=1, column=0, columnspan=4, pady=10)
tk.Label(root, textvariable=english_translation, font=("Arial", 14, "italic")).grid(row=2, column=0, columnspan=4)

root.mainloop()


