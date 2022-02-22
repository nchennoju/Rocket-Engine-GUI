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

# Custom Classes
import Gauge
import RelaySwitch
import PandID
import BarDisplay

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

    barGraph=BarDisplay.BarDisplay(d, 'white', 1)
    barGraph.getWidget().pack(side="left")
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


    '''----------------------------
    ------ MAIN PROGRAM LOOP ------
    ----------------------------'''
    prevCon = True
    temp=10
    while(True):
        print("updating")
        time.sleep(0.5)
        barGraph.changeTemp(2, temp)
        temp+=1
        root.update()
"""
    while True:

        # ARDUINO CONNECTION CHECK
        status = findArduino(getPorts())
        if (status == "None"):
            connectionLabel.configure(text='DISCONNECTED ' + status, fg="#ed3b3b")
            g1.setText("Nan", "A0")
            g2.setText("Nan", "A1")
            g3.setText("Nan", "A2")
            g4.setText("Nan", "A3")
            prevCon = False
        elif (not prevCon and status != 'None'):
            try:
                arduinoSwitchbox = serial.Serial(status.split()[0], 115200)
                time.sleep(5)
                connectionLabel.configure(text='CONNECTED ' + status, fg="#41d94d")
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

        data = strSerial.split("\\t")

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
"""




"""
data = [20, 15, 10, 7, 5, 4, 3, 2, 1, 1, 0]

#data= [1,2,3,4,5, 6, 7]

root = tk.Tk()
root.title("Tkinter Bar Graph")
c_width = 600
c_height = 450
c = tk.Canvas(root, width=c_width, height=c_height, bg= 'white')
c.pack()

# the variables below size the bar graph
# experiment with them to fit your needs
# highest y = max_data_value * y_stretch
y_stretch = 1
# gap between lower canvas edge and x axis
y_gap = 20
# stretch enough to get all data items in
x_stretch = 10
x_width = 40
# gap between left canvas edge and y axis
x_gap = 20

vara=0

rectArr=[]
textArr=[]

for x, y in enumerate(data):
    # calculate reactangle coordinates (integers) for each bar
    x0 = x * x_stretch + x * x_width + x_gap
    y0 = c_height - (y * y_stretch + y_gap)
    x1 = x * x_stretch + x * x_width + x_width + x_gap
    y1 = c_height - y_gap
    print("("+str(x0)+", "+str(y0)+")  ("+str(x1)+", "+str(y1)+")")
    # draw the bar
    temp=c.create_rectangle(x0, y0, x1, y1, fill="red")
    rectArr.append(temp)
    # put the y value above each bar
    temp=c.create_text(x0+2, y1+20, anchor=tk.SW, text=str( (c_height-y0-y_gap)/y_stretch  )  )
    textArr.append(temp)


temp=c.create_text(100, 20, anchor=tk.SW, text="testing abcd" )



def update():
    global vara, c
    for i in range(len(rectArr)):
           x=i
           x0, y0, x1, y1 = c.coords(rectArr[i])
           y=vara+1
           x0 = x * x_stretch + x * x_width + x_gap
           y0 = c_height - (y * y_stretch + y_gap)
           x1 = x * x_stretch + x * x_width + x_width + x_gap
           y1 = c_height - y_gap
           c.coords(rectArr[i],x0, y0, x1, y1 )
           c.itemconfig(textArr[i], text=str(y0) )
    vara+=1

    print("("+str(x0)+", "+str(y0)+")  ("+str(x1)+", "+str(y1)+")")
    root.after(1000, update)

vara=0
#update()
#root.mainloop()
"""
