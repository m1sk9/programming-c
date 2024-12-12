import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Info", "Selected")

root = tk.Tk()
root.title("Multiple Menus")
root.geometry("300x200")

menubar = tk.Menu(root)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=show_message)
filemenu.add_command(label="Exit", command=root.quit)

editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=show_message)
editmenu.add_command(label="Redo", command=show_message)

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Edit", menu=editmenu)

root.config(menu=menubar)

root.mainloop()
