from tkinter import Label, Tk
import time

app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("420x150")
app_window.resizable(1, 1)

# font of the time and its colour, its border width and the background colour of the digital clock
font_text = ("Boulder", 68, 'bold')
background = "#f2e750"
foreground = "#363529"
border_width = 25

label = Label(app_window, font=font_text, bg=background,
              fg=foreground, bd=border_width)
label.grid(row=0, column=1)


def digital_clock():
    pass


digital_clock()
app_window.mainloop()
