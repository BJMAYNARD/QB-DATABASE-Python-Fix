import time
from time import sleep
import tkinter
import tkinter as tk
from tkinter import *
import subprocess



def btn1():
    filepath=r"C:\Users\QB test\Desktop\Services\Services.bat"
    subprocess.Popen(filepath)


# GUI Creation
ws = Tk()
ws.title(string='')
ws.geometry('500x100')

frame1 = LabelFrame(
    ws,
    text='QB QUICK FIX',
    bg='#BFC9CA',
    font=(20),
)
frame1.pack(expand=True, fill=BOTH)

Button(
    frame1,
    bg='white',
    text='Click Here To Fix Services - Windows Will Close After',
    font=(30),
    command=btn1
   
    
    
).pack()
ws.after(25000, lambda: ws.destroy()) # Destroy the widget after 25 seconds
ws.mainloop()
exit()



