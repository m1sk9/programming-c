import tkinter as tk
from tkinter import messagebox

def calc_add():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.insert(tk.END, str(num1 + num2))
    except ValueError:
        messagebox.showerror("Error", "Please enter a number")

root = tk.Tk()
root.title("Addition of Numbers")
root.geometry("300x200")

label1 = tk.Label(root, text="Number 1:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Number 2:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

label3 = tk.Label(root, text="Result:")
label3.pack()

result = tk.Entry(root)
result.pack()

button = tk.Button(root, text="Add", command=calc_add)
button.pack(pady = 20)

root.mainloop()
