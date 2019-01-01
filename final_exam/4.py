from tkinter import *
import time
class draw:
    def __init__(self):
        self.width = 300
        self.height = 200
        self.canvas = Canvas(root,width = self.width, height = self.height)
        self.canvas.pack()
        root.bind("", self.key)
        self.x = self.width / 2
        self.y = self.height / 2
        self.lineCoord = [150, 10, 100, 100]
        self.pointCoord = [148, 8, 152, 12]
        self.ovalCoord = [90, 90, 110, 110 ]
        self.speed = 2
        self.ovalFlag = 0
    
    def Pendulum(self):

        self.canvas.create_line(self.lineCoord)
        self.canvas.create_oval(self.pointCoord, fill = 'black')
        self.canvas.create_oval(self.ovalCoord, fill = 'black')
        root.update()
        time.sleep(0.1)
        self.canvas.delete('all')

        if(self.ovalCoord[0] >= 145 and self.ovalCoord[1] >= 105 and self.ovalFlag == 0):
            self.ovalFlag = 1
        if(self.ovalCoord[0] >= 205 and self.ovalCoord[1] >= 85 and self.ovalFlag == 1 ):
            self.ovalFlag = 2

        if(self.ovalCoord[0] >= 85 and self.ovalCoord[1] >= 85 and self.ovalFlag == 2):
            self.ovalFlag = 3

        if(self.ovalCoord[0] <= 150 and self.ovalCoord[1] <= 110 and self.ovalFlag ==0) :
            self.ovalCoord[0] += 3 *self.speed
            self.ovalCoord[1] += self.speed
            self.ovalCoord[2] += 3 * self.speed
            self.ovalCoord[3] += self.speed
            print(self.ovalCoord)
            print(self.ovalFlag)
            
        if(self.ovalCoord[0] <= 205 and self.ovalCoord[1] >= 85 and self.ovalFlag == 1):
            self.ovalCoord[0] += 3 * self.speed
            self.ovalCoord[1] -= self.speed
            self.ovalCoord[2] += 3 * self.speed
            self.ovalCoord[3] -= self.speed
            print(self.ovalCoord)
            print(self.ovalFlag)


        if(self.ovalCoord[0] >= 100 and self.ovalCoord[1] <= 105 and self.ovalFlag == 2):
           self.ovalCoord[0] -= 3 * self.speed
           self.ovalCoord[1] += self.speed
           self.ovalCoord[2] -= 3 * self.speed
           self.ovalCoord[3] += self.speed
           print(self.ovalCoord)
           print(self.ovalFlag)



        if(self.ovalCoord[0] >= 85 and self.ovalCoord[1] <= 85 and self.ovalFlag == 3):
           self.ovalCoord[0] -= 3 * self.speed
           self.ovalCoord[1] += self.speed
           self.ovalCoord[2] -= 3 * self.speed
           self.ovalCoord[3] += self.speed   
           print(self.ovalCoord)
           print(self.ovalFlag)


        # else if (ovalCoord[0] < 210 and ovalCoord[1]  )
            


    def key(self,event):
        if event.char == '\uf700':
            self.speed += 1
        
        if event.char == '\uf701':
            self.speed -= 1

        if event.char == '\uf702':
            self.canvas.create_line(self.x, self.y, self.x - self.f, self.y)
            self.x -= self.f

        if event.char == '\uf703':
            self.canvas.create_line(self.x, self.y, self.x + self.f, self.y)
            self.x += self.f

        

root = Tk(className='Pendulum')
a = draw()
while True:
    a.Pendulum()
root.mainloop()
