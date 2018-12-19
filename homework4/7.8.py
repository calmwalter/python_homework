import time
class StopWatch:
    def __init__(self):
        self.__startTime=time.time()
        self.__endTime=time.time()
    def start(self):
        self.__startTime=time.time()
    def end(self):
        self.__endTime=time.time()
    def getStartTime(self):
        return self.__startTime
    def getEndTime(self):
        return self.__endTime
    def getElapsedTime(self):
        return self.__endTime-self.__startTime

sw=StopWatch()
sum=0
sw.start()
for i in range(1000000):
    sum+=i+1
sw.end()
print("%.3f"%sw.getElapsedTime())