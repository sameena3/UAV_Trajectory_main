import tkinter
from tkinter import *
import math
import random
from threading import Thread 
from collections import defaultdict
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import time
import random


global mobile, labels, mobile_x, mobile_y, text, canvas, mobile_list, root, num_nodes, tf1, nodes, uav1, uav2, uav3, running
global uav1_x, uav1_y, uav2_x, uav2_y, uav3_x, uav3_y, moving_obj
option = 0
existing_energy = []
propose_energy = []

def getDistance(iot_x,iot_y,x1,y1):
    flag = False
    for i in range(len(iot_x)):
        dist = math.sqrt((iot_x[i] - x1)**2 + (iot_y[i] - y1)**2)
        if dist < 60:
            flag = True
            break
    return flag    
    
def createUAV(x, y, title):
    mobile_x.append(x)
    mobile_y.append(y)
    name = canvas.create_oval(x,y,x+40,y+40, fill="blue")
    lbl = canvas.create_text(x+20,y-10,fill="darkblue",font="Times 7 italic bold",text=title)
    labels.append(lbl)
    mobile.append(name)

def setLocation(x1, y1, x2, y2, x3, y3):
    global uav1_x, uav1_y, uav2_x, uav2_y, uav3_x, uav3_y
    uav1_x = x1
    uav1_y = y1
    uav2_x = x2
    uav2_y = y2
    uav3_x = x3
    uav3_y = y3
    

def moveUAV(uav1_x, uav1_y, uav2_x, uav2_y, uav3_x, uav3_y, mobile, labels, running, canvas):
    global moving_obj
    class MoveUAVThread(Thread):
        def __init__(self, uav1_x, uav1_y, uav2_x, uav2_y, uav3_x, uav3_y, mobile, labels, running, canvas): 
            Thread.__init__(self)
            self.uav1_x = uav1_x
            self.uav1_y = uav1_y
            self.uav2_x = uav2_x
            self.uav2_y = uav2_y
            self.uav3_x = uav3_x
            self.uav3_y = uav3_y
            self.mobile = mobile
            self.labels = labels
            self.running = running
            self.canvas = canvas
            
        def setRunning(self, running):
            self.running = running
            
        def run(self):
            while True:
                #print(self.running)
                if self.running == True:
                    time.sleep(1)
                    if self.uav1_y >= 450 and self.uav1_y <= 600:
                        self.uav1_y = self.uav1_y + 10
                    else:
                        self.uav1_y = 450
                    if self.uav2_y >= 250 and self.uav2_y <= 400:
                        self.uav2_y = self.uav2_y + 10
                    else:
                        self.uav2_y = 250    
                    if self.uav3_y >= 50 and self.uav3_y <= 250:
                        self.uav3_y = self.uav3_y + 10
                    else:
                        self.uav3_y = 50
                    setLocation(5, self.uav1_y, 5, self.uav2_y, 5, self.uav3_y)    
                    #print(str(self.uav1_y)+" "+str(self.uav2_y)+" "+str(self.uav3_y))    
                    self.canvas.delete(self.labels[0])
                    self.canvas.delete(self.labels[1])
                    self.canvas.delete(self.labels[2])
                    self.canvas.delete(self.mobile[0])
                    self.canvas.delete(self.mobile[1])
                    self.canvas.delete(self.mobile[2])
                    self.canvas.update()
                    name = self.canvas.create_oval(self.uav1_x, self.uav1_y, self.uav1_x + 40, self.uav1_y + 40, fill="blue")
                    lbl = self.canvas.create_text(self.uav1_x + 20, self.uav1_y - 10,fill="darkblue",font="Times 8 italic bold",text="UAV1")
                    self.labels[0] = lbl
                    self.mobile[0] = name

                    name = self.canvas.create_oval(self.uav2_x, self.uav2_y, self.uav2_x + 40, self.uav2_y + 40, fill="blue")
                    lbl = self.canvas.create_text(self.uav2_x + 20, self.uav2_y - 10,fill="darkblue",font="Times 8 italic bold",text="UAV2")
                    self.labels[1] = lbl
                    self.mobile[1] = name

                    name = canvas.create_oval(self.uav3_x, self.uav3_y, self.uav3_x + 40, self.uav3_y + 40, fill="blue")
                    lbl = canvas.create_text(self.uav3_x + 20, self.uav3_y - 10,fill="darkblue",font="Times 8 italic bold",text="UAV3")
                    self.labels[2] = lbl
                    self.mobile[2] = name
                    time.sleep(1)
                    self.canvas.update()
                
    moving_obj = MoveUAVThread(uav1_x, uav1_y, uav2_x, uav2_y, uav3_x, uav3_y, mobile, labels, running, canvas) 
    moving_obj.start()    
    

