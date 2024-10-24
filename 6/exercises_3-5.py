import tkinter as tk

def calc(op):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if op == 'add':
            result = num1 + num2
        elif op == 'sub':
            result = num1 - num2
        elif op == 'mul':
            result = num1 * num2
        elif op == 'div':
            result = num1 / num2
        result_label.config(text=f"Result of {op}: {result}")
    except ValueError:
        result_label.config(text="Please enter a number")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x300")

entry1 = tk.Entry(root)
entry1.pack(pady=10)
entry2 = tk.Entry(root)
entry2.pack(pady=10)

btn_add = tk.Button(root, text="+", command=lambda: calc('add'))
btn_add.pack(padx=10)

btn_sub = tk.Button(root, text="-", command=lambda: calc('sub'))
btn_sub.pack(padx=10)

btn_mul = tk.Button(root, text="*", command=lambda: calc('mul'))
btn_mul.pack(padx=10)

btn_div = tk.Button(root, text="/", command=lambda: calc('div'))
btn_div.pack(padx=10)

result_label = tk.Label(root, text="Calculation Result: ")
result_label.pack(pady=20)

root.mainloop()
