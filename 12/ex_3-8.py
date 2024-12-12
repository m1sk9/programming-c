import tkinter as tk
from tkinter import messagebox

users = { "admin": "1234", "user": "123", "amano": "12345" }

def login():
    try:
        username = user_entry.get()
        password = password_entry.get()
        if (username not in users) or (users[username] != password):
            messagebox.showerror("Warning", "Login Failed")
        else:
            messagebox.showinfo("Information", "Login Successful")
    except Exception:
        messagebox.showerror("Error", "An error occurred")

root = tk.Tk()
root.title("Login Screen")
root.geometry("300x200")

user_label = tk.Label(root, text="Username:")
user_label.pack()
user_entry = tk.Entry(root)
user_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=20)

root.mainloop()
