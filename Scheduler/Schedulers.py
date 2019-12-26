'''
P.S.:
    * Processing time step = 1
    * Processing time steps are integers (e.g. 1,2,3,10,35)
    * processes: is a list of processes [id, arrival, burst, priority]
    * Consider the context switching time
'''

import numpy as np
from queue import PriorityQueue
import matplotlib.pyplot as plt

def HPF(processes):
    '''
    0 -> Waiting
    1 -> Turnaround
    2 -> Weighted Turnaround
    '''
    processTime = np.zeros((len(processes)+1,3))
    averageTurnaround = 0
    averageWeightedTurnaround = 0
    
    processNum = len(processes)
    ready = PriorityQueue()
    time = 0
    processes.sort(key = lambda process: process[1],reverse = True)
    busy = False
    cur=[]
    plotX = []
    plotY = []
    while(True):
        while(len(processes)>0 and processes[-1][1]==time):
            p = processes.pop()
            '''
            0 -> -ve Priority
            1 -> ID
            2 -> Remaining Time
            3 -> Arrival Time
            4 -> Burst Time
            '''
            ready.put([-p[3],p[0],p[2],p[1],p[2]])
        if(busy == False and (not ready.empty())):
            busy = True
            cur = ready.get()
            
            
        plotX.append(time)
        
        
        if(busy == True):
            cur[2]-=1
            plotY.append(cur[1])
            if(cur[2]==0):
                processTime[cur[1]][1] = time - cur[3]+1 #Turnaround time
                processTime[cur[1]][2] = (processTime[cur[1]][1])/cur[4] #Weighted Turnaround time
                processTime[cur[1]][0] = processTime[cur[1]][1]-cur[4] #Waiting time
                averageTurnaround += processTime[cur[1]][1]
                averageWeightedTurnaround += processTime[cur[1]][2]
                busy = False
        else:
            plotY.append(0)
            
            
        if(busy==False and len(processes)==0 and (ready.empty())):
            break
        time+=1
    averageTurnaround /= processNum
    averageWeightedTurnaround /= processNum
    plotX.append(time+1)
    plotY.append(0)
    plt.fill_between(plotX,plotY,step='post',color='purple')
    plt.title('Highest Priority First')
    plt.xlabel('Time')
    plt.ylabel('Process')
    plt.show()
    return processTime,averageTurnaround,averageWeightedTurnaround


def FCFS(processes):
    '''
    0 -> Waiting
    1 -> Turnaround
    2 -> Weighted Turnaround
    '''
    processTime = np.zeros((len(processes)+1,3))
    averageTurnaround = 0
    averageWeightedTurnaround = 0
    
    processNum = len(processes)
    ready = PriorityQueue()
    time = 0
    processes.sort(key = lambda process: process[1],reverse = True)
    busy = False
    cur=[]
    plotX = []
    plotY = []
    while(True):
        while(len(processes)>0 and processes[-1][1]==time):
            p = processes.pop()
            '''
            0 -> ID
            1 -> Remaining Time
            2 -> Arrival Time
            3 -> Burst Time
            '''
            ready.put([p[0],p[2],p[1],p[2]])
        if(busy == False and (not ready.empty())):
            busy = True
            cur = ready.get()
            
            
        plotX.append(time)
        
        
        if(busy == True):
            cur[1]-=1
            plotY.append(cur[0])
            if(cur[1]==0):
                processTime[cur[0]][1] = time - cur[2]+1 #Turnaround time
                processTime[cur[0]][2] = (processTime[cur[0]][1])/cur[3] #Weighted Turnaround time
                processTime[cur[0]][0] = processTime[cur[0]][1]-cur[3] #Waiting time
                averageTurnaround += processTime[cur[0]][1]
                averageWeightedTurnaround += processTime[cur[0]][2]
                busy = False
        else:
            plotY.append(0)
            
            
        if(busy==False and len(processes)==0 and (ready.empty())):
            break
        time+=1
    averageTurnaround /= processNum
    averageWeightedTurnaround /= processNum
    plotX.append(time+1)
    plotY.append(0)
    plt.fill_between(plotX,plotY,step='post',color='yellow')
    plt.title('First Come First Serve')
    plt.xlabel('Time')
    plt.ylabel('Process')
    plt.show()
    return processTime,averageTurnaround,averageWeightedTurnaround

