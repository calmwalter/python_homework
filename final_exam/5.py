from tkinter import *
import random

class Optional:
    def __init__(self):
        self.window=Tk()
        self.width=500
        self.height=400
        self.canvas=Canvas(self.window,width=self.width,height=self.height)
        self.canvas.pack()
        self.randomnumber=[]
        self.select=0
        for i in range(20):
            self.randomnumber.append(random.randint(1,20))
        self.r1=self.canvas.create_rectangle(20,self.height-20-self.randomnumber[0]*18,40,self.height-20,fill="red")
        self.r2=self.canvas.create_rectangle(40,self.height-20-self.randomnumber[1]*18,60,self.height-20)
        self.r3=self.canvas.create_rectangle(60,self.height-20-self.randomnumber[2]*18,80,self.height-20)
        self.r4=self.canvas.create_rectangle(80,self.height-20-self.randomnumber[3]*18,100,self.height-20)
        self.r5=self.canvas.create_rectangle(100,self.height-20-self.randomnumber[4]*18,120,self.height-20)
        self.r6=self.canvas.create_rectangle(120,self.height-20-self.randomnumber[5]*18,140,self.height-20)
        self.r7=self.canvas.create_rectangle(140,self.height-20-self.randomnumber[6]*18,160,self.height-20)
        self.r8=self.canvas.create_rectangle(160,self.height-20-self.randomnumber[7]*18,180,self.height-20)
        self.r9=self.canvas.create_rectangle(180,self.height-20-self.randomnumber[8]*18,200,self.height-20)
        self.r10=self.canvas.create_rectangle(200,self.height-20-self.randomnumber[9]*18,220,self.height-20)
        self.r11=self.canvas.create_rectangle(220,self.height-20-self.randomnumber[10]*18,240,self.height-20)
        self.r12=self.canvas.create_rectangle(240,self.height-20-self.randomnumber[11]*18,260,self.height-20)
        self.r13=self.canvas.create_rectangle(260,self.height-20-self.randomnumber[12]*18,280,self.height-20)
        self.r14=self.canvas.create_rectangle(280,self.height-20-self.randomnumber[13]*18,300,self.height-20)
        self.r15=self.canvas.create_rectangle(300,self.height-20-self.randomnumber[14]*18,320,self.height-20)
        self.r16=self.canvas.create_rectangle(320,self.height-20-self.randomnumber[15]*18,340,self.height-20)
        self.r17=self.canvas.create_rectangle(340,self.height-20-self.randomnumber[16]*18,360,self.height-20)
        self.r18=self.canvas.create_rectangle(360,self.height-20-self.randomnumber[17]*18,380,self.height-20)
        self.r19=self.canvas.create_rectangle(380,self.height-20-self.randomnumber[18]*18,400,self.height-20)
        self.r20=self.canvas.create_rectangle(400,self.height-20-self.randomnumber[19]*18,420,self.height-20)
        self.button1=Button(self.window,text="step",command=self.select_sort)
        self.button1.pack(side=LEFT)
        self.button2=Button(self.window,text="reset",command=self.reset)
        self.button2.pack(side=LEFT)
    
        self.window.mainloop()
    def reset(self):
        self.select=0
        self.canvas.delete(self.r1)
        self.canvas.delete(self.r2)
        self.canvas.delete(self.r3)
        self.canvas.delete(self.r4)
        self.canvas.delete(self.r5)
        self.canvas.delete(self.r6)
        self.canvas.delete(self.r7)
        self.canvas.delete(self.r8)
        self.canvas.delete(self.r9)
        self.canvas.delete(self.r10)
        self.canvas.delete(self.r11)
        self.canvas.delete(self.r12)
        self.canvas.delete(self.r13)
        self.canvas.delete(self.r14)
        self.canvas.delete(self.r15)
        self.canvas.delete(self.r16)
        self.canvas.delete(self.r17)
        self.canvas.delete(self.r18)
        self.canvas.delete(self.r19)
        self.canvas.delete(self.r20)
        for i in range(20):
            self.randomnumber[i]=(random.randint(1,20))
        self.r1=self.canvas.create_rectangle(20,self.height-20-self.randomnumber[0]*18,40,self.height-20,fill="red")
        self.r2=self.canvas.create_rectangle(40,self.height-20-self.randomnumber[1]*18,60,self.height-20)
        self.r3=self.canvas.create_rectangle(60,self.height-20-self.randomnumber[2]*18,80,self.height-20)
        self.r4=self.canvas.create_rectangle(80,self.height-20-self.randomnumber[3]*18,100,self.height-20)
        self.r5=self.canvas.create_rectangle(100,self.height-20-self.randomnumber[4]*18,120,self.height-20)
        self.r6=self.canvas.create_rectangle(120,self.height-20-self.randomnumber[5]*18,140,self.height-20)
        self.r7=self.canvas.create_rectangle(140,self.height-20-self.randomnumber[6]*18,160,self.height-20)
        self.r8=self.canvas.create_rectangle(160,self.height-20-self.randomnumber[7]*18,180,self.height-20)
        self.r9=self.canvas.create_rectangle(180,self.height-20-self.randomnumber[8]*18,200,self.height-20)
        self.r10=self.canvas.create_rectangle(200,self.height-20-self.randomnumber[9]*18,220,self.height-20)
        self.r11=self.canvas.create_rectangle(220,self.height-20-self.randomnumber[10]*18,240,self.height-20)
        self.r12=self.canvas.create_rectangle(240,self.height-20-self.randomnumber[11]*18,260,self.height-20)
        self.r13=self.canvas.create_rectangle(260,self.height-20-self.randomnumber[12]*18,280,self.height-20)
        self.r14=self.canvas.create_rectangle(280,self.height-20-self.randomnumber[13]*18,300,self.height-20)
        self.r15=self.canvas.create_rectangle(300,self.height-20-self.randomnumber[14]*18,320,self.height-20)
        self.r16=self.canvas.create_rectangle(320,self.height-20-self.randomnumber[15]*18,340,self.height-20)
        self.r17=self.canvas.create_rectangle(340,self.height-20-self.randomnumber[16]*18,360,self.height-20)
        self.r18=self.canvas.create_rectangle(360,self.height-20-self.randomnumber[17]*18,380,self.height-20)
        self.r19=self.canvas.create_rectangle(380,self.height-20-self.randomnumber[18]*18,400,self.height-20)
        self.r20=self.canvas.create_rectangle(400,self.height-20-self.randomnumber[19]*18,420,self.height-20)
    def select_sort(self):
        minselect=self.select
        minnumber=20000
        for i in range(self.select,len(self.randomnumber)):
            if self.randomnumber[i]<minnumber:
                minnumber=self.randomnumber[i]
                minselect=i
        #exchange number
        tmp=self.randomnumber[self.select]
        self.randomnumber[self.select]=minnumber
        self.randomnumber[minselect]=tmp
        self.select+=1
        print(self.randomnumber)
        self.build()
    def build(self):
        self.canvas.delete(self.r1)
        self.canvas.delete(self.r2)
        self.canvas.delete(self.r3)
        self.canvas.delete(self.r4)
        self.canvas.delete(self.r5)
        self.canvas.delete(self.r6)
        self.canvas.delete(self.r7)
        self.canvas.delete(self.r8)
        self.canvas.delete(self.r9)
        self.canvas.delete(self.r10)
        self.canvas.delete(self.r11)
        self.canvas.delete(self.r12)
        self.canvas.delete(self.r13)
        self.canvas.delete(self.r14)
        self.canvas.delete(self.r15)
        self.canvas.delete(self.r16)
        self.canvas.delete(self.r17)
        self.canvas.delete(self.r18)
        self.canvas.delete(self.r19)
        self.canvas.delete(self.r20)
        self.r1=self.canvas.create_rectangle(20,self.height-20-self.randomnumber[0]*18,40,self.height-20)
        self.r2=self.canvas.create_rectangle(40,self.height-20-self.randomnumber[1]*18,60,self.height-20)
        self.r3=self.canvas.create_rectangle(60,self.height-20-self.randomnumber[2]*18,80,self.height-20)
        self.r4=self.canvas.create_rectangle(80,self.height-20-self.randomnumber[3]*18,100,self.height-20)
        self.r5=self.canvas.create_rectangle(100,self.height-20-self.randomnumber[4]*18,120,self.height-20)
        self.r6=self.canvas.create_rectangle(120,self.height-20-self.randomnumber[5]*18,140,self.height-20)
        self.r7=self.canvas.create_rectangle(140,self.height-20-self.randomnumber[6]*18,160,self.height-20)
        self.r8=self.canvas.create_rectangle(160,self.height-20-self.randomnumber[7]*18,180,self.height-20)
        self.r9=self.canvas.create_rectangle(180,self.height-20-self.randomnumber[8]*18,200,self.height-20)
        self.r10=self.canvas.create_rectangle(200,self.height-20-self.randomnumber[9]*18,220,self.height-20)
        self.r11=self.canvas.create_rectangle(220,self.height-20-self.randomnumber[10]*18,240,self.height-20)
        self.r12=self.canvas.create_rectangle(240,self.height-20-self.randomnumber[11]*18,260,self.height-20)
        self.r13=self.canvas.create_rectangle(260,self.height-20-self.randomnumber[12]*18,280,self.height-20)
        self.r14=self.canvas.create_rectangle(280,self.height-20-self.randomnumber[13]*18,300,self.height-20)
        self.r15=self.canvas.create_rectangle(300,self.height-20-self.randomnumber[14]*18,320,self.height-20)
        self.r16=self.canvas.create_rectangle(320,self.height-20-self.randomnumber[15]*18,340,self.height-20)
        self.r17=self.canvas.create_rectangle(340,self.height-20-self.randomnumber[16]*18,360,self.height-20)
        self.r18=self.canvas.create_rectangle(360,self.height-20-self.randomnumber[17]*18,380,self.height-20)
        self.r19=self.canvas.create_rectangle(380,self.height-20-self.randomnumber[18]*18,400,self.height-20)
        self.r20=self.canvas.create_rectangle(400,self.height-20-self.randomnumber[19]*18,420,self.height-20)
        if self.select==0:
            self.canvas.delete(self.r1)
            self.r1=self.canvas.create_rectangle(20,self.height-20-self.randomnumber[0]*18,40,self.height-20,fill="red")
        if self.select==1:
            self.canvas.delete(self.r2)
            self.r2=self.canvas.create_rectangle(40,self.height-20-self.randomnumber[1]*18,60,self.height-20,fill="red")
        if self.select==2:
            self.canvas.delete(self.r3)
            self.r3=self.canvas.create_rectangle(60,self.height-20-self.randomnumber[2]*18,80,self.height-20,fill="red")
        if self.select==3:
            self.canvas.delete(self.r4)
            self.r4=self.canvas.create_rectangle(80,self.height-20-self.randomnumber[3]*18,100,self.height-20,fill="red")
        if self.select==4:
            self.canvas.delete(self.r5)
            self.r5=self.canvas.create_rectangle(100,self.height-20-self.randomnumber[4]*18,120,self.height-20,fill="red")
        if self.select==5:
            self.canvas.delete(self.r6)
            self.r6=self.canvas.create_rectangle(120,self.height-20-self.randomnumber[5]*18,140,self.height-20,fill="red")
        if self.select==6:
            self.canvas.delete(self.r7)
            self.r7=self.canvas.create_rectangle(140,self.height-20-self.randomnumber[6]*18,160,self.height-20,fill="red")
        if self.select==7:
            self.canvas.delete(self.r8)
            self.r8=self.canvas.create_rectangle(160,self.height-20-self.randomnumber[7]*18,180,self.height-20,fill="red")
        if self.select==8:
            self.canvas.delete(self.r9)
            self.r9=self.canvas.create_rectangle(180,self.height-20-self.randomnumber[8]*18,200,self.height-20,fill="red")
        if self.select==9:
            self.canvas.delete(self.r10)
            self.r10=self.canvas.create_rectangle(200,self.height-20-self.randomnumber[9]*18,220,self.height-20,fill="red")
        if self.select==10:
            self.canvas.delete(self.r11)
            self.r11=self.canvas.create_rectangle(220,self.height-20-self.randomnumber[10]*18,240,self.height-20,fill="red")
        if self.select==11:
            self.canvas.delete(self.r12)
            self.r12=self.canvas.create_rectangle(240,self.height-20-self.randomnumber[11]*18,260,self.height-20,fill="red")
        if self.select==12:
            self.canvas.delete(self.r13)
            self.r13=self.canvas.create_rectangle(260,self.height-20-self.randomnumber[12]*18,280,self.height-20,fill="red")
        if self.select==13:
            self.canvas.delete(self.r14)
            self.r14=self.canvas.create_rectangle(280,self.height-20-self.randomnumber[13]*18,300,self.height-20,fill="red")
        if self.select==14:
            self.canvas.delete(self.r15)
            self.r15=self.canvas.create_rectangle(300,self.height-20-self.randomnumber[14]*18,320,self.height-20,fill="red")
        if self.select==15:
            self.canvas.delete(self.r16)
            self.r16=self.canvas.create_rectangle(320,self.height-20-self.randomnumber[15]*18,340,self.height-20,fill="red")
        if self.select==16:
            self.canvas.delete(self.r17)
            self.r17=self.canvas.create_rectangle(340,self.height-20-self.randomnumber[16]*18,360,self.height-20,fill="red")
        if self.select==17:
            self.canvas.delete(self.r18)
            self.r18=self.canvas.create_rectangle(360,self.height-20-self.randomnumber[17]*18,380,self.height-20,fill="red")
        if self.select==18:
            self.canvas.delete(self.r19)
            self.r19=self.canvas.create_rectangle(380,self.height-20-self.randomnumber[18]*18,400,self.height-20,fill="red")
        if self.select==19:
            self.canvas.delete(self.r20)
            self.r20=self.canvas.create_rectangle(400,self.height-20-self.randomnumber[19]*18,420,self.height-20,fill="red")


Optional()
