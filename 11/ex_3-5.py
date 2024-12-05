import tkinter as tk

root = tk.Tk()
root.title("ランダムデータでのグラフ描画")
root.geometry("200x200")

draw_button = tk.Button(root, text="グラフを描画")
draw_button.pack()

root.mainloop()
