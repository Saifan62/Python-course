from tkinter import *
from tkinter import messagebox


root=Tk()
root.title("Denomination Calculator")
root.geometry("600x600")

Label1 = Label (
    root,
    text="Hey User! Welcome to the Denomination Counter Application",
    bg="lightblue"
)
Label1.place(relx=0.5, y=340,anchor=CENTER)

def msg():
    MsgBox= messagebox.showinfo(
        'Denomination Counter',
        'Do you want to calculate the denomination count?'
    )
    if MsgBox == 'ok':
        topwin()

btn1= Button(
    root,
    text="Click to start",
    command=msg,
    bg="brown",
    fg="white",
)
btn1.place(x=260, y=360)

def topwin():
    top= Toplevel()
    top.title("Denomination Counter")
    top.config(bg="lightblue")
    top.geometry("600x600")

    label= Label(top, text='Enter total amount', bg="light grey")
    entry = Entry(top)

    lbl= Label(
        top,
        text="Here are number of notes for each denomination",
        bg="light grey"
    )

    l1 = Label(top, text="2000", bg="light grey")
    l2 = Label(top, text="500", bg="light grey")
    l3 = Label(top, text="100", bg="light grey")

    t1= Entry(top)
    t2= Entry(top)
    t3= Entry(top)

    def calculator():
        try:
            amount = int(entry.get())

            note2000 = amount // 2000
            amount %= 2000

            note500 = amount // 500
            amount %= 500

            note100 = amount // 100
            
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))

        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid integer amount")

    btn = Button(
        top,
        text="Calculate",
        command=calculator,
        bg="brown",
        fg="white"
    )

    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)

    lbl.place(x=140, y=120)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    top.mainloop()
root.mainloop()
