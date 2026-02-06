from tkinter import *
from datetime import date

root = Tk()
root.title("Widgets")
root.geometry("400x400")


lbl = Label(text="Hey There!", fg="white", bg = "#FF261F", height=1 , width=300)

name_lbl = Label(text="Full Name", bg="#FB8023")
name_entry = Entry()

def display():
    name = name_entry.get()

    global message
    message = "Welcome to the app! \n Today's date is:"
    greet = "Hello "+name+"\n"

    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height=3)

btn = Button(text='Begin', command=display, height=1, bg="#FB8023", fg="white")

lbl.pack()
name_lbl.pack()
name_entry.pack()
text_box.pack()
btn.pack()

root.mainloop()