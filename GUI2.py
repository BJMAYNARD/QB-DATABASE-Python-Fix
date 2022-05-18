import tkinter
import tkinter as tk
from tkinter import *


def task_message():
    # The window will stay open until this function call ends. Timed it to 25 seconds
    root.destroy()


root = Tk()
root.title(string='')
root.geometry('300x75')


frame1 = LabelFrame(
    root,
    text='QB FIX IN PROGRESS',
    bg='#BFC9CA',
    font=(20),
)
T = tk.Text(root, height=2.2, width=35)
T.pack()
T.insert(tk.END, " Window Will Close When Process Is Completed. Thank You")
frame1.pack(expand=True, fill=BOTH)
root.after(25000, task_message)
root.mainloop()
