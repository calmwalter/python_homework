class Array:
    def __init__(self,arr=[]):
        self.elements=arr
    def __mul__(self,a):
        elem=self.elements
        for i in range(len(self.elements)):
            elem[i]*=a
        return Array(elem)
    def __truediv__(self,a):
        elem=self.elements
        for i in range(len(self.elements)):
            elem[i]/=a
        return Array(elem)
    def __add__(self,arr):
        return Array(arr.elements+self.elements)
    def __sub__(self,arr):
        re=[]
        for i in range(len(self.elements)):
            judge=True
            for k in range(len(arr.elements)):
                if self.elements[i]==arr.elements[k]:
                    judge=False
                    break
            if judge:
                re.append(self.elements[i])
                judge=True
        return Array(re)
    def __cmp__(self,arr):
        return self.elements==arr.elements
    def modifyElem(self,v,pos):
        self.elements[pos]=v
