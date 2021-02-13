# !/usr/bin/env python3
from tkinter import *

#UNCOMMENT IF TESTING
import time
from random import randint
import tkinter as tk

import Nozzle
import Tank
import Valves
import Pipes
import Header

gridLen = 100

width = gridLen*7
height = gridLen*10

win = tk.Tk()
win.title("ELEMENT TEST")
win.geometry(str(width) + "x" + str(height))
win.configure(bg='black')

win_w = width
win_h = height

#HEADER
header = Header.Header(win, 'black', 'SDR P&ID GUI', width, gridLen, 24)
header.getWidget().place(x=gridLen*0, y=gridLen*0)

#All TANKS
he = Tank.Tank(win, 'black', 'He', '#1d2396', gridLen, gridLen)
gn2 = Tank.Tank(win, 'black', 'GN2', '#1d2396', gridLen, gridLen)
lox = Tank.Tank(win, 'black', 'LOx', '#1d2396', gridLen, gridLen)
k = Tank.Tank(win, 'black', 'K', '#1d2396', gridLen, gridLen)
he.getWidget().place(x=gridLen*1, y=gridLen*1)
gn2.getWidget().place(x=gridLen*3, y=gridLen*1)
lox.getWidget().place(x=gridLen*1, y=gridLen*4)
k.getWidget().place(x=gridLen*5, y=gridLen*4)

#CONSTANT
fluidColor = '#41d94d'

#All SOLENOID VALVES
one = Valves.Solenoid(win, 'black', 1, gridLen, gridLen, True, False, True, False, fluidColor, True, False, True, False)
seven = Valves.Solenoid(win, 'black', 7, gridLen, gridLen, False, False, True, True, fluidColor, False, False, True, True)
four = Valves.Solenoid(win, 'black', 4, gridLen, gridLen, False, True, False, True, fluidColor, False, True, False, True)
five = Valves.Solenoid(win, 'black', 5, gridLen, gridLen, False, True, False, True, fluidColor, False, True, False, True)
loxFD = Valves.Solenoid(win, 'black', 5, gridLen, gridLen, False, True, False, True, fluidColor, False, True, False, True)
one.getWidget().place(x=gridLen*1, y=gridLen*2)
seven.getWidget().place(x=gridLen*5, y=gridLen*2)
four.getWidget().place(x=gridLen*2, y=gridLen*6)
five.getWidget().place(x=gridLen*4, y=gridLen*6)
loxFD.getWidget().place(x=gridLen*0, y=gridLen*5)

#All STEPPER VALVES
s1 = Valves.Stepper(win, 'black', gridLen, gridLen, True, True, True, False, fluidColor, True, True, True, False,)
s2 = Valves.Stepper(win, 'black', gridLen, gridLen, True, False, True, True, fluidColor, True, False, True, True)
s1.getWidget().place(x=gridLen*1, y=gridLen*6)
s2.getWidget().place(x=gridLen*5, y=gridLen*6)

#All ORIFICEs
o1 = Valves.Orifice(win, 'black', gridLen, gridLen, False, True, False, True, '#41d94d', False, True, False, True)
o2 = Valves.Orifice(win, 'black', gridLen, gridLen, True, False, True, False, '#41d94d', True, False, True, False)
o1.getWidget().place(x=gridLen*2, y=gridLen*7)
o2.getWidget().place(x=gridLen*5, y=gridLen*7)

#All Pressure Sensors
p1 = Valves.PressureSensor(win, 'black', gridLen, gridLen, False, True, False, False, '#41d94d', False, False, False, False)
p2 = Valves.PressureSensor(win, 'black', gridLen, gridLen, False, False, False, True, '#41d94d', False, False, False, False)
p3 = Valves.PressureSensor(win, 'black', gridLen, gridLen, False, False, True, True, '#41d94d', False, False, False, False)
p1.getWidget().place(x=gridLen*0, y=gridLen*3)
p2.getWidget().place(x=gridLen*6, y=gridLen*3)
p3.getWidget().place(x=gridLen*4, y=gridLen*7)

#All PIPES
p1 = Pipes.Pipe(win, 'black', gridLen, gridLen, True, True, True, False, '#41d94d', False)
p2 = Pipes.Pipe(win, 'black', gridLen, gridLen, False, True, False, True, '#41d94d', False)
p3 = Pipes.Pipe(win, 'black', gridLen, gridLen, True, False, True, True, '#41d94d', False)
p4 = Pipes.Pipe(win, 'black', gridLen, gridLen, True, False, True, False, '#41d94d', False)
p5 = Pipes.Pipe(win, 'black', gridLen, gridLen, True, True, True, False, '#41d94d', False)
p6 = Pipes.Pipe(win, 'black', gridLen, gridLen, True, False, True, False, '#41d94d', False)
p7 = Pipes.Pipe(win, 'black', gridLen, gridLen, True, False, True, True, '#41d94d', False)
p8 = Pipes.Pipe(win, 'black', gridLen, gridLen, True, False, True, False, '#41d94d', False)
p9 = Pipes.Pipe(win, 'black', gridLen, gridLen, True, True, True, False, '#41d94d', False)
p10 = Pipes.Pipe(win, 'black', gridLen, gridLen, True, True, False, True, '#41d94d', False)
p11 = Pipes.Pipe(win, 'black', gridLen, gridLen, True, True, False, False, '#41d94d', False)
p12 = Pipes.Pipe(win, 'black', gridLen, gridLen, False, True, True, True, '#41d94d', False)
p13 = Pipes.Pipe(win, 'black', gridLen, gridLen, True, True, False, False, '#41d94d', False)
p14 = Pipes.Pipe(win, 'black', gridLen, gridLen, True, False, False, True, '#41d94d', False)
p1.getWidget().place(x=gridLen*3, y=gridLen*2)
p2.getWidget().place(x=gridLen*4, y=gridLen*2)
p3.getWidget().place(x=gridLen*1, y=gridLen*3)
p4.getWidget().place(x=gridLen*3, y=gridLen*3)
p5.getWidget().place(x=gridLen*5, y=gridLen*3)
p6.getWidget().place(x=gridLen*3, y=gridLen*4)
p7.getWidget().place(x=gridLen*1, y=gridLen*5)
p8.getWidget().place(x=gridLen*3, y=gridLen*5)
p9.getWidget().place(x=gridLen*5, y=gridLen*5)
p10.getWidget().place(x=gridLen*3, y=gridLen*6)
p11.getWidget().place(x=gridLen*1, y=gridLen*7)
p12.getWidget().place(x=gridLen*3, y=gridLen*7)
p13.getWidget().place(x=gridLen*4, y=gridLen*8)
p14.getWidget().place(x=gridLen*5, y=gridLen*8)

#NOZZLE
n = Nozzle.Nozzle(win, 'black', gridLen, gridLen*1.5)
n.getWidget().place(x=gridLen*3, y=gridLen*8)

win.mainloop()