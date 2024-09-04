# Following this guide: https://www.geeksforgeeks.org/create-first-gui-application-using-python-tkinter/

from tkinter import *

root = Tk()

root.title("Clicky Thing")
root.geometry('500x500')

lbl = Label(root, text = "Enter the celcius temperature you wish to convert to fahrenheit:")
lbl.grid()

txt = Entry(root, width=10)
txt.grid(column=4,row=4)

Tc = txt.get()

float(Tc)

Tf = Tc * 9 / 5 + 32

def clicked():
    res = "Temp in Fahrenheit is:" + " " + Tf
    lbl.configure(text = res)

btn = Button(root, text = "Click to convert",
        fg = "green", command=clicked)

btn.grid(column=5, row=5)

root.mainloop()
