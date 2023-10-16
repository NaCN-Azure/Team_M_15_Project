import tkinter as tk
import os

def register():
    username = reg_username.get()
    email = reg_email.get()
    password = reg_password.get()
    confirm_password = reg_confirm_password.get()
    
    if password == confirm_password:
        status_label.config(text=f"Registration successful for {username} with email {email}.")
    else:
        status_label.config(text="Password confirmation does not match.")

def go_back_to_login():
    root.destroy()  # Close the registration window
    os.system("python pages/log.py")  # Open the login page

# Create the main window
root = tk.Tk()
root.title("Registration Page")

# Increase the size of the window
root.geometry("400x300")

# Registration Section
reg_frame = tk.Frame(root)
reg_frame.pack(pady=20)

reg_label = tk.Label(reg_frame, text="Registration", font=("Helvetica", 16))
reg_label.grid(row=0, column=0, columnspan=2)

reg_username_label = tk.Label(reg_frame, text="Username", font=("Helvetica", 12))
reg_username_label.grid(row=1, column=0)
reg_username = tk.Entry(reg_frame, font=("Helvetica", 12))
reg_username.grid(row=1, column=1)

reg_email_label = tk.Label(reg_frame, text="Email", font=("Helvetica", 12))
reg_email_label.grid(row=2, column=0)
reg_email = tk.Entry(reg_frame, font=("Helvetica", 12))
reg_email.grid(row=2, column=1)

reg_password_label = tk.Label(reg_frame, text="Password", font=("Helvetica", 12))
reg_password_label.grid(row=3, column=0)
reg_password = tk.Entry(reg_frame, show="*", font=("Helvetica", 12))
reg_password.grid(row=3, column=1)

reg_confirm_password_label = tk.Label(reg_frame, text="Confirm Password", font=("Helvetica", 12))
reg_confirm_password_label.grid(row=4, column=0)
reg_confirm_password = tk.Entry(reg_frame, show="*", font=("Helvetica", 12))
reg_confirm_password.grid(row=4, column=1)

button_frame = tk.Frame(reg_frame)
button_frame.grid(row=5, column=0, columnspan=2)

register_button = tk.Button(button_frame, text="Register", command=register, font=("Helvetica", 12))
register_button.grid(row=0, column=0, padx=5)

go_back_button = tk.Button(button_frame, text="Go back to login page", command=go_back_to_login, font=("Helvetica", 12))
go_back_button.grid(row=0, column=1, padx=5)

# Status Label
status_label = tk.Label(root, text="", font=("Helvetica", 12))
status_label.pack()

root.mainloop()
