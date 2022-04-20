# !/usr/bin python3

__author__ = "Nitish Chennoju"
__credits__ = ["Colton Acosta"]

import threading
import time
import serial
import serial.tools.list_ports
from serial import SerialException
import tkinter as tk
from mttkinter import mtTkinter

# Custom Classes
import Gauge
import RelaySwitch
import PandID
import BarDisplay
import LineGraph

# imports needed for live plotting

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

msg = ''

DEBUG=False

Thermocouple_Count=4 #number of thermocouple reading that will be expexted to be displayed

# Returns list of all accessible serial ports
def getPorts():
    portData = serial.tools.list_ports.comports()
    return portData

# Returns COM port of Arduino if detected by computer. User for switchbox
def findArduino(portsFound):
    numConnections = len(portsFound)
    for i in range(0, numConnections):
        if ('Uno' in str(portsFound[i]) or 'Nano' in str(portsFound[i]) or 'CH340' in str(portsFound[i])):
            return str(portsFound[i])

        # teensy 3.6
        if ('USB Serial Device' in str(portsFound[i])):
            print(portsFound[i])
            return str(portsFound[i])
    return "None"


def conv(str):
    return str[2:len(str) - 5]

# method called by button. Message forwarded to threading function
def startup():
    global msg
    msg = 'start'
    time.sleep(0.1)
    msg = ''

# Hard code all off
# Relays (no power state), Stepper/Servo (pos = 0)
def allOff():
    try:
        if(DEBUG):
            arduinoSwitchbox.write(b'8')
            switch1.actionOff()
            time.sleep(0.001)
            switch2.actionOff()
            time.sleep(0.001)
            switch3.actionOff()
            time.sleep(0.001)
            switch4.actionOff()
            time.sleep(0.001)
            switch5.actionOff()
            time.sleep(0.001)
            switch6.actionOff()
        plumbing.s2.setPercentage(0)
        plumbing.s1.setPercentage(0)
        print("All OFF COMPLETE")
    except:
        print('Serial Error: Arduino Not Connected or Detected')
    if(DEBUG):
        switch1.setLedState(False)
        switch2.setLedState(False)
        switch3.setLedState(False)
        switch4.setLedState(False)
        switch5.setLedState(False)
        switch6.setLedState(False)
        switch7.scale.set(0)
        switch8.scale.set(0)

    plumbing.one.setState(False)
    plumbing.two.setState(False)
    plumbing.three.setState(False)
    plumbing.four.setState(False)
    plumbing.five.setState(False)
    plumbing.six.setState(False)

# THREADING METHOD
# Runs in parallel with the GUI main loop
def actionHandler():
    global msg
    global root, switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, prevCon
    while True:
        time.sleep(0.001)
        if(msg == 'start'):
            '''----------------------------
            ---- STARTUP SEQUENCE HERE ----
            ----------------------------'''

            #TEST SEQUENCE (DELETE ONCE STARTUP SEQ HAS BEEN DETERMINED)
            delay = 0.2
            delaySlider = 0.001
            if(prevCon): # if Arduino is connected via serial
                if(DEBUG):
                    continue
                for i in range(2):
                    try:
                        print('Trigger Relay 1')
                        switch1.actionOn()
                        time.sleep(delay)
                        for j in range(0, 101, 2):
                            switch7.scale.set(j)
                            time.sleep(delaySlider)
                        for j in range(0, 101, 2):
                            switch7.scale.set(100-j)
                            time.sleep(delaySlider)
                        print('Trigger Relay 2')
                        switch2.actionOn()
                        time.sleep(delay)
                        print('Trigger Relay 3')
                        switch3.actionOn()
                        time.sleep(delay)
                        for j in range(0, 101, 2):
                            if(DEBUG): switch8.scale.set(j)
                            time.sleep(delaySlider)
                        for j in range(0, 101, 2):
                            if(DEBUG): switch8.scale.set(100-j)
                            time.sleep(delaySlider)
                        print('Trigger Relay 4')
                        if(DEBUG): switch4.actionOn()
                        time.sleep(delay)
                        print('Trigger Relay 5')
                        switch5.actionOn()
                        time.sleep(delay)
                        for j in range(0, 101, 2):
                            switch7.scale.set(j)
                            time.sleep(delaySlider)
                        for j in range(0, 101, 2):
                            switch7.scale.set(100-j)
                            time.sleep(delaySlider)
                        print('Trigger Relay 6')
                        switch6.actionOn()
                        time.sleep(delay)
                        print('Trigger Relay 6')
                        switch6.actionOff()
                        time.sleep(delay)
                        print('Trigger Relay 5')
                        switch5.actionOff()
                        time.sleep(delay)
                        print('Trigger Relay 4')
                        if(DEBUG): switch4.actionOff()
                        time.sleep(delay)
                        print('Trigger Relay 3')
                        switch3.actionOff()
                        time.sleep(delay)
                        print('Trigger Relay 2')
                        switch2.actionOff()
                        time.sleep(delay)
                        print('Trigger Relay 1')
                        switch1.actionOff()
                        time.sleep(delay)
                    except:
                        print('ERROR')
            else:
                print('Serial Error: Arduino Not Connected or Detected')
                time.sleep(0.1)