def generateIoT():
    global uav1_x, uav1_y, uav2_x, uav2_y, uav3_x, uav3_y, running, canvas
    global mobile, labels, mobile_x, mobile_y, num_nodes, tf1, nodes, uav1, uav2, uav3
    mobile = []
    mobile_x = []
    mobile_y = []
    labels = []
    nodes = []
    uav1_x = 5
    uav1_y = 650
    uav2_x = 5
    uav2_y = 400
    uav3_x = 5
    uav3_y = 100
    canvas.update()
    num_nodes = int(tf1.get().strip())
    createUAV(5, 450, "UAV1")#450 to 650
    createUAV(5, 250, "UAV2")#250 to 450
    createUAV(5, 50, "UAV3")#50 to 250
    running = True
    for i in range(3,num_nodes):
        run = True
        while run == True:
            x = random.randint(100, 450)
            y = random.randint(50, 600)
            flag = getDistance(mobile_x,mobile_y,x,y)
            if flag == False:
                nodes.append([x, y])
                mobile_x.append(x)
                mobile_y.append(y)
                run = False
                name = canvas.create_oval(x,y,x+40,y+40, fill="red")
                lbl = canvas.create_text(x+20,y-10,fill="darkblue",font="Times 8 italic bold",text="IoT "+str(i))
                labels.append(lbl)
                mobile.append(name)    
    moveUAV(uav1_x, uav1_y, uav2_x, uav2_y, uav3_x, uav3_y, mobile, labels, running, canvas)


def startDataTransferSimulation(moving_obj, canvas,line1,line2,x1,y1,x2,y2,x3,y3):
    class SimulationThread(Thread):
        def __init__(self,moving_obj, canvas,line1,line2,x1,y1,x2,y2,x3,y3): 
            Thread.__init__(self) 
            self.canvas = canvas
            self.line1 = line1
            self.line2 = line2
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2
            self.x3 = x3
            self.y3 = y3
            self.moving_obj = moving_obj
             
        def run(self):
            time.sleep(1)
            for i in range(0,3):
                self.canvas.delete(self.line1)
                self.canvas.delete(self.line2)
                time.sleep(1)
                self.line1 = canvas.create_line(self.x1, self.y1,self.x2, self.y2,fill='black',width=3)
                self.line2 = canvas.create_line(self.x1, self.y1,self.x3, self.y3,fill='black',width=3)                
                time.sleep(1)
            self.canvas.delete(self.line1)
            self.canvas.delete(self.line2)
            self.canvas.update()
            self.moving_obj.setRunning(True)                
    newthread = SimulationThread(moving_obj, canvas,line1,line2,x1,y1,x2,y2,x3,y3) 
    newthread.start()

