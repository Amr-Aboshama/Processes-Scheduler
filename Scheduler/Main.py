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
    [1, 6, 1, 10],
    [2, 2, 2, 11],
    [3, 1, 5, 5],
]

###Testing###
SRTNret = Schedulers.SRTN(processSRTN)
print(SRTNret)
HPFret = Schedulers.HPF(processHPF)
print(HPFret)