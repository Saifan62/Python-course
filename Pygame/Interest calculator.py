import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        principal = float(entry_principal.get())
        time = float(entry_time.get())
        rate = float(entry_rate.get())

        simple_interest = (principal * time * rate) / 100
        compound_interest = principal * ((1 + rate/100) ** time - 1)
        messagebox.showinfo()
