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


def checkVS( arr1, arr2):
    if (len(arr1) != len(arr2)):
        print("Amount of Valves are unexpected")

    for indx, val in enumerate(arr1):
        if val != arr2[indx]:
            return False

    return True
class LineGraph:
    def __init__(self, root, count=2, datapoints=100, floor=-100, ceiling=100, mving_avg_Size=10, valves=5):
        #root= TK object which LineGraph will be placed onto
        #count= number of TC's which will be displayed
        #datapoints = number of temperature data points to be represented in single instance of the graph

        self.datapoints=datapoints
        TC_Names = ["HE", "LNG", "LOX", "TC4", "TC5", "TC6"]
        colors=['r', 'b', 'c', 'g', 'm', 'y']
        if count>=6:
            self.activeLines=6
        else:
            #save number of lines which will be active in the graph
            self.activeLines=count

        self.xList = collections.deque([i for i in range(datapoints) ])
        #holds y-axis datapoints for all lines
        self.yCoords=[None]*self.activeLines
        for i in range(self.activeLines):
            self.yCoords[i]= collections.deque(np.zeros(datapoints))

        #will hold a number of points, used for calculating moving average
        self.mvAvg=[]
        for i in range(self.activeLines):
            self.mvAvg.append(collections.deque(np.zeros(mving_avg_Size)))
       # self.mvAvg = [collections.deque(np.zeros(mving_avg_Size))] * self.activeLines

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
        #redisplays readings next to the legend in the top right corner
        self.static_annotations=[ self.ax1.annotate(str(i), xy=(datapoints*1.05, ceiling/2 +18 -(6*i) ), textcoords='data') for i in range(self.activeLines) ]

        self.valve_annotations=[]# self.ax1.annotate(str(i), xy=(datapoints*1.05, ceiling/2 +18 -(6*i) ), textcoords='data') for i in range(2) ]
        self.valve_annotations.append(self.ax1.annotate("Time since Last Actuation: %s" % "N/A", xy=(self.datapoints/3, -10), textcoords='data'))
        self.valve_annotations.append(self.ax1.annotate("Time since Last Random   : %s" % "N/A", xy=(self.datapoints/3, -17), textcoords='data'))



        for i in range(self.activeLines):
            self.lineControl[i], =self.ax1.plot(self.xList, [(-1-i)]*datapoints, colors[i], label=TC_Names[i])

        self.ax1.plot(self.xList, [0]*datapoints, "w")


        leg = plt.legend(loc='upper right')
        print(type(self.lineControl[0]))

        self.plotcanvas = FigureCanvasTkAgg(self.fig, root)
        print(type(self.plotcanvas))
        self.plotcanvas.get_tk_widget().grid(column=1, row=1)

        #init variable for valve checking
        self.valveCount=valves
        self.timeLastData=0 #timestamp of current data point
        self.timeLastValve=0 #timestamp any valve last actuated
        self.timeLastRandom=0 #timestamp of last random actuatuation
        self.prevValve1 = np.zeros(self.valveCount) #last valve state recorded
        self.prevValve2 = np.zeros(self.valveCount) #2nd to last valve state recorded
        self.ttt=0
        self.firstValve=False
        self.firstRand=False






    def getWidget(self):
        return self.plotcanvas
    def getFig(self):
        return self.fig
    def animate(self, i):

        #TODO apply animate to all lines in class
        #print("active lines ="+str(self.activeLines))

        for i in range(self.activeLines):
            self.lineControl[i].set_data(self.xList, self.yCoords[i])

        for j in range(self.activeLines):
            self.annotations[j].set_y(self.yCoords[j][-1])
            self.annotations[j].set_text(self.yCoords[j][-1])
            self.static_annotations[j].set_text(self.yCoords[j][-1])





#Nextpts functions will take inividual points and add them to the yCoords
#nextPts take in a point for each line
#nextPoint takes a single datapoint and the index to insert it into

    def nextPts(self, data):
        #this function is not implemented - meant to be a wrapper where we can send an array of datapoints in 1 function call, rather than call nextPoint() for each line

        #if data list is empty, will not append anything otherwise append to end of yList and pop the oldest data point
        #TODO- confirm new data from serial is being pushed and there is not a delay building in the dataList as more time goes on
            if not data:
                return

    def nextPoint(self, data, index):
        #if data list is empty, will not append anything otherwise append to end of yList and pop the oldest data point
            if not data:
                return

            self.mvAvg[index].popleft()
            self.mvAvg[index].append(float(data))
            avg=sum(self.mvAvg[index])/len(self.mvAvg[index])

            self.yCoords[index].popleft()
            self.yCoords[index].append(avg)
            print("mvAvg "+str(index)+"="+str(avg))

# valve Check functions
    def valveCheck(self, valveStates):
        #function expects a valveStates Array of binary values representing state of the valves`
        # function will check if any valves have changed state since last call
        # self.ttt+=1
        # # if(self.ttt%10==0):
        # #     valveStates[0]=1
        # if(self.ttt>40):
        #     valveStates[0]=1
        # if(self.ttt>100):
        #     self.ttt=0


        currValve=np.array(valveStates)

        self.timeLastData = time.time()
        if(len(currValve)!=self.valveCount):
            print("value Count is not matching number of valves provided")
            print(len(currValve))
            print("!=")
            print(self.valveCount)


       # if(currValve==self.prevValve1): # no change
        if checkVS(currValve, self.prevValve1):
            self.prevValve2=self.prevValve1
            t1= self.timeLastData-self.timeLastValve
        else:
            self.firstValve=True
            #valve has actuated
            t1=0
            self.timeLastValve = self.timeLastData

            #check if current valve state is equal to the valve state 2 cycles ago, if it is this might indicate that a random actuation occured and rapidly flipped back
            #NOTE: this is a very specific case of random actuation, assuming a random actuation occurs in a single data point and will revert back to its correct state at the next data point. Random actuations lasting longer than this will not be detected
            # trust the general actuation detection over the random actuation detection as the sign for a random actuataion within a data stream is not known for sure
            #if(currValve==self.prevValve2):
            if checkVS(currValve, self.prevValve2):
                self.firstRand=True
                self.timeLastRandom = time.time()

            self.prevValve2 = self.prevValve1
            self.prevValve1 = currValve

        #draw time since last change
        if (self.firstValve):
            self.valve_annotations[0].set_text("Time since Last Actuation: %s" % t1)
        if(self.firstRand):
            self.valve_annotations[1].set_text("Time since Last Random   : %s" % (self.timeLastData-self.timeLastRandom))