def taskOffloading():
    text.delete('1.0', END)
    global existing_energy, propose_energy, option, running, canvas, moving_obj
    src = int(mobile_list.get())
    temp = nodes[src]
    src_x = temp[0]
    src_y = temp[1]
    selected_uav1 = 0
    selected_uav1 = 1
    moving_obj.setRunning(False)
    #print(str(uav1_y)+"  === "+str(uav2_y)+" "+str(uav3_y))
    distance1 = math.sqrt((uav1_x - src_x)**2 + (uav1_y - src_y)**2)
    distance2 = math.sqrt((uav2_x - src_x)**2 + (uav2_y - src_y)**2)
    distance3 = math.sqrt((uav3_x - src_x)**2 + (uav3_y - src_y)**2)
    print(str(distance1)+" "+str(distance2)+" "+str(distance3))
    id1 = 0
    id2 = 0
    if distance1 <= distance2 and distance1 <= distance3:
        selected_uav1 = uav1_y
        selected_uav2 = uav2_y
        id1 = 1
        id2 = 2
        existing_energy.append(distance1 * 0.2)
        propose_energy.append((distance1 * 0.2) / 2)
    elif distance2 <= distance1 and distance2 <= distance3:
        id1 = 2
        id2 = 1
        selected_uav1 = uav2_y
        selected_uav2 = uav1_y
        existing_energy.append(distance2 * 0.2)
        propose_energy.append((distance2 * 0.2) / 2)
    else:
        id1 = 3
        id2 = 2
        selected_uav1 = uav3_y
        selected_uav2 = uav2_y
        existing_energy.append(distance3 * 0.2)
        propose_energy.append((distance3 * 0.2) / 2)
    text.insert(END,"Source "+str(src)+" Selected UAV are : "+str(id1)+" & "+str(id2)+"\n\n")
    line1 = canvas.create_line(mobile_x[src]+20, mobile_y[src]+20,25, selected_uav1+20,fill='black',width=3)
    line2 = canvas.create_line(mobile_x[src]+20, mobile_y[src]+20,25, selected_uav2+20,fill='black',width=3)
    startDataTransferSimulation(moving_obj,canvas,line1,line2,(mobile_x[src]+20),(mobile_y[src]+20),25,selected_uav1+20,25,selected_uav2+20)
    option = 1    
    

def graph():
    global existing_energy, propose_energy
    plt.figure(figsize=(10,6))
    plt.grid(True)
    plt.xlabel('Number of Offloads')
    plt.ylabel('Energy Consumption')
    plt.plot(existing_energy, 'ro-', color = 'blue')
    plt.plot(propose_energy, 'ro-', color = 'green')
    plt.legend(['Existing Single Access UAV', 'Propose Multi UAV Access'], loc='upper left')
    plt.title('Energy Consumption Graph')
    plt.show()

def close():
    global root
    root.destroy()

def Main():
    global root, tf1, text, canvas, mobile_list
    root = tkinter.Tk()
    root.geometry("1300x1200")
    root.title("Joint Resource Allocation and Trajectory Optimization for Multi-UAV-Assisted Multi-Access Mobile Edge Computing")
    root.resizable(True,True)
    font1 = ('times', 12, 'bold')

    canvas = Canvas(root, width = 800, height = 700)
    canvas.pack()

    l2 = Label(root, text='Num IoT:')
    l2.config(font=font1)
    l2.place(x=820,y=10)

    tf1 = Entry(root,width=10)
    tf1.config(font=font1)
    tf1.place(x=970,y=10)

    l1 = Label(root, text='IoT ID:')
    l1.config(font=font1)
    l1.place(x=820,y=60)

    mid = []
    for i in range(3,100):
        mid.append(str(i))
    mobile_list = ttk.Combobox(root,values=mid,postcommand=lambda: mobile_list.configure(values=mid))
    mobile_list.place(x=970,y=60)
    mobile_list.current(0)
    mobile_list.config(font=font1)

    createButton = Button(root, text="Generate IoT Network", command=generateIoT)
    createButton.place(x=820,y=110)
    createButton.config(font=font1)
    
    offloadButton = Button(root, text="IoT Task Offloading", command=taskOffloading)
    offloadButton.place(x=820,y=160)
    offloadButton.config(font=font1)

    graphButton = Button(root, text="Energy Graph", command=graph)
    graphButton.place(x=820,y=210)
    graphButton.config(font=font1)

    exitButton = Button(root, text="Exit", command=close)
    exitButton.place(x=820,y=260)
    exitButton.config(font=font1)

    text=Text(root,height=18,width=60)
    scroll=Scrollbar(text)
    text.configure(yscrollcommand=scroll.set)
    text.place(x=820,y=310)    
    
    root.mainloop()
   
 
if __name__== '__main__' :
    Main ()
    
