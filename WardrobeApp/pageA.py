import tkinter
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Outluk")
root.geometry('220x500')

# Create a photoimage object of the image in the path
image1 = Image.open('weather.jpg')
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test

# Position image
label1.place(x=0, y=0)
root.mainloop()