if __name__ == '__main__':
    global root, switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, a, b, c, d, off, g1, g2, g3, g4, connectionLabel, plumbing, fileName, arduinoSwitchbox, prevCon

    #ACTION HANDLER THREAD (checks for startup button press)
    thread = threading.Thread(target=actionHandler)
    thread.start()

    # Get file name from user
    print("Enter file name (don't include file extension): ", end='')
    #fileName = input() + ".txt"
    fileName="log.txt"

    # Spacing constants within GUI
    pad = 10
    gridLen = 85

    # Initialize GUI Windows
    plumbing = PandID.Liquid_Engine_Plumbing(gridLen)  # P&ID diagram window

    root = tk.Tk(mt_debug = 1)
    root.title("Engine Dashboard");
    root.configure(background="green")

    tk.Label(root, text="Engine Dashboard", bg="pink", fg="white", font="Arial 30").pack(pady=40)

    # GET ARDUINO STATUS / Update on GUI connection label
    status = findArduino(getPorts())
    connectionLabel = tk.Label(root, text='DISCONNECTED ' + status, bg="black", fg="#ed3b3b", font="Arial 14")
    arduinoSwitchbox = serial.Serial()
    if (not (status == "None")):
        arduinoSwitchbox = serial.Serial(status.split()[0], 115200)
        connectionLabel.configure(text='CONNECTED ' + status, fg="#41d94d")
    connectionLabel.pack()


    # RELAY Switches created
    a = tk.Frame(root, bg='black')  # represents tow 1
    b = tk.Frame(root, bg='black')  # represents tow 2
    c = tk.Frame(root, bg='black')  # represents tow 3
    d = tk.Frame(root, bg='black')  # represents tow 4
    if(DEBUG):
        switch1 = RelaySwitch.Buttons(a, 0, arduinoSwitchbox, "Relay 1", plumbing.one)
        switch2 = RelaySwitch.Buttons(b, 1, arduinoSwitchbox, "Relay 2", plumbing.two)
        switch3 = RelaySwitch.Buttons(c, 2, arduinoSwitchbox, "Relay 3", plumbing.three)
        switch4 = RelaySwitch.Buttons(d, 3, arduinoSwitchbox, "Relay 4", plumbing.four)
        switch5 = RelaySwitch.Buttons(a, 4, arduinoSwitchbox, "Relay 5", plumbing.five)
        switch6 = RelaySwitch.Buttons(b, 5, arduinoSwitchbox, "Relay 6", plumbing.six)
        switch7 = RelaySwitch.StepperSlider(c, 0, arduinoSwitchbox)
        switch8 = RelaySwitch.StepperSlider(d, 1, arduinoSwitchbox)
    # attaches rows to root tkinter GUI
    a.pack()
    b.pack()
    c.pack()
    # barGraph=BarDisplay.BarDisplay(d, 'white', 1, Thermocouple_Count)
    # barGraph.getWidget().pack(side="left")

    lineGraph=LineGraph.LineGraph(d, count=2, datapoints=200, floor=-90, ceiling=90)

    lineFig=lineGraph.getFig()
    ani = animation.FuncAnimation(lineFig, func=lineGraph.animate, interval=100, blit=False)

    d.pack()

    g = tk.Frame(root)
    h = tk.Frame(root)
    # s = tk.Button(root, text="STARTUP", padx=40, pady=10, font="Verdana 14", bg="yellow", command=startup,
    #               activebackground="yellow")
    # off = tk.Button(root, text="All OFF", padx=30, pady=10, font="Verdana 14", bg="RED", command=allOff,
    #                 activebackground="RED")
    #
    # s.pack(pady=pad)
    # off.pack(pady=pad)


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


    i=0
    temp=0
    '''----------------------------
    ------ MAIN PROGRAM LOOP ------
    ----------------------------'''
    prevCon = True
    while True:
        temp+=1
        # ARDUINO CONNECTION CHECK
        status = findArduino(getPorts())
        if (status == "None"):
            connectionLabel.configure(text='DISCONNECTED ' + status, fg="#ed3b3b")
            g1.setText("Nan", "A0")
            g2.setText("Nan", "A1")
            g3.setText("Nan", "A2")
            g4.setText("Nan", "A3")
            prevCon = False
            print("No Line")
        elif (not prevCon and status != 'None'):
            print("Line Found")
            try:
                arduinoSwitchbox = serial.Serial(status.split()[0], 115200)
                connectionLabel.configure(text='CONNECTED ' + status, fg="#41d94d")
                if(DEBUG):
                    switch1.setArduino(arduinoSwitchbox)
                    switch2.setArduino(arduinoSwitchbox)
                    switch3.setArduino(arduinoSwitchbox)
                    switch4.setArduino(arduinoSwitchbox)
                    switch5.setArduino(arduinoSwitchbox)
                    switch6.setArduino(arduinoSwitchbox)
                    switch7.setArduino(arduinoSwitchbox)
                    switch8.setArduino(arduinoSwitchbox)
                prevCon = True
            except SerialException:
                print("ERROR: LOADING...")
        else:
            connectionLabel.configure(text='CONNECTED ' + status, fg="#41d94d")


        # Attempt to get data from Arduino
        try:
            strSerial = conv(str(arduinoSwitchbox.readline()))
        except SerialException:
            strSerial = ''#

        #data = strSerial.split("\\t")
        data = strSerial.split(",")
        print(data)
        if (data[0] == "Time"):
            # detect serial data start
            file = open(fileName, "a")
            file.write(strSerial[0:len(strSerial) - 2] + "\n")
            print('-------- BEGIN --------')
            file.close()
        elif (len(data) > 4 and data[0] != "Time"):
            file = open(fileName, "a")
            file.write((strSerial[0:len(strSerial) - 2] + "\n"))
            file.close()
            g1.setAngle(abs(5 * float(data[1])) / 1023.0)
            g1.setText(data[1], "A0")
            g2.setAngle(abs(5 * float(data[2])) / 1023.0)
            g2.setText(data[2], "A1")
            g3.setAngle(abs(5 * float(data[3])) / 1023.0)
            g3.setText(data[3], "A2")
            g4.setAngle(abs(5 * float(data[4])) / 1023.0)
            g4.setText(data[4].replace('\n', ''), "A3")

            # barGraph.changeTemp(0, float(data[38]))
            # barGraph.changeTemp(1, float(data[39]))

        # time.sleep(1)
        # i+=1

        if(DEBUG):
            plumbing.s1.setPercentage(switch8.getVal())
            plumbing.s2.setPercentage(switch7.getVal())

        plumbing.updatePipeStatus()

        #for testing when not hooked up to ECU/serial port
        lineGraph.nextPoint(temp%100, 0)
        lineGraph.nextPoint(((temp+50)%100), 1)

#must be hooked up to ECU and recieving data through serial in order to work
#        lineGraph.nextPoint(float(data[39], 0)


        root.update_idletasks()
        root.update()
        plumbing.getWindow().update()
