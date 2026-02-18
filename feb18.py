import tkinter as tk
from tkinter import filedialog
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Create window
root = tk.Tk()
root.title("Python Music Player")
root.geometry("400x300")

# Functions
def load_music():
    file = filedialog.askopenfilename()
    if file:
        pygame.mixer.music.load(file)
        song_label.config(text=file.split("/")[-1])

def play_music():
    pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def stop_music():
    pygame.mixer.music.stop()

# UI Elements
song_label = tk.Label(root, text="No song selected", wraplength=300)
song_label.pack(pady=20)

load_btn = tk.Button(root, text="Load Song", command=load_music)
load_btn.pack(pady=5)

play_btn = tk.Button(root, text="Play", command=play_music)
play_btn.pack(pady=5)

pause_btn = tk.Button(root, text="Pause", command=pause_music)
pause_btn.pack(pady=5)

stop_btn = tk.Button(root, text="Stop", command=stop_music)
stop_btn.pack(pady=5)

root.mainloop()
