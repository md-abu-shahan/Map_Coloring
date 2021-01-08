from tkinter import *
from tkinter.font import Font
import time

F_selection =0
O_selection =0
x = [0]*10
b = [0]*10
r = [0]*10
g = [0]*10

def check():
    F_selection=i.get()
    O_selection=j.get()
    if(F_selection==1 and O_selection==3):
        g = Graph(10)
        graph={}
        graph[1] = [2,4,5]
        graph[2] = [1,3,5,6]
        graph[3] = [2,6]
        graph[4] = [1,5,7,8]
        graph[5] = [1,2,4,6,8,9]
        graph[6] = [2,3,5,9]
        graph[7] = [4,8]
        graph[8] = [4,5,7,9]
        graph[9] = [5,6,8]
        m = 3
        g.graphColouring(m)
  
def reset():
    for i in range(1,10):
        canvas.itemconfig(x[i],fill="white")
        canvas.itemconfig(r[i],fill="red")
        canvas.itemconfig(g[i],fill="green")
        canvas.itemconfig(b[i],fill="blue")
        canvas.update()
    

root = Tk()
root.title("__________Map Coloring__________")
root.geometry("620x550+300+50")

canvas = Canvas(root, width=400, height=400, bg="grey88")
canvas.pack()
canvas.place(x=10, y=70)
root.configure(bg="Pale green")

frame = Frame(root, width=200,height=400,bg="grey88")
frame.pack()
frame.place(x=450, y=120)

frame1 = Frame(root, width=250,height=100)
frame1.pack()
frame1.place(x=80, y=500)

# ...1..1...
x[1]=canvas.create_oval(120, 320, 70, 270, fill="white", outline="black", width=2)
b[1]=canvas.create_oval(95,295,80,280,fill="blue",width=0)
r[1]=canvas.create_oval(110,295,95,280,fill="red",width=0)
g[1]=canvas.create_oval(103,310,88,295,fill="green",width=0)
# ...1..2...
x[2]=canvas.create_oval(220, 320, 170, 270, fill="white", outline="black", width=2)
b[2]=canvas.create_oval(195,295,180,280,fill="blue",width=0)
r[2]=canvas.create_oval(210,295,195,280,fill="red",width=0)
g[2]=canvas.create_oval(203,310,188,295,fill="green",width=0)

# ...1..3...
x[3]=canvas.create_oval(320, 320, 270, 270, fill="white", outline="black", width=2)
b[3]=canvas.create_oval(295,295,280,280,fill="blue",width=0)
r[3]=canvas.create_oval(310,295,295,280,fill="red",width=0)
g[3]=canvas.create_oval(303,310,288,295,fill="green",width=0)

# ...2..1...
x[4]=canvas.create_oval(120, 220, 70, 170, fill="white", outline="black", width=2)
b[4]=canvas.create_oval(95,195,80,180,fill="blue",width=0)
r[4]=canvas.create_oval(110,195,95,180,fill="red",width=0)
g[4]=canvas.create_oval(103,210,88,195,fill="green",width=0)
# ...2..2...
x[5]=canvas.create_oval(220, 220, 170, 170, fill="white", outline="black", width=2)
b[5]=canvas.create_oval(195,195,180,180,fill="blue",width=0)
r[5]=canvas.create_oval(210,195,195,180,fill="red",width=0)
g[5]=canvas.create_oval(203,210,188,195,fill="green",width=0)

# ...2..3...
x[6]=canvas.create_oval(320, 220, 270, 170, fill="white", outline="black", width=2)
b[6]=canvas.create_oval(295,195,280,180,fill="blue",width=0)
r[6]=canvas.create_oval(310,195,295,180,fill="red",width=0)
g[6]=canvas.create_oval(303,210,288,195,fill="green",width=0)

# ...3..1...
x[7]=canvas.create_oval(120, 120, 70, 70, fill="white", outline="black", width=2)
b[7]=canvas.create_oval(95,95,80,80,fill="blue",width=0)
r[7]=canvas.create_oval(110,95,95,80,fill="red",width=0)
g[7]=canvas.create_oval(103,110,88,95,fill="green",width=0)
# ...3..2...
x[8]=canvas.create_oval(220, 120, 170, 70, fill="white", outline="black", width=2)
b[8]=canvas.create_oval(195,95,180,80,fill="blue",width=0)
r[8]=canvas.create_oval(210,95,195,80,fill="red",width=0)
g[8]=canvas.create_oval(203,110,188,95,fill="green",width=0)
# ...3..3...
x[9]=canvas.create_oval(320, 120, 270, 70, fill="white", outline="black", width=2)
b[9]=canvas.create_oval(295,95,280,80,fill="blue",width=0)
r[9]=canvas.create_oval(310,95,295,80,fill="red",width=0)
g[9]=canvas.create_oval(303,110,288,95,fill="green",width=0)