def RR(processes, contextSwitch=1, quantum=1):
    '''
    0 -> Waiting
    1 -> Turnaround
    2 -> Weighted Turnaround
    '''
    processTime = np.zeros((len(processes)+1,3))
    averageTurnaround = 0
    averageWeightedTurnaround = 0
    
    processNum = len(processes)
    ready = PriorityQueue()
    time = 0
    processes.sort(key = lambda process: process[1],reverse = True)
    busy = False
    cur=[]
    plotX = []
    plotY = []
    while(True):
        while(len(processes)>0 and processes[-1][1]==time):
            p = processes.pop()
            '''
            0 -> Remaining Time
            1 -> ID
            2 -> Arrival Time
            3 -> Burst Time
            4 -> Quantum
            '''
            ready.put([p[2],p[0],p[1],p[2], quantum])
        if(not ready.empty()):
            if(busy==True):
                last = ready.get()
                if(cur[4] == 0):
                    ready.put(cur)
                    cur=last
                    cur[4] = quantum
                    plotX.append(time)
                    plotY.append(1)
                    time+=contextSwitch
                else:
                    ready.put(last)
            else:
                if(not ready.empty()):
                    busy = True
                    cur = ready.get()
                
        plotX.append(time)
        
        if(busy == True):
            cur[0]-=1
            cur[4]-=1
            plotY.append(cur[1]+1)
            if(cur[0]==0):
                processTime[cur[1]][1] = time - cur[2]+1 #Turnaround time
                processTime[cur[1]][2] = (processTime[cur[1]][1])/cur[3] #Weighted Turnaround time
                processTime[cur[1]][0] = processTime[cur[1]][1]-cur[3] #Waiting time
                averageTurnaround += processTime[cur[1]][1]
                averageWeightedTurnaround += processTime[cur[1]][2]
                busy = False
        else:
            plotY.append(0)
            
            
        if(busy==False and len(processes)==0 and (ready.empty())):
            break
        time+=1
    averageTurnaround /= processNum
    averageWeightedTurnaround /= processNum
    plotX.append(time+1)
    plotY.append(0)
    plt.fill_between(plotX,plotY,step='post',color='red')
    plt.title('Round Robin')
    plt.xlabel('Time')
    plt.ylabel('Process')
    plt.show()
    return processTime,averageTurnaround,averageWeightedTurnaround
    
def SRTN(processes,contextSwitch=1):
    '''
    0 -> Waiting
    1 -> Turnaround
    2 -> Weighted Turnaround
    '''
    processTime = np.zeros((len(processes)+1,3))
    averageTurnaround = 0
    averageWeightedTurnaround = 0
    
    processNum = len(processes)
    ready = PriorityQueue()
    time = 0
    processes.sort(key = lambda process: process[1],reverse = True)
    busy = False
    cur=[]
    plotX = []
    plotY = []
    while(True):
        while(len(processes)>0 and processes[-1][1]==time):
            p = processes.pop()
            '''
            0 -> Remaining Time
            1 -> ID
            2 -> Arrival Time
            3 -> Burst Time
            '''
            ready.put([p[2],p[0],p[1],p[2]])
        if(not ready.empty()):
            if(busy==True):
                last = ready.get()
                if(last<cur):
                    ready.put(cur)
                    cur=last
                    plotX.append(time)
                    plotY.append(1)
                    time+=contextSwitch
                else:
                    ready.put(last)
            else:
                if(not ready.empty()):
                    busy = True
                    cur = ready.get()
                
        plotX.append(time)
        
        if(busy == True):
            cur[0]-=1
            plotY.append(cur[1]+1)
            if(cur[0]==0):
                processTime[cur[1]][1] = time - cur[2]+1 #Turnaround time
                processTime[cur[1]][2] = (processTime[cur[1]][1])/cur[3] #Weighted Turnaround time
                processTime[cur[1]][0] = processTime[cur[1]][1]-cur[3] #Waiting time
                averageTurnaround += processTime[cur[1]][1]
                averageWeightedTurnaround += processTime[cur[1]][2]
                busy = False
        else:
            plotY.append(0)
            
            
        if(busy==False and len(processes)==0 and (ready.empty())):
            break
        time+=1
    averageTurnaround /= processNum
    averageWeightedTurnaround /= processNum
    plotX.append(time+1)
    plotY.append(0)
    plt.fill_between(plotX,plotY,step='post',color='brown')
    plt.title('Preemptive Shortest Remaining Time Next')
    plt.xlabel('Time')
    plt.ylabel('Process')
    plt.show()
    return processTime,averageTurnaround,averageWeightedTurnaround
