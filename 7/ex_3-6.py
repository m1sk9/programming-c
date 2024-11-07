import tkinter as tk

root = tk.Tk()
root.title("Display numerical totals")

entry = tk.Text(root, width = 60, height = 20)
entry.pack()

label = tk.Label(root, text = "Result: ")
label.pack()

def calc_sum():
    entry_str = entry.get("1.0", tk.END)
    num_list = entry_str.strip().splitlines()
    total = 0
    for num in num_list:
        total += int(num)
    label["text"] = f"Result: {total}"

button = tk.Button(root, text = "Show Total", command = calc_sum)
button.pack(pady = 20)

root.mainloop()
