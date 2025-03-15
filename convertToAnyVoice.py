import tkinter as tk
from tkinter import messagebox

import pyttsx3


def text_to_speech():
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Please enter text to convert to speech")
        return

    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        
        selected_voice = voice_var.get()
        
        # Choose voice based on selection
        if selected_voice == "Male":
            engine.setProperty('voice', voices[0].id)
        else:
            engine.setProperty('voice', voices[1].id)
        
        engine.say(text)
        engine.runAndWait()
        
    except Exception as e:
        messagebox.showerror("Error", f"Speech generation failed: {e}")


# GUI Setup
root = tk.Tk()
root.title("Text to Speech App")
root.geometry("400x300")

tk.Label(root, text="Enter Text:", font=("Arial", 12)).pack(pady=5)
text_entry = tk.Text(root, height=5, width=40)
text_entry.pack()

# Voice selection dropdown
tk.Label(root, text="Select Voice:", font=("Arial", 12)).pack(pady=5)
voice_var = tk.StringVar(root)
voice_var.set("Male")  # Default voice is Male
tk.OptionMenu(root, voice_var, "Male", "Female").pack(pady=5)

# Button to trigger speech
tk.Button(root, text="Convert & Play", command=text_to_speech).pack(pady=10)

root.mainloop()
