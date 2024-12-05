import tkinter as tk

def show_text():
    result_text = text.get("1.0", tk.END)
    result_label.config(text=result_text)

root = tk.Tk()
root.title("Multi-line Text")
root.geometry("300x200")

text = tk.Text(root)
text.pack()

button = tk.Button(root, text="Show", command=show_text)
button.pack(pady = 20)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
