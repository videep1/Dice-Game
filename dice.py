import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import random
win=tk.Tk()
win.title("Dice game")

def play():
    num=random.randint(1,6)
    number.config(text=f"number is:{num}")
    if num==6:
        showinfo("CONGRATULATIONS:!!!!YOU WIN!!!!")

number= ttk.Label(win,text="")
number.pack(pady=10)
play= ttk.Button(win,text="play",command=play)
play.pack(padx=50)
win.mainloop()