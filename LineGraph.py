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

class LineGraph:
    def __init__(self, root, count=2, datapoints=10, floor=-100, ceiling=100):
        #root= TK object which LineGraph will be placed onto
        #count= number of lines which will be


        colors=['r','b','g', 'c', 'm', 'y']
        if count>=6:
            self.activeLines=6
        else:
            #save number of lines which will be active in the graph
            self.activeLines=count


        self.xList = collections.deque([i for i in range(datapoints) ])
        self.yList = collections.deque(np.zeros(datapoints))
        #holds y-axis datapoints for all lines
        self.yCoords=[None]*self.activeLines
        for i in range(self.activeLines):
            #self.yCoords[i]= collections.deque(np.zeros(datapoints))
            self.yCoords[i]= collections.deque([(-1-i)]*datapoints)

            [(-1-i)]*datapoints
        #holds the line objects themselves
        self.lineControl=[None]*self.activeLines

        print(type(self.yCoords[0]))
        #style.use('ggplot')
        #style.use("seaborn-whitegrid")
        self.fig = plt.figure(figsize=(14, 4.5), dpi=100)
        self.ax1 = self.fig.add_subplot(1, 1, 1)
        self.ax1.set_ylim(floor, ceiling)
        self.ax1.set_xlim(0, int(datapoints*1.2))
        self.annotations=[ self.ax1.annotate("(%s)" % 0, xy=(datapoints, 0), textcoords='data') for i in range(self.activeLines) ]


        #
        for i in range(self.activeLines):
            #self.lineControl[i], =ax1.plot(self.xList, [(-1-i)]*datapoints, colors[i], marker='o', label="line1")
            self.lineControl[i], =self.ax1.plot(self.xList, [(-1-i)]*datapoints, colors[i], label="line1")

        self.ax1.plot(self.xList, [0]*datapoints, label="origin")


        leg = plt.legend(loc='upper right')
        print(type(self.lineControl[0]))

        self.plotcanvas = FigureCanvasTkAgg(self.fig, root)
        print(type(self.plotcanvas))
        self.plotcanvas.get_tk_widget().grid(column=1, row=1)

    def getWidget(self):
        return self.plotcanvas
    def getFig(self):
        return self.fig
    def animate(self, i):
        #TODO apply animate to all lines in class
        print(self.activeLines)
        #print(self.yCoords)

        for i in range(self.activeLines):
            self.lineControl[i].set_data(self.xList, self.yCoords[i])
        #for j in range(self.activeLines):
        #self.annotations[0].remove()
        #self.annotations[0]=self.ax1.annotate("(%s)" %self.yCoords[0][-1], xy=(len(self.xList),self.yCoords[0][-1]), textcoords='data' )
        for j in range(self.activeLines):
            self.annotations[j].set_y(self.yCoords[j][-1])
            self.annotations[j].set_text(self.yCoords[j][-1])




#Nextpts functions will take inividual points and add them to the yCoords
#nextPts take in a point for each line
#nextPoint takes a single datapoint and the index to insert it into

    def nextPts(self, data):
        #if data list is empty, will not append anything otherwise append to end of yList and pop the oldest data point

        #TODO- confirm new data from serial is being pushed and there is not a delay building in the dataList as more time goes on
            if not data:
                return
            self.yList.popleft()
            self.yList.append(float(data[0]))
            data.pop(0)
            #data.append(cc%12)
    def nextPoint(self, data, index):
        #if data list is empty, will not append anything otherwise append to end of yList and pop the oldest data point

            if not data:
                return
            self.yCoords[index].popleft()
            self.yCoords[index].append(float(data))
