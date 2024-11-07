import tkinter as tk

root = tk.Tk()
root.title("Double the value")
root.geometry("300x200")

label1 = tk.Label(root, text = "Enter numerical values")
label1.pack()
entry1 = tk.Entry(root, width = 20)
entry1.pack()

label2 = tk.Label(root, text = "Result")
label2.pack()
entry2 = tk.Entry(root, width = 20)
entry2.pack()

def double_num():
    num = int(entry1.get())
    doubled = num * 2
    entry2.delete(0, tk.END)
    entry2.insert(0, str(doubled))

button = tk.Button(root, text = "double", command = double_num)
button.pack(pady = 20)

root.mainloop()
