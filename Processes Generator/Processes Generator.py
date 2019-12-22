'''
Process Generator Module
'''
import numpy as np

#Read input and split it into a list

print('Enter the input file name: ')
fileIn = input()
print('Enter the output file name: ')
fileOut = input()

distFile = open(fileIn,'r')
dataString = distFile.read().split()
distFile.close()
#Extract data from the input
numProcess = int(dataString[0])
arrivalMean,arrivalSTD = float(dataString[1]),float(dataString[2])
burstMean,burstSTD = float(dataString[3]),float(dataString[4])
priorityLambda = float(dataString[5])

#Open file to write the processes data
outFile = open(fileOut,'w')

#Generate processes data
outFile.write(str(numProcess) + '\n')
for processID in range(0,numProcess):
    arrivalTime = abs(int(np.random.normal(arrivalMean,arrivalSTD)))
    burstTime = abs(int(np.random.normal(burstMean,burstSTD)))
    priority = abs(np.random.poisson(priorityLambda))
    outFile.write(str(processID+1) + '\t' + str(arrivalTime) + '\t' + str(burstTime) + '\t' + str(priority) + '\n')
outFile.close()