# !/usr/bin/env python3


#UNCOMMENT IF TESTING
'''import tkinter as tk
import time
import math
import random'''
import tkinter as tk
# the variables below size the bar graph
# experiment with them to fit your needs
# highest y = max_data_value * y_stretch
y_stretch = 0.4
# gap between lower canvas edge and x axis
y_gap = 15
# stretch enough to get all data items in
x_stretch = 10
x_width = 40
# gap between left canvas edge and y axis
x_gap = 20


class BarDisplay:

    def __init__(self, root, background, max, TC_Count):
        self.max = max
        wVar=400
        hVar=250
        self.c = tk.Canvas(root, width=wVar, height=hVar, bg=background, highlightthickness=0)
        self.data= [500]* TC_Count#, 7, 5, 4, 3, 2, 1, 1, 0]
        self.rectArr=[]
        self.textArr=[]
        self.c_width=wVar
        self.c_height=hVar

        size = 180
        for x, y in enumerate(self.data):
            # calculate reactangle coordinates (integers) for each bar
            x0 = x * x_stretch + x * x_width + x_gap
            y0 = self.c_height - (y * y_stretch + y_gap)
            x1 = x * x_stretch + x * x_width + x_width + x_gap
            y1 = self.c_height - y_gap
            #print("("+str(x0)+", "+str(y0)+")  ("+str(x1)+", "+str(y1)+")")

            # draw the bar
            temp=self.c.create_rectangle(x0, y0, x1, y1, fill="red")
            self.rectArr.append(temp)
            # put the y value above each bar
            print(str( (self.c_height-y0-y_gap)/y_stretch  ))
            temp=self.c.create_text(x0+2, y1+15, anchor=tk.SW, text=str( (self.c_height-y0-y_gap)/y_stretch  )  )

            self.textArr.append(temp)
        #temp=self.c.create_text(300, 250, anchor=tk.SW, text="( Testing Coordinate)" )


    def calculateCoordinate(self, index, value):
        #index - 0 is leftmost Bar
        #value - thermocouple reading

        x0 = index * x_stretch + index * x_width + x_gap
        y0 = self.c_height - (value * y_stretch + y_gap)
        x1 = index * x_stretch + index * x_width + x_width + x_gap
        y1 = self.c_height - y_gap
        return x0, y0, x1, y1


    def getWidget(self):
        return self.c

    def setText(self,index, str):
        self.c.itemconfig(self.textArr[index], text=str)

    def changeTemp(self, index, newVal):
        x0, y0, x1, y1=self.calculateCoordinate(index, newVal)
        self.c.coords(self.rectArr[index],x0, y0, x1, y1)
        self.setText(index, newVal)


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
