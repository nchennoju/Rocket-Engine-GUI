# drawing a bar graph with the Tkinter canvas and
# canvas.create_rectangle(x0, y0, x1, y1, option, ...)
# note: coordinates are relative to the top left corner of the canvas
# used a more modern import to give Tkinter items a namespace
# tested with Python24  by    vegaseat    01nov2006

#import tkinter as tk  # gives tk namespace
import random


import threading
import time
import serial
import serial.tools.list_ports
from serial import SerialException
import tkinter as tk
from mttkinter import mtTkinter

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import collections
import numpy as np
import time
import tkinter as tk
import matplotlib.pyplot as plt

# Custom Classes
import Gauge
import RelaySwitch
import PandID
import BarDisplay
import LineGraph
dataList=[0,1,2,3,4,5]
if __name__ == '__main__':
    global root, switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, a, b, c, d, off, g1, g2, g3, g4, connectionLabel, plumbing, fileName, arduinoSwitchbox, prevCon

    # Spacing constants within GUI
    pad = 10
    gridLen = 85

    # Initialize GUI Windows

    root = tk.Tk(mt_debug = 1)
    root.title("Engine Dashboard");
    root.configure(background="green")

    tk.Label(root, text="Engine Dashboard", bg="pink", fg="white", font="Arial 30").pack(pady=40)

    # GET ARDUINO STATUS / Update on GUI connection label
    # status = findArduino(getPorts())
    # connectionLabel = tk.Label(root, text='DISCONNECTED ' + status, bg="black", fg="#ed3b3b", font="Arial 14")
    # arduinoSwitchbox = serial.Serial()
    # if (not (status == "None")):
    #     arduinoSwitchbox = serial.Serial(status.split()[0], 115200)
    #     connectionLabel.configure(text='CONNECTED ' + status, fg="#41d94d")
    # connectionLabel.pack()


    # RELAY Switche created

    d = tk.Frame(root, bg='black')  # represents tow 4

    # attaches rows to root tkinter GUI

    # barGraph=BarDisplay.BarDisplay(d, 'white', 1, 2)
    # barGraph.getWidget().pack(side="left")


    #seems to be unessesary f = Figure(figsize=(12, 6), dpi=100)

    lineGraph=LineGraph.LineGraph(d, count=6, datapoints=20)

    d.pack()

    g = tk.Frame(root)
    h = tk.Frame(root)


    # ------------------------ DATA LOGGER GAUGE ELEMENTS -----------------------------
    # consists of two rows of 2 gauges
    g1 = Gauge.Gauge(g, 'black', 5)
    g1.setText("Nan", "A0")
    g1.getWidget().pack(side="left")
    g2 = Gauge.Gauge(g, 'black', 5)
    g2.setText("Nan", "A1")
    g2.getWidget().pack(side="right")
    g3 = Gauge.Gauge(h, 'black', 5)
    g3.setText("Nan", "A2")
    g3.getWidget().pack(side="left")
    g4 = Gauge.Gauge(h, 'black', 5)
    g4.setText("Nan", "A3")
    g4.getWidget().pack(side="right")
    g.pack()
    h.pack()



    lineFig=lineGraph.getFig()
    ani = animation.FuncAnimation(lineFig, func=lineGraph.animate, interval=100, blit=False)
    '''----------------------------
    ------ MAIN PROGRAM LOOP ------
    ----------------------------'''
    prevCon = True
    temp=10
    while(True):
        print("updating")
        time.sleep(0.1)
        temp+=1

        #lineGraph.nextPts(dataList)

        #dataList.append(temp%10)

        lineGraph.nextPoint(temp%10, 0)
        lineGraph.nextPoint(((temp+5)%10), 1)


        root.update()
        root.update_idletasks()
