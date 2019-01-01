from tkinter import *

import random
word=['r','e','c','e','i','v','e']
guess=['*','*','*','*','*','*','*']
class HangMan:
    def __init__(self):
        self.bihua=1
        window = Tk()
        window.title("Hangman")
        self.text = StringVar()
        self.text.set('')

        self.word=StringVar()
        self.word.set(guess)
        # 画布
        self.canvas = Canvas(window, bg="white", width=800, height=500)
        self.canvas.pack()
        # 标签1，隐藏的字
        label1 = Label(window, textvariable=self.word)
        label1.pack()
        # 标签2，输入的字
        label2 = Label(window, textvariable=self.text)
        label2.pack()

        self.canvas.bind("<Key>", self.keyEvent)
        self.canvas.focus_set()
        self.canvas.create_oval(0,450,200,580,tags="oval")
        self.canvas.create_line(100,450,100,20,tags="line1")
        self.canvas.create_line(450,20,100,20,tags="line2")

        window.mainloop()

    def keyEvent(self, event):
        global guess
        a=False
        success=0
        for x in range(7):
            if word[x]==guess[x]:
                success=success+1
            if event.char==word[x]:
                a=True
                guess[x]=event.char
                self.word.set(guess)
        if success==7:
            self.text.set("You have guess the word!\nTo continue the game, press ENTER")
            if event.keycode == 13:
                guess=['*','*','*','*','*','*','*']
                self.text.set('')
                self.word.set(guess)
                self.canvas.delete("line3","line4","line5","line6","line7","line8","circle")
                self.bihua=1
            return

        if self.bihua > 6:
            self.drawline6()
            self.text.set("To continue the game, press ENTER")
            self.word.set('The word is:'.split()+ word)
            if event.keycode == 13:
                guess=['*','*','*','*','*','*','*']
                self.text.set('')
                self.word.set(guess)
                self.canvas.delete("line3","line4","line5","line6","line7","line8","circle")
                self.bihua=1
                
        else:
            
            #print(event.keycode)
            if a==False:
                self.text.set(self.text.get()+event.char)
                l=self.bihua
                if l==1:
                    self.drawline1()
                elif l==2:
                    self.drawcircle()
                elif l==3:
                    self.drawline2()
                elif l==4:
                    self.drawline3()
                elif l==5:
                    self.drawline4()
                elif l==6:
                    self.drawline5()
                self.bihua=self.bihua+1
    def drawline1(self):
        self.canvas.create_line(450,20,450,50,tags="line3")
    def drawcircle(self):
        self.canvas.create_oval(430,50,470,90,tags="circle")
    def drawline2(self):
        self.canvas.create_line(440,87,390,172,tags="line4")
    def drawline3(self):
        self.canvas.create_line(460,87,490,172,tags="line5")
    def drawline4(self):
        self.canvas.create_line(450,90,450,200,tags="line6")
    def drawline5(self):
        self.canvas.create_line(450,200,430,300,tags="line7")
    def drawline6(self):
        self.canvas.create_line(450,200,470,300,tags="line8")     

HangMan()
