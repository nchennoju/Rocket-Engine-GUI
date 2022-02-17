# !/usr/bin/env python3
from tkinter import *

#UNCOMMENT IF TESTING
'''import tkinter as tk
import time
import math
import random'''

class BarDisplay:

    def __init__(self, root, background, max):
        self.max = max
        self.c = Canvas(root, width=300, height=200, bg=background, highlightthickness=0)

        size = 180


    def setAngle(self, value):
        #Gauge bounds set
        theta = self.endAngle - ((value / self.max) * abs(self.endAngle - self.startAngle))

        if(theta > self.endAngle):
            theta = self.endAngle
        if(theta < self.startAngle):
            theta = self.startAngle

        self.c.itemconfig(self.dark, start=self.startAngle, extent=theta - self.startAngle)
        self.c.itemconfig(self.light, start=theta, extent=self.endAngle - theta)

    def getWidget(self):
        return self.c

    def setText(self, str, label):
        self.c.itemconfig(self.readout, text=str)
        self.c.itemconfig(self.label, text=label)




#GAUGE TEST CODE
'''win = tk.Tk()
win.title("Gauge ELement")
win.geometry("800x200")
win.configure(bg='black')

g = Gauge(win, 'black', 5)
g.getWidget().pack(side='bottom')
while True:

    for i in range(6):
        g.setAngle(i)
        time.sleep(0.1)
        win.update()

    for i in range(6):
        g.setAngle(5-i)
        time.sleep(0.1)
        win.update()

win.mainloop()'''
