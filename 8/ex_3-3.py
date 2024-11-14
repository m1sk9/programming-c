import tkinter as tk

root = tk.Tk()
root.title("テキストファイルの文字数表示")
root.geometry("400x300")

def count_chars():
    try:
        with open("./text01.txt", "r", encoding="utf-8") as f:
            text = f.read()
            result.config(text=f"文字数: {len(text)}")
    except FileNotFoundError:
        result.config(text="ファイルが見つかりません")
    except UnicodeDecodeError:
        result.config(text="ファイルがテキスト形式ではありません")

action_button = tk.Button(root, text="テキストファイルを開く", command=count_chars)
action_button.pack(pady=10)

result = tk.Label(root, text="文字数がここに表示されます")
result.pack()

root.mainloop()
