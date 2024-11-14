import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        quotient = num1 // num2
        remainder = num1 % num2
        label_result.config(text=f"商: {quotient}, 余り: {remainder}")
    except ValueError:
        messagebox.showerror("エラー", "数値を入力してください")
    except ZeroDivisionError:
        messagebox.showerror("エラー", "0で割ることはできません")

root = tk.Tk()
root.title("商と余りの計算アプリ")
root.geometry("300x200")

label_num1 = tk.Label(root, text="1つ目の数を入力:")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="2つ目の数を入力:")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

action_button = tk.Button(root, text="計算", command=calculate)
action_button.pack(pady=10)

label_result = tk.Label(root, text="商と余りがここに表示されます")
label_result.pack()

root.mainloop()
