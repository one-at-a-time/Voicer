import os
import tkinter as tk
from tkinter import messagebox

import pygame
from gtts import gTTS


def text_to_speech():
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Please enter text to convert to speech")
        return
    
    try:
        tts = gTTS(text=text, lang='en')
        filename = "output.mp3"
        tts.save(filename)
        
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        pygame.mixer.quit()
        os.remove(filename)  # Clean up the file after playing
    except Exception as e:
        messagebox.showerror("Error", f"Speech generation failed: {e}")


# GUI Setup
root = tk.Tk()
root.title("Text to Speech App")
root.geometry("400x300")

tk.Label(root, text="Enter Text:", font=("Arial", 12)).pack(pady=5)
text_entry = tk.Text(root, height=5, width=40)
text_entry.pack()

tk.Button(root, text="Convert & Play", command=text_to_speech).pack(pady=10)

root.mainloop()
