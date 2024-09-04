import pyautogui
import time
import random

def typing_ghost():
    sentences = [
        "Why are you ignoring me?",
        "I'm still here...",
        "You can't escape from me.",
        "I'm watching you.",
        "Did you hear that noise?",
    ]
    while True:
        time.sleep(random.uniform(5, 15))  # Random delay between sentences
        pyautogui.typewrite(random.choice(sentences))
        pyautogui.press('enter')

typing_ghost()
