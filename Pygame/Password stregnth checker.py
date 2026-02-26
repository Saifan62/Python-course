import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("600x600")

def check_password_strength():
    password = password_entry.get()
    if len(password) < 6:
        messagebox.showwarning("Weak Password", "Password must be at least 6 characters long.")
    elif not any(char.isdigit() for char in password):
        messagebox.showwarning("Weak Password", "Password must contain at least one number.")
    elif not any(char.isupper() for char in password):
        messagebox.showwarning("Weak Password", "Password must contain at least one uppercase letter.")

    elif not any(char in "!@#$%^&*()-+?_=,<>/." for char in password):
        messagebox.showwarning("Weak Password", "Password must contain at least one special character.")
    else:
        messagebox.showinfo("Strong Password", "Your password is strong.")

password_label = tk.Label(root, text="Enter your password:", font=("Komika", 30), fg="#0e9e8d", pady=20)
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

check_button = tk.PhotoImage(file="button_check-password.png")
chck_btn= tk.Button(root, image=check_button, command=check_password_strength, border=0)
chck_btn.pack(pady=50)




root.mainloop()