import tkinter as tk
import random
import os
import time
from pygame import mixer

# Initialize Pygame Mixer
mixer.init()

# Swear dictionary
swear_dict = {
    "Anger": ["Kurat!", "Persevest!", "Sitapea!", "Käi põrgu!", "Loll kui saabas!", "Kanaaju!", "Jälkus!", "Tainapea!", "Loll nagu oinas!"],
    "Humour": ["Püha müristus!", "Taevas appi!", "Püha püss!", "Mine metsa!", "Sõida seenele!", "Tõmba uttu!", "Käi kuu peale!", "Käi kukele!", "Tõmba lesta!"],
    "Surprise": ["Tõsi või?", "Issand jumal!", "Mida perset!", "Mida põrgut!", "Kuramus!", "Mind ei koti!", "Sitanikerdis!", "Kurivaim!", "Türaürask!"],

    "Too Far": ["Mul on nii nii nii kahju!", "Suudlen su varbaid!", "Tubli oled, mina olen prügi.!", "Anna andeks, ma olen ahv!", 
    "Ma olen täielik idioot!", "Ma rooman su ees nagu uss", "Las ma elan nagu su mopp!", "Ma lähen metsa häbi pärast!", "Palun andesta mu kanaaju!"], 
}


# Copy of swear_dict to track unplayed swears
unplayed_swears = {category: swear_dict[category][:] for category in swear_dict}


# Function to translate Estonian swears to English
def translate_swear(swear):
    translations = {
        # Anger
        "Kurat!" : "Damn it!", "Persevest!" : "Ass vest!", "Sitapea!" : "Shithead!", 
        "Käi põrgu!" : "Go to hell!", "Loll kui saabas!" : "You're stupid like boot!", "Kanaaju!" : "Chicken brain!", 
        "Jälkus!" : "Disgusting creature!", "Tainapea!" : "Dough-head!", "Loll nagu oinas!" : "You're stupid like ram",
        # Humour
        "Püha müristus!" : "Holy thunder!", "Taevas appi!" : "Heaven help us!", "Püha püss!" : "Holy gun!", 
        "Mine metsa!" : "Go to the forest!", "Sõida seenele!" : "Go pick some mushrooms!", "Tõmba uttu!" : "Pull into a fog!", 
        "Käi kuu peale!" : "Walk to the moon!", "Käi kukele!" : "Go to the rooster!", "Tõmba lesta!" : "Pull a flipper!",
        # Surprise
        "Tõsi või?" : "Is it true?", "Issand jumal!" : "Lord God!", "Mida perset!" : "What the ass!", 
        "Mida põrgut!" : "What the hell!", "Kuramus!" : "Damnation!", "Mind ei koti!" : "It doesn't bag me!",
        "Sitanikerdis!" : "What a carving of shit!", "Kurivaim!" : "Angry spirits!", "Türaürask!" : "Cockbeetles!",
        # Too Far
        "Mul on nii nii nii kahju!" : "I'm so so so sorry!", "Suudlen su varbaid!" : "I kiss your toes!",
        "Tubli oled, mina olen prügi.!" : "You are good, I am scum!", "Anna andeks, ma olen ahv!" : "Forgive me, I am a monkey!",
        "Ma olen täielik idioot!" : "I'm a total idiot!", "Ma rooman su ees nagu uss" : "I crawl before you like a worm!",
        "Las ma elan nagu su mopp!" : "Let me live as your mop!", "Ma lähen metsa häbi pärast!" : "I'm going to the forest in shame!",
        "Palun andesta mu kanaaju!" : "Please forgive my chicken brain!",
    }
    
    return translations.get(swear, "Unknown")


# Function to play a single swear without repeating
def play_swear(category):
    global unplayed_swears

    if category == "Random":
        category = random.choice(list(swear_dict.keys()))

    # If all swears in this category have been played, reset the list
    if not unplayed_swears[category]:
        unplayed_swears[category] = swear_dict[category][:]

    # Choose and remove a swear from the unplayed list
    swear = random.choice(unplayed_swears[category])
    unplayed_swears[category].remove(swear)

    # Display and play it
    swear_text.set(swear)
    english_translation.set(translate_swear(swear))
    play_audio(swear)


# Function to play audio
def play_audio(swear):
    audio_file = f"audio/{swear}.mp3"
    if os.path.exists(audio_file):
        mixer.music.load(audio_file)
        mixer.music.play()


def play_combo():
    import random

    # Helper: lowercase & clean second swear
    def to_combo_form(s):
        s = s.strip()
        if s.endswith(("!", "?", ".")):
            s = s[:-1]
        return s[0].lower() + s[1:]

    # Collect all swears across all categories
    #all_swears = [swear for cat in swear_dict.values() for swear in cat]

    # Collect swears only from Anger, Humour, and Surprise
    all_swears = [swear for cat_name, cat in swear_dict.items() if cat_name != "Too Far" for swear in cat]


    # Pick two distinct swears
    swear1, swear2 = random.sample(all_swears, 2)

    # Build combo text (Estonian)
    combo_est = f"{swear1[:-1]} {to_combo_form(swear2)}!"
    swear_text.set(combo_est)

    # Build translation text (English)
    #combo_eng = f"{translate_swear(swear1)} {translate_swear(swear2).lower()}"
    #english_translation.set(combo_eng)
    eng1 = translate_swear(swear1).strip()
    eng2 = translate_swear(swear2).strip()

    # Remove trailing punctuation and lowercase second word
    if eng1.endswith(("!", ".", "?")):
        eng1 = eng1[:-1]
    eng2 = eng2[0].lower() + eng2[1:]

    combo_eng = f"{eng1} {eng2}!"
    english_translation.set(combo_eng)

    # Play audio sequentially — nice timing
    root.after(1, lambda: mixer.music.load(f"audio/{swear1}.mp3"))
    root.after(2, lambda: mixer.music.play())
    root.after(900, lambda: mixer.music.load(f"audio/{swear2}.mp3"))  # Adjust timing if needed
    root.after(901, lambda: mixer.music.play())


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
swear_text = tk.StringVar(value="")
english_translation = tk.StringVar(value="")

estonian_title = "Eesti Vandumismasin"
english_title = "Estonian Swearing Machine"

# --- Typewriter effect ---
def typewriter_effect(text, var, delay=100, index=0, callback=None):
    """Displays text one character at a time."""
    if index < len(text):
        var.set(text[:index + 1])
        root.after(delay, typewriter_effect, text, var, delay, index + 1, callback)
    elif callback:
        root.after(300, callback)  # Optional pause before next line


def startup_sequence():
    """Runs typing for both lines sequentially."""
    typewriter_effect(estonian_title, swear_text, delay=100, callback=lambda:
        typewriter_effect(english_title, english_translation, delay=80))

root.after(1000, startup_sequence)  # Wait 1 second after launch before starting

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
    ("Combo", lambda: play_combo(), 4, 0),
    ("Too Far", lambda: play_swear("Too Far"), 4, 1),
    ("Menu", lambda: play_swear("Anger"), 4, 2)
]

for text, command, row, col in buttons:
    btn = tk.Button(root, text=text, command=command, **button_style)
    btn.grid(row=row, column=col, padx=10, pady=10, columnspan=1)

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)

# Display Area
tk.Label(root, textvariable=swear_text, font=("Arial", 22, "bold"), bg="white", justify="center").grid(row=6, column=0, columnspan=3, pady=5)
tk.Label(root, textvariable=english_translation, font=("Arial", 18, "italic"), bg="white", justify="center").grid(row=7, column=0, columnspan=3)

root.mainloop()

