import tkinter as tk
import os

def login():
    username = login_username.get()
    password = login_password.get()

def register():
    root.destroy()
    os.system("python pages/register.py")

# Create the main window
root = tk.Tk()
root.title("Login Page")

# Increase the size of the window
root.geometry("400x200")

# Login Section
login_frame = tk.Frame(root)
login_frame.pack(pady=20)

login_label = tk.Label(login_frame, text="Login", font=("Helvetica", 16))
login_label.grid(row=0, column=0, columnspan=2)

login_username_label = tk.Label(login_frame, text="Username", font=("Helvetica", 12))
login_username_label.grid(row=1, column=0)
login_username = tk.Entry(login_frame, font=("Helvetica", 12))
login_username.grid(row=1, column=1)

login_password_label = tk.Label(login_frame, text="Password", font=("Helvetica", 12))
login_password_label.grid(row=2, column=0)
login_password = tk.Entry(login_frame, show="*", font=("Helvetica", 12))
login_password.grid(row=2, column=1)

login_button = tk.Button(login_frame, text="Login", command=login, font=("Helvetica", 12))
login_button.grid(row=3, column=0, pady=10)

register_button = tk.Button(login_frame, text="Register", command=register, font=("Helvetica", 12))
register_button.grid(row=3, column=1, pady=10)

# Status Label
status_label = tk.Label(root, text="", font=("Helvetica", 12))
status_label.pack()

root.mainloop()
