#!/usr/bin/python

# S Lewandowski
# Dec 2017

try:
    from tkinter import *
except ImportError:
    from Tkinter import *

def gantihal(frame):
    frame.tkraise()

#roto frame
root = Tk()
root.title("Chair")
root.geometry('500x300')
root.attributes("-fullscreen", True)

#frames
f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)
f5 = Frame(root)
for frame in (f1, f2, f3, f4, f5):
    frame.grid(row=1, column=1, sticky='news')


#frame 1 test OK
#Button(f1, text='OK', bg='green',width=50,height=15,
#       command=lambda:gantihal(f2)).pack(fill="none", expand=True)

#frame 1
btn = Button(f1, text='OK', bg='green', font="Courier 30",command=lambda:gantihal(f2))
btn.pack(expand=1,fill=BOTH)

#frame 2
btn0 = Button(f2,text='--->   NEXT   --->',font="Courier 20",bg='grey',command=lambda:gantihal(f3))
btn1 = Button(f2,text='1',font="Courier 20",activebackground='blue')
btn2 = Button(f2,text='2',font="Courier 20",activebackground='green')
btn3 = Button(f2,text='3',font="Courier 20",activebackground='red')
btn4 = Button(f2,text='4',font="Courier 20",activebackground='yellow')

f2.rowconfigure((0,1,2),weight=1)
f2.columnconfigure((0,1),weight=1)

btn0.grid(row=0, column=0, columnspan=2, sticky='EWNS')
btn1.grid(row=1, column=0, columnspan=1, sticky='EWNS')
btn2.grid(row=1, column=1, columnspan=1, sticky='EWNS')
btn3.grid(row=2, column=0, columnspan=1, sticky='EWNS')
btn4.grid(row=2, column=1, columnspan=1, sticky='EWNS')

#frame 3
btnP = Button(f3, text='Prev',width=9,height=2,font="Courier 20",
              bg='grey',command=lambda:gantihal(f2))
btnN = Button(f3, text='Next',width=9,height=2,font="Courier 20",
              bg='grey',command=lambda:gantihal(f4))
num=IntVar()
num.set(1)
let=StringVar()
let.set('A')
textNum = Label(f3, text=num.get(), textvariable=num, font="Courier 30")
textLet = Label(f3, text=let, textvariable=let, font="Courier 30")

up=PhotoImage(file="up.png")
up=up.subsample(5)
down=PhotoImage(file="down.png")
down=down.subsample(5)
def nuClick():
    global num
    num.set(num.get()+1)
def ndClick():
    global num
    num.set(num.get()-1)
def luClick():
    global let
    code=ord(let.get())
    let.set(chr(code+1))
def ldClick():
    global let
    code=ord(let.get())
    let.set(chr(code-1))
btnNup = Button(f3,image=up,width=230,command=nuClick)
btnNdown = Button(f3,image=down,width=230,command=ndClick)
btnAup = Button(f3,image=up,width=230,command=luClick)
btnAdown = Button(f3,image=down,width=230,command=ldClick)

f3.rowconfigure((0,1,2,3),weight=1)
f3.columnconfigure((0,1),weight=1)

btnP.grid(row=0, column=0, rowspan=1,columnspan=1)
btnN.grid(row=0, column=1, rowspan=1,columnspan=1)
textNum.grid(row=1, column=0)
textLet.grid(row=1, column=1)
btnNup.grid(row=2, column=0,columnspan=1)
btnAup.grid(row=2, column=1,columnspan=1)
btnNdown.grid(row=3, column=0)
btnAdown.grid(row=3, column=1)

#frame 4
btnP2 = Button(f4, text='Prev',font="Courier 20",width=8,height=2,bg='grey',command=lambda:gantihal(f3))
btnN2 = Button(f4, text='Next',font="Courier 20",width=8,height=2,bg='grey',command=lambda:gantihal(f5))
btnS = Button(f4, text='Save',font="Courier 20",width=10,height=2,bg='grey',)
var1=BooleanVar()
var2=BooleanVar()
var3=BooleanVar()
var4=BooleanVar()
var1.set(False)
var2.set(False)
var3.set(False)
var4.set(False)
ch1 = Checkbutton(f4,text="One",variable=var1,onvalue=True)
ch2 = Checkbutton(f4,text="Two",variable=var2,onvalue=True)
ch3 = Checkbutton(f4,text="Three",variable=var3,onvalue=True)
ch4 = Checkbutton(f4,text="Four",variable=var4,onvalue=True)

f4.rowconfigure((0,1,2,3),weight=1)
f4.columnconfigure((0,1),weight=1)

btnP2.grid(row=0, column=0, rowspan=1,columnspan=1)
btnN2.grid(row=0, column=1, rowspan=1,columnspan=1)
ch1.grid(row=1, column=0)
ch2.grid(row=1, column=1)
ch3.grid(row=2, column=0)
ch4.grid(row=2, column=1)
btnS.grid(row=3, column=0, columnspan=2)

#frame 5
def quit(root):
    root.destroy()
#Label(f5, text='Last frame').pack()
Button(f5, text='Back to start',bg='grey', height=5,
       font="Courier 20",width=15,command=lambda:gantihal(f1)).pack()
Button(f5,text='Quit',bg='red',height=4,width=15,
       font="Courier 20",command=lambda root=root:quit(root)).pack()

gantihal(f1)
root.mainloop()
