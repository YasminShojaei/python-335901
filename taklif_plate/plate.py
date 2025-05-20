from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as msg
import re
from plate_validation import *


def check_plate():
    p1 = first.get()
    p2 = second.get()
    p3 = third.get()
    p4 = fourth.get()

    plate_sting = f"{p1}{p2}{p3}{p4}"
    print("Ypur plate is: ", plate_sting)

    if not plate_validation(plate_sting):
        msg.showerror("NOT VALID", "Plate is not correct")
    else:
        msg.showinfo("Your plate was saved", "saved!")


window = Tk()

window.title("my plate")
window.geometry("1212x373")

img = Image.open("d:/python/python 335901/taklif_plate/plate.png")
photo = ImageTk.PhotoImage(img)

my_lable = Label(window, image=photo)
my_lable.image = photo
my_lable.pack()


first = IntVar()
Entry(window, textvariable=first, font=("B Traffic", 120)).place(
    x=175, y=90, width=170, height=170)

second = StringVar()
Entry(window, textvariable=second, font=("B Traffic", 120)).place(
    x=360, y=90, width=170, height=170)

third = IntVar()
Entry(window, textvariable=third, font=("B Traffic", 120)).place(
    x=549, y=90, width=320, height=170)

fourth = IntVar()
Entry(window, textvariable=fourth, font=("B Traffic", 120)).place(
    x=900, y=120, width=180, height=150)

Button(window, text="check my plate", command=check_plate,
       font=("B Traffic", 15)).place(x=175, y=300)

window.mainloop()
