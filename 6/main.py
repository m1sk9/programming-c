import tkinter as tk

def change_text():
    label.config(text="Hello, World!")

root = tk.Tk()
root.title("Hello, World App")
root.geometry("300x200")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)

button = tk.Button(root, text="Change Text", command=change_text)
button.pack(pady=10)

root.mainloop()
