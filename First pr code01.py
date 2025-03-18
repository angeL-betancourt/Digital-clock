from tkinter import *
from tkinter.ttk import *
from time import strftime


top=Tk()
top.title("Digital Clock")
def none():
    text=strftime(' %H:%M:%S %P ')
    lbl.config(text=text)
    lbl.after(1000,none)
lbl=Label(top,font=('digital-7', 50,'bold'),
          background='green',foreground='blue')
lbl.pack(anchor='center')
none()
mainloop()
