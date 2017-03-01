import tkinter as tk
import time
import math
import random

main = tk.Tk()

but1 = tk.Button(main,text="sgfhilsggjofsduh")
but2 = tk.Button(main,text="adsfsafgsad")
entry1 = tk.Entry(main)
can1 = tk.Canvas(main, width=200,height=200, bg = "#FFFFFF")

can1.grid(row = 1, column = 0, columnspan = 3)
but1.grid(row = 2, column = 0)
but1.grid(row = 2, column = 1)
but1.gird(row = 2, column = 2)

main.mainloop()