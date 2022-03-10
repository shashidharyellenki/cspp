import threading
import timeit
import random


def cube(nbr):
    return nbr*nbr*nbr

start = timeit.default_timer()
numberProcessList = [100, 1000,10000,100000,1000000]
for processNumber in numberProcessList:
    resultList=[]   
    for i in range(processNumber):
        randomResult = random.randint(0,100)
        thread = threading.Thread(target=cube, args=(randomResult, ))
        resultList.append(thread)
    for t in resultList:
        t.start()
    for t in resultList:
        t.join()

    finish = timeit.default_timer()
    print(f'time consumed for {processNumber} is {round(finish-start)}(s)')