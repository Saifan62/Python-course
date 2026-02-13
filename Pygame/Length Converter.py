import tkinter as tk
root=tk.Tk()
root.title("Length Converter")
root.geometry("600x600")

label= tk.Label(text="Enter the length in meters", font=("Times New Roman", 30), fg="#9d07e8", pady=20)
entry= tk.Entry(fg="#9d07e8",  width=40, font=("Times New Roman", 20), justify="center", border=0)
label.pack()
entry.pack()

def convert_to_cm():
    try:
        inches = float(entry.get())
        cm= inches * 2.54
        result_label.config(text=f"{inches} inches is equal to {cm:.2f} cm")
    except ValueError:
        result_label.config(text="Please enter a valid number")

round= tk.PhotoImage(file="button_convert-to-cm.png")
round_btn= tk.Button(root, image=round, command=convert_to_cm, border=0)

result_label= tk.Label(text="", font=("Arial", 12), fg="#9d07e8")
round_btn.pack(pady=10)
result_label.pack()

def convert_to_mm():
    try:
        inches = float(entry.get())
        mm = inches * 25.4
        result_label.config(text=f"{inches} inches is equal to {mm:.2f} mm")
    except ValueError:
        result_label.config(text="Please enter a valid number")

round2= tk.PhotoImage(file="button_convert-to-mm.png")
round_btn2= tk.Button(root, image=round2, command=convert_to_mm, border=0)
round_btn2.pack(pady=10)

result_label= tk.Label(text="", font=("Arial", 12), fg="#9d07e8")

result_label.pack()



root.mainloop()



