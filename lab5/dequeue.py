class deque:
    def __init__(self):
        self.items=[]
        self.largestSize=0
    def addLeft(self,item):
        if len(self.items)<self.largestSize:
            self.items.insert(0,item)
    def addRight(self,item):
        if len(self.items)<self.largestSize:
            self.items.append(item)
    def popLeft(self):
        if len(self.items)>0:
            self.items.pop(0)
    def popRight(self):
        if len(self.items)>0:
            self.items.pop()
    def modeifySize(self,size):
        if self.largestSize>size:
            for i in range(self.largestSize-size):
                self.popRight()
        self.largestSize=size
    def displayNumber(self):
        return len(self.items)
    def clearQueue(self):
        self.items=[]
    def isEmpty(self):
        return len(self.items)==0
