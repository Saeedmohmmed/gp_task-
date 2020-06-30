from tkinter import *
import os

def Greffti():
    os.system('Greffti.py')
    
def mousedraw():
    os.system('unistork.py')

i = 0
def screen():
    myScreenshot.save(r'C:\Users\zamzam\Desktop\{}.png'.format(i))

win = Tk()

win.geometry('1000x500')
win.title("GpTask")
buton = Button(text = "unistark", fg = "red",command=mousedraw).place(x = 100,y=300)
buton = Button(text = "Graffeti", fg = "red",command=Greffti).place(x = 400,y=300)
win.mainloop()
