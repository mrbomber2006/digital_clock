from tkinter import *
from time import *

window = Tk()
window.title("digital clock")
window.geometry("600x400")


def The_time():
    hour = strftime("%I")
    minute = strftime("%M")
    second = strftime("%S")
    am_pm = strftime("%p")
    day = strftime("%A")
    zone = strftime("%Z")
    myText = hour + ":" + minute + ":" + second + " " + am_pm
    myText2 = day + ", " + zone
    mylable.config(text=myText)
    mylable2.config(text=myText2)
    mylable.after(1000, The_time)

mylable = Label(window, text="", font=("Arial", 69), fg="yellow", bg="black")
mylable.pack()

mylable2 = Label(window, text="", font=("Arial", 24), fg="black")
mylable2.pack()

The_time()
window.mainloop()
