from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Virus Detector")
root.geometry('200x200')

def msg():
    messagebox.showwarning("Alert", "Potential virus detected!")

button = Button(root, text="Scan for Viruses", command=msg)
button.place(x=40, y=80)

root.mainloop()