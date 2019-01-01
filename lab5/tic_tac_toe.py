from tkinter import *

class ticTacToe:
    def __init__(self):
        self.player=0
        self.palytimes=0
        self.window=Tk()
        self.window.title("tic-tac-toe")

        self.gameover=0
        self.havedraw=[0]*9
        self.empty=PhotoImage(file="empty.gif")
        self.o=PhotoImage(file="o.gif")
        self.x=PhotoImage(file="x.gif")

        self.frame=Frame(self.window)
        self.frame.pack()
        self.canvas=Canvas(self.frame)
        self.canvas["width"]=180
        self.canvas["height"]=180
        self.canvas.pack(side=LEFT)
        self.window.bind("<Button-1>",self.showphoto)
        self.canvas.create_image((40*1,40*1),image=self.empty,tags="empty1")
        self.canvas.create_image((40*2,40*1),image=self.empty,tags="empty2")
        self.canvas.create_image((40*3,40*1),image=self.empty,tags="empty3")
        self.canvas.create_image((40*1,40*2),image=self.empty,tags="empty4")
        self.canvas.create_image((40*2,40*2),image=self.empty,tags="empty5")
        self.canvas.create_image((40*3,40*2),image=self.empty,tags="empty6")
        self.canvas.create_image((40*1,40*3),image=self.empty,tags="empty7")
        self.canvas.create_image((40*2,40*3),image=self.empty,tags="empty8")
        self.canvas.create_image((40*3,40*3),image=self.empty,tags="empty9")

        self.window.mainloop()
    def drawo(self,pos):
        self.canvas.create_image(pos,image=self.o)
    def drawx(self,pos):
        self.canvas.create_image(pos,image=self.x)
    def getpos(self,x,y):
        if x+20>40 and x+20<80 and y+20>40 and y+20<80:
            return (40,40)
        elif x+20>80 and x+20<120 and y+20>40 and y+20<80:
            return (80,40)
        elif x+20>120 and x+20<160 and y+20>40 and y+20<80:
            return (120,40)
        elif x+20>40 and x+20<80 and y+20>80 and y+20<120:
            return (40,80)
        elif x+20>80 and x+20<120 and y+20>80 and y+20<120:
            return (80,80)
        elif x+20>120 and x+20<160 and y+20>80 and y+20<120:
            return (120,80)
        elif x+20>40 and x+20<80 and y+20>120 and y+20<160:
            return (40,120)
        elif x+20>80 and x+20<120 and y+20>120 and y+20<160:
            return (80,120)
        elif x+20>120 and x+20<160 and y+20>120 and y+20<160:
            return (120,120)
        else:
            return (0,0)
    def deleteempty(self,number):
        if number==0:
            self.canvas.delete("empty1")
        if number==1:
            self.canvas.delete("empty2")
        if number==2:
            self.canvas.delete("empty3")
        if number==3:
            self.canvas.delete("empty4")
        if number==4:
            self.canvas.delete("empty5")
        if number==5:
            self.canvas.delete("empty6")
        if number==6:
            self.canvas.delete("empty7")
        if number==7:
            self.canvas.delete("empty8")
        if number==8:
            self.canvas.delete("empty9")
    def showphoto(self,event):
        if self.gameover==1:
            return
        pos=self.getpos(event.x,event.y)
        number=pos[0]//40+3*(pos[1]//40)-4
        if pos!=(0,0) and self.havedraw[number]==0 and self.palytimes<10:
            self.deleteempty(number)
            if self.player==0 : 
                self.drawo(pos)
                self.player=1
                self.havedraw[number]=1
            elif self.player==1:
                self.drawx(pos)
                self.player=0
                self.havedraw[number]=2

            self.palytimes+=1
            win=self.ifsomeonewin()
            if win==1:
                self.canvas.create_text(90,160,text="The O player won the game")
                self.gameover=1
            elif win==2:
                self.canvas.create_text(90,160,text="The X player won the game")
                self.gameover=1
            elif win==0 and self.palytimes==9:
                self.canvas.create_text(90,160,text="Draw--no winners")
                self.gameover=1
    def ifsomeonewin(self):
        for i in range(1,4):
            cnt1=0
            cnt2=0
            for k in range(1,4):
                if self.havedraw[3*i+k-4]==1:
                    cnt1+=1
                elif self.havedraw[i*3+k-4]==2:
                    cnt2+=1
            if cnt1==3:
                return 1
            if cnt2==3:
                return 2

        for i in range(1,4):
            cnt1=0
            cnt2=0
            for k in range(1,4):
                if self.havedraw[i+(k-1)*3-1]==1:
                    cnt1+=1
                elif self.havedraw[i+(k-1)*3-1]==2:
                    cnt2+=1
            if cnt1==3:
                return 1
            if cnt2 ==3:
                return 2
        if self.havedraw[0]==1 and self.havedraw[4]==1 and self.havedraw[8]==1:
            return 1
        elif self.havedraw[2]==1 and self.havedraw[4]==1 and self.havedraw[6]==1:
            return 1
        elif self.havedraw[0]==2 and self.havedraw[4]==2 and self.havedraw[8]==2:
            return 2
        elif self.havedraw[2]==2 and self.havedraw[4]==2 and self.havedraw[6]==2:
            return 2
        return 0
a=ticTacToe()