# 1st
canvas.create_line(120, 95, 170, 95, fill="black", width=2)
canvas.create_line(220, 95, 270, 95, fill="black", width=2)
# 2nd
canvas.create_line(120, 195, 170, 195, fill="black", width=2)
canvas.create_line(220, 195, 270, 195, fill="black", width=2)
# 3rd
canvas.create_line(120, 295, 170, 295, fill="black", width=2)
canvas.create_line(220, 295, 270, 295, fill="black", width=2)

# 11st...colum.....line.....
canvas.create_line(95, 120, 95, 170, fill="black", width=2)
canvas.create_line(95, 220, 95, 270, fill="black", width=2)
# 22nd
canvas.create_line(195, 120, 195, 170, fill="black", width=2)
canvas.create_line(195, 220, 195, 270, fill="black", width=2)
# 33rd
canvas.create_line(295, 120, 295, 170, fill="black", width=2)
canvas.create_line(295, 220, 295, 270, fill="black", width=2)

# 111st.....digonal.......LINE...........
canvas.create_line(180, 115, 115, 180, fill="black", width=2)
canvas.create_line(280, 115, 215, 180, fill="black", width=2)
##222nd
canvas.create_line(180, 215, 115, 280, fill="black", width=2)
canvas.create_line(280, 215, 215, 280, fill="black", width=2)

b1=Button(frame1,text="reset",bg="cadetblue1",height=1,width=5,command=reset)
b2=Button(frame1,text="Next",bg="plum1",height=1,width=5)
b3=Button(frame1,text="Stop",bg="salmon2",height=1,width=5)
b4=Button(frame1,text="Play",bg="red",height=1,width=5,command=check)
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
b4.pack(side=LEFT)

f1 = Font(family="Times New Romad", size=12, weight="bold",underline=1)  
f2 = Font(family="Times New Romad", size=12, weight="bold") 
Label(root, text="MAP COLORING", fg="black",bg="Pale green",font=Font(family="Algerian", size=20,underline=1)).pack(side=TOP)

title = Label(frame, text="Algo: Backtracking", fg="purple",bg="grey88", font=f1)
title.pack(side=TOP)
i = IntVar()

title1 = Label(frame, text="Filtering:", fg="cyan",bg="grey",font=f2).pack(side=TOP)
r1 = Radiobutton(frame, text="None", fg="black",bg="grey88", value=1, variable=i).pack(side=TOP,anchor=W)
r2 = Radiobutton(frame, text="ForwardChecking", fg="black",bg="grey88", value=2, variable=i).pack(side=TOP,anchor=W )
i.set(1)

j = IntVar()
title2 = Label(frame, text="Ordering:", fg="cyan",bg="grey", font=f2).pack(side=TOP)
r3 = Radiobutton(frame, text="None", fg="black",bg="grey88", value=3, variable=j).pack(side=TOP,anchor=W )
r4 = Radiobutton(frame, text="MRV",fg="black",bg="grey88", value=4, variable=j).pack(side=TOP,anchor=W )
r5 = Radiobutton(frame, text="MRVwithDegree",fg="black",bg="grey88", value=5, variable=j).pack(side=TOP,anchor=W )
j.set(3)



# problem using backtracking
class Graph():
   
    def __init__(self, vertices):
        self.V = vertices
    # is safe for vertex v
    def isSafe(self, v, colour, c):
        for i in graph.get(v):
            if colour[i] == c:
                return False
        return True

    # A recursive utility function to solve m
    def graphColourUtil(self, m, colour, v):
        if v == self.V:
            return True

        for c in range(1, m + 1):
            if self.isSafe(v, colour, c) == True:
                colour[v] = c
                if c==1:
                    st="red"
                elif c==2:
                    st="green"
                elif c==3:
                    st="blue"
                #print (x[v+1],v)

                time.sleep(.5)
                canvas.itemconfig(x[v+1],fill=st)
                canvas.itemconfig(r[v+1],fill=st)
                canvas.itemconfig(g[v+1],fill=st)
                canvas.itemconfig(b[v+1],fill=st)
                canvas.update()
                if self.graphColourUtil(m, colour, v + 1) == True:
                    return True
                time.sleep(.5)
                canvas.itemconfig(x[v+1],fill="white")
                canvas.itemconfig(r[v+1],fill="red")
                canvas.itemconfig(g[v+1],fill="green")
                canvas.itemconfig(b[v+1],fill="blue")
                canvas.update()
                colour[v]=0

    def graphColouring(self, m):
        colour = [0] * self.V
        if self.graphColourUtil(m, colour, 1) == None:
            return False
'''
        # Print the solution
        print("Solution exist and Following are the assigned colours:")
        for c in colour:
            print(c)
        return True'''

root.mainloop()