from tkinter import Tk, Canvas

root = Tk()
root.title("Screen_Pet_Game")

c = Canvas(root, width=" 400", height="400")
c.configure(bg='gray10', highlightthickness=0)
c.body_color = 'coral'


body = c.create_oval(35, 20, 365, 350, outline=c.body_color, fill=c.body_color)
ear_left = c.create_polygon(75, 80, 75, 10, 165, 70,
                            outline=c.body_color, fill=c.body_color)
ear_right = c.create_polygon(
    255, 45, 325, 10, 320, 70, outline=c.body_color, fill=c.body_color)
foot_left = c.create_oval(
    65, 320, 145, 360, outline=c.body_color, fill=c.body_color)
foot_right = c.create_oval(
    250, 320, 330, 360, outline=c.body_color, fill=c.body_color)

eye_left = c.create_oval(
    130, 110, 160, 170, outline='black', fill='misty rose')
eye_right = c.create_oval(
    230, 110, 260, 170, outline='black', fill='misty rose')
pupil_right = c.create_oval(240, 145, 250, 155, outline='black', fill='black')
pupil_left = c.create_oval(140, 145, 150, 155, outline='black', fill='black')

# mouth_normal = c.create_line(170, 250, 200, 272, 230, 250, smooth=1, width=2)
# mouth_happy = c.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2)
# mouth_sad = c.create_line(170, 250, 200, 232, 230, 250, smooth=1, width=2)
tongue_main = c.create_rectangle(170, 250, 230, 290, outline='red', fill='red')
tongue_tip = c.create_oval(170, 285, 230, 300, outline='red', fill='red')
cheek_left = c.create_oval(70, 180, 120, 230, outline='pink', fill='pink')
cheek_right = c.create_oval(280, 180, 330, 230, outline='pink', fill='pink',)

c.pack()
root.mainloop()
