import tkinter as tk
from tkinter import ttk
import math

try:
    from ctypes import windll
    windll.shcore.SetProcessDpAwareness(1)
except:
    pass

answer=''
def button(num):
    global answer
    answer=answer+str(num)
    calans.set(answer)

def equal():
    try:
    #this function is used only for equals
        global answer
        finalanswer=0
        finalanswer = str(eval(answer))
        #this evaluates the final anser
        calans.set(finalanswer)
        # and then it will pack the answer in the storage value
        answer=''
    except:
        calans.set('Error ! enter again')
        answer=''

def clear():
    global answer
    answer=''
    calans.set('')
    

def prime():
    global answer
    c=0
    num=str(eval(answer))
    n=int(num)
    for i in range(2,n+1):
        if n%i==0:
            c=c+1
    if c==1:
        calans.set('It is a prime number')
    else:
        calans.set('Not a prime number')
    answer=''

def sroot():
    global answer
    num=str(eval(answer))
    n=int(num)
    s=math.sqrt(n)
    calans.set(s)
    answer=''

root=tk.Tk()
root.resizable(False,False)
root.columnconfigure(0,weight=1)

theme=ttk.Style(root)#to select themes

print(theme.theme_names()) #to print all the themes in windows or in our system
theme.theme_use('classic') #to use certain theme


root.title('Simple calculator')
fanswer=ttk.Frame(root)
fanswer.grid()

label=ttk.Label(fanswer,text='VARSHITH')
label.config(font=('Algerian',15))
label.grid(row=0,column=0)

calans=tk.StringVar() #storage variable which stores the value which we enter
cal=tk.Entry(fanswer,textvariable=calans,width=30)# this is used to modify the value
cal.grid(row=1,column=0)
calans.set('Enter the number')# to print the default text

fbutton=ttk.Frame(root)
fbutton.grid()
#to display the numbers
b1=tk.Button(fbutton,text='1',command=lambda : button(1),height=2, width=6)
b1.grid(row=1,column=2)
b2=tk.Button(fbutton,text='2',command=lambda : button(2),height=2, width=6)
b2.grid(row=2,column=2)
b3=tk.Button(fbutton,text='3',command=lambda : button(3),height=2, width=6)
b3.grid(row=3,column=2)
b4=tk.Button(fbutton,text='4',command=lambda : button(4),height=2, width=6)
b4.grid(row=1,column=1)
b5=tk.Button(fbutton,text='5',command=lambda : button(5),height=2, width=6)
b5.grid(row=2,column=1)
b6=tk.Button(fbutton,text='6',command=lambda : button(6),height=2, width=6)
b6.grid(row=3,column=1)
b7=tk.Button(fbutton,text='7',command=lambda : button(7),height=2, width=6)
b7.grid(row=1,column=0)
b8=tk.Button(fbutton,text='8',command=lambda : button(8),height=2, width=6)
b8.grid(row=2,column=0)
b9=tk.Button(fbutton,text='9',command=lambda : button(9),height=2, width=6)
b9.grid(row=3,column=0)
b0=tk.Button(fbutton,text='0',command=lambda : button(0),height=2, width=6)
b0.grid(row=4,column=0)
ba=tk.Button(fbutton,text='+',command=lambda : button('+'),height=2, width=6)
ba.grid(row=2,column=3)
bb=tk.Button(fbutton,text='-',command=lambda : button('-'),height=2, width=6)
bb.grid(row=1,column=3)
bc=tk.Button(fbutton,text='*',command=lambda : button('*'),height=2, width=6)
bc.grid(row=3,column=3)
bd=tk.Button(fbutton,text='/',command=lambda : button('/'),height=2, width=6)
bd.grid(row=4,column=3)
bdeci=tk.Button(fbutton,text='.',command=lambda : button('.'),height=2, width=6)
bdeci.grid(row=4,column=1)

bclear=tk.Button(fbutton,text='clear',command=clear,height=2, width=6)
bclear.grid(row=4,column=2)
febutton=ttk.Frame(root)
febutton.grid()
bprime=tk.Button(febutton,text='Check prime',command=prime,height=2, width=13)
bprime.grid(row=5,column=0)
broot=bd=tk.Button(febutton,text='√',command=sroot,height=2, width=13)
bd.grid(row=5,column=1)
bequal=tk.Button(febutton,text='=',command=equal,fg='green',bg='lightblue',height=2, width=13)
bequal.grid(row=6,column=0)
bquit=tk.Button(febutton,text='Exit',command=root.destroy,fg='black',bg='lightblue',height=2, width=13)
bquit.grid(row=6,column=1)
root.mainloop()