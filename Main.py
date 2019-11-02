from tkinter import *
import PIL

top = Tk()
# Code to add widgets will go here...

canvas = Canvas(top, width=300, height=300)
canvas.pack()
img = PhotoImage(file="ball.ppm")
canvas.create_image(20,20, anchor=NW, image=img)

top.mainloop()