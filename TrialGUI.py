# drawing a bar graph with the Tkinter canvas and
# canvas.create_rectangle(x0, y0, x1, y1, option, ...)
# note: coordinates are relative to the top left corner of the canvas
# used a more modern import to give Tkinter items a namespace
# tested with Python24  by    vegaseat    01nov2006

import tkinter as tk  # gives tk namespace
import random

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




def update():
    global vara
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
update()
root.mainloop()
