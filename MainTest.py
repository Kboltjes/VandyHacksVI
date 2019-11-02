import tkinter as tk
from PIL import Image, ImageTk
import cv2
import pyqrcode
import PySimpleGUI as gui


def hello(event):
    print("Single Click")



window = tk.Tk()
window.title("Glove Sizer")
window.geometry("1500x900")
window.configure(background='white')

# img = cv2.imread('moon.png', cv2.IMREAD_UNCHANGED)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)



navtext = tk.Text(window, height=3, width=1000, background='#6DA295')
navtext.tag_configure('color', foreground='#000000')
navtext.tag_configure('big', font=('Proxima Nova Soft', 30, 'bold'))
navtext.pack(anchor="nw", padx=0, pady=0)
navtext.insert(tk.END, "Hillman", 'big')
navtext.config(state=tk.DISABLED)

instructtext = tk.Text(window, height=10, width=110, background='grey')
instructtext.tag_configure('color', foreground='#000000', font=('Georgia', 18))
instructtext.pack(anchor="ne", side="right", padx=10, pady=10)
instructtext.insert(tk.END, "These are the instructions....", 'color')
instructtext.config(state=tk.DISABLED)

image = Image.open('moon.png')
image = image.resize((400, 400), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label = tk.Label(window, image=photo)
label.image = photo
label.pack(anchor="nw", side="left", padx=10, pady=10)

button = tk.Button(window,
                   text="Submit",
                   width=100,
                   height=5)
button.pack(anchor="n", side="left", padx=0, pady=10)
button.bind('<Button-1>', hello)



# url = pyqrcode.create('https://www.wikipedia.org/' + '?=')

# url.png('wiki.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])

# rightLbl = tk.Label(window, image=url)
# rightLbl.pack(side="right", padx=10, pady=10)


# a = tk.Label(window, image=ImageTk.PhotoImage(image)) #ImageTk.PhotoImage(Image.fromarray(img)))
# a.place(x=20, y=30, width=500, height=500)

# print('Original Dimensions : ', img.shape)

# scale_percent = 50  # percent of original size
# width = int(img.shape[1] * scale_percent / 100)
# height = int(img.shape[0] * scale_percent / 100)
# dim = (width, height)
# resize image
# resized = cv2.resize(img, dim)
# print('Resized Dimensions : ', resized.shape)

# l = tk.Label(window, image=ImageTk.PhotoImage(Image.fromarray(resized)))
# l.place(x=500, y=500, width=width, height=height)

#Start the GUI
window.mainloop()

# cv2.imshow("Resized image", resized)
# images = gui.Image("moon.png")
# url.show()

# url.show()
# cv2.waitKey(0)
# cv2.destroyAllWindows()