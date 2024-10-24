import tkinter as tk

def show_message():
    message = entry.get()
    label.config(text=message)

root = tk.Tk()
root.title("Message App")
root.geometry("400x300")


entry = tk.Entry(root, width=50)
entry.pack(pady=20)


button = tk.Button(root, text="View", command=show_message)
button.pack(pady=10)

label = tk.Label(root, text="")
label.pack(pady=20)


root.mainloop()
