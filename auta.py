import tkinter as tk
import time
import math
import random

def auto_draw():
	

main = tk.Tk()

but1 = tk.Button(main,text="Start")
but2 = tk.Button(main,text="ReStart")
entry1 = tk.Entry(main)
can1 = tk.Canvas(main, width=1000,height=200, bg = "#FFFFFF")
lab1 = tk.Label(main, text='Uplynuty cas:')
lab2 = tk.Label(main, text='cas')



lab1.grid(row = 0, column = 0, columnspan = 2)
lab2.grid(row = 0, column = 2)
can1.grid(row = 1, column = 0, columnspan = 3)
but1.grid(row = 2, column = 0)
but2.grid(row = 2, column = 1)
entry1.grid(row = 2, column = 2)

main.mainloop()