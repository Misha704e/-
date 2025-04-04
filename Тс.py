import tkinter as tk
import random

colors = ["red", "blue", "green", "yellow", "purple", "orange"]

def change_border_color():
    random_color = random.choice(colors)
    button.config(bg=random_color)

root = tk.Tk()
root.title("Зміна кольору рамки")

button = tk.Button(root, text="Натисни мене!", command=change_border_color, relief="solid", borderwidth=4)
button.pack(pady=20)

root.mainloop()
