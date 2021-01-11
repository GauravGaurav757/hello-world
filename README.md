# hello-world
first repository

import tkinter as tk

import time as tm

import datetime

now = datetime.datetime.now()

my_window = tk.Tk()

my_window.title('Current Date and Time')

current_Time=now.strftime("%Y-%m-%d %H:%M:%S")

clock_label=tk.Label(my_window,font='ariel 80',bg='black',fg='red',text=current_Time)

clock_label.grid(row=0,column=0)

my_window.mainloop()
