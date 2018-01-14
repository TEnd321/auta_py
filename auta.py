import tkinter as tk
import time
import math
import random

a=1
e=1
ta = lambda: math.trunc(time.time() * 100)
tb = 0
te = lambda: (ta() - tb) / 100

def autoBlueDraw(x,y=45):
	#can1.delete("all")
	can1.create_polygon(x+18,y,x+46,y,x+53,y+9,x+69,y+9,x+70,y+10,x+71,y+10,x+72,y+11,x+72,y+12,x+73,y+13,x+73,y+17,x+72,y+18,x+72,y+19,x+71,y+20,x+70,y+20,x+69,y+21,x+2,y+21,x,y+19,x,y+12,x+2,y+10,x+4,y+10,x+18,y,fill="#00A")
	can1.create_oval(x+13,y+16,x+22,y+25,fill="#BBB")
	can1.create_oval(x+56,y+16,x+65,y+25,fill="#BBB")
	can1.create_oval(x+16,y+19,x+19,y+22,fill="#777")
	can1.create_oval(x+59,y+19,x+62,y+22,fill="#777")
	can1.create_polygon(x+35,y+3,x+35,y+8,x+36,y+9,x+47,y+9,x+48,y+8,x+44,y+2,x+36,y+2, fill="#66FFFF",outline="#000")
	can1.create_polygon(x+33,y+3,x+33,y+8,x+32,y+9,x+25,y+9,x+24,y+8,x+24,y+5,x+26,y+2,x+32,y+2,fill="#66FFFF",outline="#000")
	can1.create_polygon(x+21,y+9,x+14,y+9,x+15,y+7,x+19,y+3,x+21,y+3, fill="#66FFFF",outline="#000")
	can1.create_polygon(x+67,y+9,x+69,y+9,x+70,y+10,x+71,y+10,x+72,y+11,x+72,y+12,x+73,y+13,x+73,y+14,x+69,y+14,x+67,y+12,fill="#FF0",outline="#000")
	can1.create_polygon(x,y+13,x+3,y+13,x+4,y+14,x+4,y+16,x,y+16,x,y+13,fill="#F00",outline="#000")
	can1.create_polygon(x+4,y+16,x,y+16,x,y+18,x+3,y+18,x+4,y+17,fill="#ff7b00",outline="#000")

def autoRedDraw(x1,y1=110):
	can1.create_polygon(x1+2,y1,x1+43,y1,x1+46,y1+3,x1+46,y1+11,x1+49,y1+15,x1+70,y1+15,x1+73,y1+18,x1+73,y1+26,x1+72,y1+27,x1+72,y1+28,x1+71,y1+29,x1+70,y1+29,x1+69,y1+30,x1+2,y1+30,x1,y1+28,x1,y1+2,fill="#00960f",outline="#000")
	can1.create_oval(x1 + 13, y1 + 25, x1 + 22, y1 + 34, fill="#BBB")
	can1.create_oval(x1 + 56, y1 + 25, x1 + 65, y1 + 34, fill="#BBB")
	can1.create_oval(x1 + 16, y1 + 28, x1 + 19, y1 + 31, fill="#777")
	can1.create_oval(x1 + 59, y1 + 28, x1 + 62, y1 + 31, fill="#777")
	can1.create_polygon(x1+70,y1+17,x1+72,y1+17,x1+73,y1+18,x1+73,y1+23,x1+70,y1+23,x1+69,y1+22,x1+69,y1+18, fill="#FF0", outline="#000")
	can1.create_polygon(x1+43,y1+14,x1+43,y1+5,x1+41,y1+3,x1+30,y1+3,x1+30,y1+14,fill="#66FFFF",outline="#000")
	can1.create_rectangle(x1+27,y1+3,x1+17,y1+14,fill="#66FFFF", outline="#000")
	can1.create_rectangle(x1+2,y1+3,x1+11,y1+12,fill="#66FFFF", outline="#000")
	can1.create_line(x1+14,y1+3,x1+14,y1+22)
	can1.create_rectangle(x1+54,y1+12,x1+64,y1+14, fill="#000", outline="#000")
	can1.create_rectangle(x1,y1+17,x1+4,y1+24,fill="#f00",outline="#000")
	can1.create_rectangle(x1,y1+22,x1+4,y1+26,fill="#ff7b00",outline="#000")

def precedence():
	global tb
	tb = ta()
	masterRace()

def masterRace():
	global a,e
	finish=900-73
	can1.delete("all")
	finishLine()
	lab2.config(text=te())
	finishLine()
	a+=random.randint(1,5)
	b=random.randint(1,5)
	c=random.randint(1,10)
	if c < 3:
		autoBlueDraw(a)
		e+=1
		autoRedDraw(e)
	else:
		autoBlueDraw(a)
		e+=b
		autoRedDraw(e)
	if a > finish:
		a,e = 1,1
		wonWin(0)
		return
	if e > finish:
		a,e = 1,1
		wonWin(1)
		return
	can1.after(40,masterRace)

def finishLine():
	can1.create_rectangle(900,5,905,195)

def restart():
	can1.delete("all")
	finishLine()
	autoRedDraw(2)
	autoBlueDraw(2)
	lab2.config(text="0.00")

def wonWin(winner):
	win1 = tk.Tk()
	canw = tk.Canvas(win1, width=120, height=30)
	if winner == 0:
		canw.config(bg="#aad7ff")
		canw.create_text(60,15, text="Vyhralo modré auto")
	if winner == 1:
		canw.config(bg="#bfffc5")
		canw.create_text(60,15,text="Vyhralo zelené auto")
	butw = tk.Button(win1,text="Zatvoriť",command=win1.destroy)
	canw.pack()
	butw.pack()
	win1.mainloop()

main = tk.Tk()

but1 = tk.Button(main,text="Start",width=40,command=precedence)
but2 = tk.Button(main,text="ReStart",width=40,command=restart)
entry1 = tk.Entry(main, width=40)
can1 = tk.Canvas(main, width=1000,height=200, bg = "#FFFFFF")
lab1 = tk.Label(main, text='Uplynuty cas:')
lab2 = tk.Label(main, text='0.00')

finishLine()
autoRedDraw(2)
autoBlueDraw(2)

lab1.grid(row = 0, column = 0, columnspan = 1)
lab2.grid(row = 0, column = 1)
can1.grid(row = 1, column = 0, columnspan = 2)
but1.grid(row = 2, column = 0)
but2.grid(row = 2, column = 1)

main.mainloop()