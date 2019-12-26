'''
GUI and preparing the list of the processes will be here
'''

import Schedulers


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

###Testing###
SRTNret = Schedulers.SRTN(processSRTN)
print(SRTNret)
FCFSret = Schedulers.FCFS(processFCFS)
print(FCFSret)
RRret = Schedulers.RR(processRR)
print(RRret)
HPFret = Schedulers.HPF(processHPF)
print(HPFret)