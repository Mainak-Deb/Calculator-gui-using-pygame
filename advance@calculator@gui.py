import math
from tkinter import *
wd=Tk()
wd.title("CALCULATOR")
wd.configure(background="cadetblue4")
wd.geometry()
e=Entry(wd,width=62,borderwidth=7,bg="darkslategray",fg="snow")
e.grid(row=2,column=0,columnspan=6)
e2=Entry(wd,width=62,borderwidth=7,bg="royalblue4",fg="snow")
e2.grid(row=1,column=0,columnspan=6)


lb1=Label(wd,text="|| SCREEN ||",padx=202,pady=5,bg="lightsteelblue4").grid(row=0,column=0,columnspan=6)
lb2=Label(wd,text="|| BASICS ||",padx=204,pady=10,bg="lightsteelblue4").grid(row=3,column=0,columnspan=6)
lb3=Label(wd,text="|| ADVANCE ||",padx=196,pady=10,bg="lightsteelblue4").grid(row=8,column=0,columnspan=6)
lb3=Label(wd,text="* DEV *",padx=214,pady=10,bg="lightsteelblue4",fg="red").grid(row=12,column=0,columnspan=6)

#functions
def enter(a):
    ls=e.get()
    e.delete(0,END)
    e.insert(0,str(ls)+str(a))
    ls=e2.get()
    e2.delete(0,END)
    e2.insert(0,str(ls)+str(a))
    
def enter2(a):
    ls=e2.get()
    e2.delete(0,END)
    e2.insert(0,str(ls)+str(a))
    
    
    
def clear_screen():
    e.delete(0,END)
    e2.delete(0,END)

def ev():
    e.delete(0,END)
    lv=2.718281
    e.insert(0,str(2.718281))
    enter2("e")
   
def pi():
    e.delete(0,END)
    lv=3.141592653589793238
    e.insert(0,str(3.141592653589793238))
    enter2("pi")

def plus():
    e2.delete(0,END)
    sv=e.get()
    e2.insert(0,str(sv))
    
    global lv
    global mathoperation
    lv=float(sv)
    mathoperation="+"
    e.delete(0,END)
    enter2("+")
    return
def minus():
    e2.delete(0,END)
    sv=e.get()
    e2.insert(0,str(sv))
    
    global lv
    global mathoperation
    lv=float(sv)
    mathoperation="-"
    e.delete(0,END)
    enter2(" - ")
    
    return

def division():
    e2.delete(0,END)
    
    sv=e.get()
    e2.insert(0,str(sv))
    
    global lv
    global mathoperation
    lv=float(sv)
    mathoperation="/"
    e.delete(0,END)
    enter2(" / ")
    
    return

def multiply():
    e2.delete(0,END)
    
    sv=e.get()
    e2.insert(0,str(sv))
    
    global lv
    global mathoperation
    lv=float(sv)
    mathoperation="*"
    e.delete(0,END)
    enter2(" x ")
    
    return

def percent():
    e2.delete(0,END)
    
    sv=e.get()
    e2.insert(0,str(sv))
    
    global lv
    global mathoperation
    lv=float(sv)
    mathoperation="%"
    e.delete(0,END)
    enter2(" % ")

    return

def power():
    e2.delete(0,END)
    
    sv=e.get()
    e2.insert(0,str(sv))
    
    global lv
    global mathoperation
    lv=float(sv)
    mathoperation="^"
    e.delete(0,END)
    enter2("^ ")
    
    return     

def root():
    e2.delete(0,END)
    
    sv=e.get()
    e2.insert(0,str(sv))
    
    global lv
    global mathoperation
    lv=float(sv)
    mathoperation="v"
    e.delete(0,END)
    enter2(" ^(1/")
    
    return


def ln():
    e2.delete(0,END)
    enter2("ln ")
    
    global mathoperation
    mathoperation="ln"
    e.delete(0,END)
    return
def log():
    e2.delete(0,END)
    enter2("log ")
    
    global mathoperation
    mathoperation="log"
    e.delete(0,END)
    return


def factorial():
    e2.delete(0,END)
    
    sv=e.get()
    e2.insert(0,str(sv))
    
    global lv
    lv=float(sv)
    e.delete(0,END)
    e2.delete(0,END)
    if((lv==int(lv))and (lv>=0)):
        ans=1
        for i in range(1,int(lv)+1):ans=ans*i
        e.insert(0,str(ans))
        e2.insert(0,str(lv)+"!"+" ="+str(ans))
    else:
       e2.delete(0,END)
       e2.insert(0,"math error")
       e.delete(0,END) 
    return
