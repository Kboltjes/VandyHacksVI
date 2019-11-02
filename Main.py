import tkinter as tk
from PIL import ImageTk, Image
import cv2


#This creates the main window of an application
window = tk.Tk()
window.title("Join")
window.geometry("300x700")
window.configure(background='grey')

path = "moon.png"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))


img2 = cv2.imread(path)
resizedImg = cv2.resize(img2, (50, 30))

imgtk = ImageTk.PhotoImage(image=resizedImg)

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image=imgtk, height=20, anchor="nw", width=20)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side="bottom", fill="both", expand="yes")

#Start the GUI
window.mainloop()