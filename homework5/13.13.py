from tkinter import *

fileName = input("Enter a filename: ")
openfile=open(fileName,"r")
content=openfile.readline()
l=int(content)
#get the graph
graph=[]
for i in range(l):
    content=openfile.readline()
    ls=content.split()
    graph.append(ls)
openfile.close()
#show tk,for every vertex add the vertex an its edge
window=Tk()
canvas=Canvas(window, height=500, width=600)
canvas.pack(side=LEFT)

for i in range(l):
    x=int(graph[i][1])
    y=int(graph[i][2])
    canvas.create_oval(x-1,y-1,x+1,y+1,fill='black')
    canvas.create_text(x-6,y-6,text=str(i))
    for k in range(len(graph[i])-3):
        x1=int(graph[int(graph[i][k+3])][1])
        y1=int(graph[int(graph[i][k+3])][2])
        canvas.create_line(x,y,x1,y1,fill='black')
mainloop()

