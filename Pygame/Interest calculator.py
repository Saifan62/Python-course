import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        principal = float(entry_principal.get())
        time = float(entry_time.get())
        rate = float(entry_rate.get())

        simple_interest = (principal * time * rate) / 100
        compound_interest = principal * ((1 + rate/100) ** time - 1)
        messagebox.showinfo("Result",
                            f"Simple Interest: {simple_interest:.2f}\n"
                            f"Compound Interest: {compound_interest:.2f}"
                            )
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

root = tk.Tk()
root.title("Interest Calculator")

tk.Label(root,text="Principal Amount:").grid(row=0, column=0, padx=10, pady=5)
entry_principal = tk.Entry(root)
entry_principal.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root,text="Time (years):").grid(row=1, column=0, padx=10, pady=5)
entry_time = tk.Entry(root)
entry_time.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root,text="Rate of Interest (%):").grid(row=2, column=0, padx=10, pady=5)
entry_rate = tk.Entry(root)
entry_rate.grid(row=2, column=1, padx=10, pady=5)

tk.Button(root, text="Calculate Interest", command=calculate_interest).grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()


