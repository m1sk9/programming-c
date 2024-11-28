import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Information", "Button was clicked!")

root = tk.Tk()
root.title("Basic Structure")
root.geometry("300x200")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady = 20)

button = tk.Button(root, text="Click", command=show_message)
button.pack(pady = 20)

root.mainloop()