def equalsto():
    sv=e.get()
    global rv
    rv=float(sv)
    e.delete(0,END)

    if (mathoperation=="+"):
        ans=lv+rv
        e.insert(0,str(ans))
        e2.delete(0,END)
        e2.insert(0,str(lv)+"+"+str(rv)+" =" +str(ans))

    if (mathoperation=="-"):
        ans=int(lv)-int(rv)
        e.insert(0,str(ans))
        e2.delete(0,END)
        e2.insert(0,str(lv)+"-"+str(rv)+" = "+str(ans))
        
    if (mathoperation=="*"):
        ans=lv*rv
        e.insert(0,str(ans))
        e2.delete(0,END)
        e2.insert(0,str(lv)+"x"+str(rv)+" = " +str(ans))
        
    if (mathoperation=="/"):
       if(rv!=0):
        ans=lv/rv
        e.insert(0,str(ans))
        e2.delete(0,END)
        e2.insert(0,str(lv)+"/"+str(rv)+" = "+str(ans))
       else:
        e2.delete(0,END)
        e2.insert(0,"math error")
        e.delete(0,END)
        
    if (mathoperation=="%"):
        ans=lv*(rv/100)
        e.insert(0,str(ans))
        e2.delete(0,END)
        e2.insert(0,str(lv)+" x "+str(rv)+"%"+" = "+str(ans))
        
    if (mathoperation=="^"):
        ans=lv**rv
        e.insert(0,str(ans))
        e2.delete(0,END)
        e2.insert(0,str(lv)+"^"+str(rv)+" ="+str(ans))
        
    if (mathoperation=="v"):
        ans=lv**(1/rv)
        e.insert(0,str(ans))
        e2.delete(0,END)
        e2.insert(0,str(lv)+"^(1/"+str(rv)+")"+" = "+str(ans))
        
    if (mathoperation=="log"):
        if(rv>0):
            ans=math.log10(rv)
            e.insert(0,str(ans))
            e2.delete(0,END)
            e2.insert(0,"log "+str(rv)+" = "+str(ans))
        else:
            e2.delete(0,END)
            e2.insert(0,"math error")
            e.delete(0,END)
            
    if (mathoperation=="ln"):
        if(rv>0):
            ans=math.log(rv)
            e.insert(0,str(ans))
            e2.delete(0,END)
            e2.insert(0,"ln "+str(rv)+" = "+str(ans))
        else:
            e2.delete(0,END)
            e2.insert(0,"math error")
            e.delete(0,END)
        
#number_butons        
bt=Button(wd,text="CLEAR SCREEN",bg="darkslategray",fg="lavenderblush",padx=190,pady=5,command=clear_screen).grid(row=11,column=0,columnspan=4)
b1=Button(wd,text="     1     ",padx=40,pady=5,bg="mediumpurple",command=lambda: enter(1)).grid(row=6,column=0)
b2=Button(wd,text="   2   ",padx=40,pady=5,bg="mediumpurple",command=lambda: enter(2)).grid(row=6,column=1)
b3=Button(wd,text="   3   ",padx=40,pady=5,bg="mediumpurple",command=lambda: enter(3)).grid(row=6,column=2)
b4=Button(wd,text="     4     ",padx=40,pady=5,bg="mediumpurple",command=lambda: enter(4)).grid(row=5,column=0)
b5=Button(wd,text="   5   ",padx=40,pady=5,bg="mediumpurple",command=lambda: enter(5)).grid(row=5,column=1)
b6=Button(wd,text="   6   "  ,padx=40,pady=5,bg="mediumpurple",command=lambda: enter(6)).grid(row=5,column=2)
b7=Button(wd,text="     7     ",padx=40,pady=5,bg="mediumpurple",command=lambda: enter(7)).grid(row=4,column=0)
b8=Button(wd,text="   8   ",padx=40,pady=5,bg="mediumpurple",command=lambda: enter(8)).grid(row=4,column=1)
b9=Button(wd,text="   9   ",padx=40,pady=5,bg="mediumpurple",command=lambda: enter(9)).grid(row=4,column=2)
b0=Button(wd,text="     0     ",padx=40,pady=5,bg="mediumpurple",command=lambda: enter(0)).grid(row=7,column=0)
#basic_operation_buttons
b_point=Button(wd,text="    .   ",padx=40,pady=5,bg="deepskyblue4",command=lambda: enter(".")).grid(row=7,column=1,columnspan=1)
b_plus=Button(wd,text="   + ",padx=40,pady=5,bg="deepskyblue4",command=plus).grid(row=4,column=3,columnspan=1)
b_minus=Button(wd,text="   -  ",padx=40,pady=5,bg="deepskyblue4",command=minus).grid(row=5,column=3,columnspan=1)
b_division=Button(wd,text="   /  "  ,padx=40,pady=5,bg="deepskyblue4",command=division).grid(row=6,column=3,columnspan=1)
b_multiplication=Button(wd,text="   x  ",padx=40,pady=5,bg="deepskyblue4",command=multiply).grid(row=7,column=3,columnspan=1)
b_equalto=Button(wd,text="   =  ",padx=40,pady=5,bg="deepskyblue4",command=equalsto).grid(row=7,column=2,columnspan=1)
#advanc_operation_buttons
b_percent=Button(wd,text="    %x   " ,padx=40,pady=5,bg="slateblue4",fg="white",command=percent).grid(row=9,column=0,columnspan=1)
b_log=Button(wd,text="  log " ,padx=40,pady=5,bg="slateblue4",fg="white",command=log).grid(row=9,column=1,columnspan=1)
b_ln=Button(wd,text="  ln  ",padx=40,pady=5,bg="slateblue4",fg="white",command=ln).grid(row=9,column=2,columnspan=1)
b_power=Button(wd,text=" x^y",padx=40,pady=5,bg="slateblue4",fg="white",command=power).grid(row=9,column=3,columnspan=1)
b_root=Button(wd,text="x^(1/y)",padx=40,pady=5,bg="slateblue4",fg="white",command=root).grid(row=10,column=0,columnspan=1)
b_pi=Button(wd,text="   Pi  ",padx=40,pady=5,bg="slateblue4",fg="white",command=pi).grid(row=10,column=1,columnspan=1)
b_factorial=Button(wd,text="    !   ",padx=40,pady=5,bg="slateblue4",fg="white",command=factorial).grid(row=10,column=2,columnspan=1)
b_Dtor=Button(wd,text="   e   ",padx=40,pady=5,bg="slateblue4",fg="white",command=ev).grid(row=10,column=3,columnspan=1)


mainloop()