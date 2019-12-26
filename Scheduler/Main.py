'''
GUI and preparing the list of the processes will be here
'''

import Schedulers

'''
###For testing purposes###
processHPF = [
    [1, 1, 5, 10],
    [2, 11, 2, 11],
    [3, 1, 3, 5],
]
processSRTN = [
    [1, 7, 1, 10],
    [2, 3, 2, 11],
    [3, 2, 5, 5],
]
processFCFS = [
    [1, 3, 5, 10],
    [2, 11, 2, 11],
    [3, 2, 3, 5],
]
processRR = [
    [1, 7, 1, 10],
    [2, 3, 2, 11],
    [3, 2, 5, 5],
]
'''

###Testing###
'''
SRTNret = Schedulers.SRTN(processSRTN)
print(SRTNret)
FCFSret = Schedulers.FCFS(processFCFS)
print(FCFSret)
RRret = Schedulers.RR(processRR)
print(RRret)
HPFret = Schedulers.HPF(processHPF)
print(HPFret)
'''

print('Enter the file path:')
filePath = input()
processFile = open(filePath,'r')
processList = []
fileList = processFile.readline().split()
fileList = processFile.readline().split()
while(len(fileList)>0):
    tmp = []
    for i in fileList:
        tmp.append(int(i))
    processList.append(tmp)
    fileList = processFile.readline().split()

processFile.close()

print('Enter out file name:')
outName = input()

print('Enter the number of the choosen algorithm:')
print('1. HPF\n2. FCFS\n3. RR\n4. SRTN')
ch = int(input())

contextSwitch=0
quan=1
if(ch>2):
    print('Please specify a context switch:')
    contextSwitch=int(input())
if(ch==3):
    print('Please specify a quantum:')
    quan = int(input())
ret = []
if ch==1:
    ret = HPF(processList)
elif ch==2:
    ret = FCFS(processList)
elif ch==3:
    ret = RR(processList,contextSwitch,quan)
else:
    ret = SRTN(processList,contextSwitch)

processTime,averageTurnaround,averageWeightedTurnaround = ret[0],ret[1],ret[2]

outFile = open(outName,'w')
outFile.write('Number of Processes = ' + str(len(processTime)-1) + '\n')
outFile.write('ID\t\tWaiting\t\tTurnaround\t\tWTurnaround\n')
for i in range(1,len(processTime)):
    outFile.write(str(i)+'\t\t'+str(int(processTime[i][0]))+'\t\t\t'+str(int(processTime[i][1]))+'\t\t\t\t'+str(round(processTime[i][2],2))+'\n')
outFile.write('Average Turnaround = ' + str(averageTurnaround) + '\n')
outFile.write('Average Weighted Turnaround = ' + str(averageWeightedTurnaround) + '\n')
outFile.close()