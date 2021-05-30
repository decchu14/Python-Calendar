from tkinter import *

window = Tk()
window.config(background='red4')


def from_kg():
    gram = float(e2_value.get())*1000
    pound = float(e2_value.get())*2.20462
    ounce = float(e2_value.get()) * 35.274

    t1.delete("1.0", END)
    t1.insert(END, gram)

    t2.delete("1.0", END)
    t2.insert(END, pound)

    t3.delete("1.0", END)
    t3.insert(END, ounce)


e1 = Label(window, text="Enter the weight in KG:", font=("Cambria Math", 16, "bold italic"), bg="red4",
           fg="peach puff")
e2_value = StringVar()
e2 = Entry(window, bg="peach puff", textvariable=e2_value)
e3 = Label(window, text="Grams", font=("Cambria Math", 16, "bold italic"), bg="red4",
           fg="peach puff")
e4 = Label(window, text="Pounds", font=("Cambria Math", 16, "bold italic"), bg="red4",
           fg="peach puff")
e5 = Label(window, text="Ounces", font=("Cambria Math", 16, "bold italic"), bg="red4",
           fg="peach puff")

e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)
e4.grid(row=1, column=1)
e5.grid(row=1, column=2)

t1 = Text(window, height=5, width=30, bg="peach puff")
t2 = Text(window, height=5, width=30, bg="peach puff")
t3 = Text(window, height=5, width=30, bg="peach puff")

t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)

b1 = Button(window, text="Convert", bg="peach puff",
            fg="red4", command=from_kg)
b1.grid(row=0, column=2)

window.mainloop()
