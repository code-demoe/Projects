from tkinter import *
from ttkthemes import themed_tk as theme
from tkinter import ttk
from PIL import ImageTk,Image
import math

root=theme.ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.title('Calculator')
root.iconbitmap(r'C:\Users\HP\.spyder-py3\gui\Project_calc\calc.ico')

root.geometry('500x430')

main=Frame(root).grid(row=0,column=0)
fram1=Frame(main).grid(row=0,column=0)
frame=Frame(main).grid(row=0,column=1,padx=50)

Label(fram1,text=' ').grid(row=0,column=0,pady=50,sticky='n')


equation=ttk.Entry(frame,width=32,font='Times 18 italic',justify=RIGHT)
equation.grid(row=0,column=1,pady=1,ipady=20,ipadx=1,columnspan=4,sticky='we')


def instr():
    global pic
    top = Toplevel()
    top.title('Instructions')
    top.iconbitmap(r'C:\Users\HP\.spyder-py3\gui\Project_calc\calc.ico')
       
    C=Canvas(top,width=900,height=500)
    pic=ImageTk.PhotoImage(Image.open(r'C:\Users\HP\.spyder-py3\gui\Project_calc\bg7.jpg'))
    C.create_image(0,0,anchor=NW,image=pic)
    print('here')
    C.create_text(500,220,text='''\n
              1.Insert the values before choosing a function from f(x).\n
              2.Use f(x) to choose a function.\n
              3.Available functions are:\n
              \ti)Logrithmic : ln(natural log with base e), log(with base 10)\n
              \tii)Trignometric : sin, cos, tan, cosec, sec, cot\n
              \tiii)Algebric : 1/x, √, x²\n
              4.After choosing desired function press ok to get result.\n
              5.Use the buttons given on the calculator to perform operations.\n
              6.Numeric Entries can be added directly from keyboard.\n
              7.Equal to sign (=) can be selected by pressing tab, and can be pressed using spacebar(nice shortcut right) ;)\t\t
        ''',justify=LEFT,font=('Times',13,'bold italic'),fill='white')
    C.grid(row=0,column=0,sticky='nsew')
    top.geometry('900x500')
    
def press(num):
    equation.insert(END,num)

def clearall():
    equation.delete(0,END)

def clear():
    val=equation.get()[:-1]
    equation.delete(0,END)
    equation.insert(0,val)
        
def equal():
    try:
        val=eval(equation.get())
    except SyntaxError or NameError:
        equation.delete(0,END)
        equation.insert(0,'Invalid Input')
        err=messagebox.showwarning(title='Invalid Input',message='Please Input valid Syntax')
        if err=='ok':
            equation.delete(0,END)
    else:
        equation.delete(0,END)
        equation.insert(0,val)

def sqrt():
    try:
        val=math.sqrt(eval(equation.get()))
    except SyntaxError or NameError:
        equation.delete(0,END)
        equation.insert(0,'Invalid Input')
        err=messagebox.showwarning(title='Invalid Input',message='Please Input valid Syntax')
        if err=='ok':
            equation.delete(0,END)
    else:
        equation.delete(0,END)
        equation.insert(0,val)

def sqr():
    try:
        val=eval(equation.get())
    except SyntaxError or NameError:
        equation.delete(0,END)
        equation.insert(0,'Invalid Input')
        err=messagebox.showwarning(title='Invalid Input',message='Please Input valid Syntax')
        if err=='ok':
            equation.delete(0,END)
    else:
        equation.delete(0,END)
        equation.insert(0,math.pow(val,2))
        
def sign():
    try:
        val=eval(equation.get())
    except SyntaxError or NameError:
        equation.delete(0,END)
        equation.insert(0,'Invalid Input')
        err=messagebox.showwarning(title='Invalid Input',message='Please Input valid Syntax')
        if err=='ok':
            equation.delete(0,END)
    else:
        equation.delete(0,END)
        equation.insert(0,-(val))
        
def inverse():
    try:
        val=1/eval(equation.get())
    except ZeroDivisionError or SyntaxError or NameError:
        equation.delete(0,END)
        equation.insert(0,'Invalid Input')
        err=messagebox.showwarning(title='Invalid Input',message='Please Input valid Syntax')
        if err=='ok':
            equation.delete(0,END)
    else:
        equation.delete(0,END)
        equation.insert(0,val)

def nlog():
    try:
        val=math.log(eval(equation.get()))
    except ValueError or ZeroDivisionError or SyntaxError or NameError:
        equation.delete(0,END)
        equation.insert(0,'Invalid Input')
        err=messagebox.showwarning(title='Invalid Input',message='Please Input valid Syntax')
        if err=='ok':
            equation.delete(0,END)
    else:
        equation.delete(0,END)
        equation.insert(0,val)
    
def log10():
    try:
        val=math.log10(eval(equation.get()))
    except ValueError or ZeroDivisionError or SyntaxError or NameError:
        equation.delete(0,END)
        equation.insert(0,'Invalid Input')
        err=messagebox.showwarning(title='Invalid Input',message='Please Input valid Syntax')
        if err=='ok':
            equation.delete(0,END)
    else:
        equation.delete(0,END)
        equation.insert(0,val)

def sin():
    try:
        val=math.sin(eval(equation.get()))
    except ValueError or ZeroDivisionError or SyntaxError or NameError:
        equation.delete(0,END)
        equation.insert(0,'Invalid Input')
        err=messagebox.showwarning(title='Invalid Input',message='Please Input valid Syntax')
        if err=='ok':
            equation.delete(0,END)
    else:
        equation.delete(0,END)
        equation.insert(0,val)

def cos():
    try:
        val=math.cos(eval(equation.get()))
    except ValueError or ZeroDivisionError or SyntaxError or NameError:
        equation.delete(0,END)
        equation.insert(0,'Invalid Input')
        err=messagebox.showwarning(title='Invalid Input',message='Please Input valid Syntax')
        if err=='ok':
            equation.delete(0,END)
    else:
        equation.delete(0,END)
        equation.insert(0,val) 

def tan():
    try:
        val=math.tan(eval(equation.get()))
    except ValueError or ZeroDivisionError or SyntaxError or NameError:
        equation.delete(0,END)
        equation.insert(0,'Invalid Input')
        err=messagebox.showwarning(title='Invalid Input',message='Please Input valid Syntax')
        if err=='ok':
            equation.delete(0,END)
    else:
        equation.delete(0,END)
        equation.insert(0,val)

def cosec():
    try:
        val=math.cosec(eval(equation.get()))
    except ValueError or ZeroDivisionError or SyntaxError or NameError:
        equation.delete(0,END)
        equation.insert(0,'Invalid Input')
        err=messagebox.showwarning(title='Invalid Input',message='Please Input valid Syntax')
        if err=='ok':
            equation.delete(0,END)
    else:
        equation.delete(0,END)
        equation.insert(0,val)
        
def sec():
    try:
        val=math.sec(eval(equation.get()))
    except ValueError or ZeroDivisionError or SyntaxError or NameError:
        equation.delete(0,END)
        equation.insert(0,'Invalid Input')
        err=messagebox.showwarning(title='Invalid Input',message='Please Input valid Syntax')
        if err=='ok':
            equation.delete(0,END)
    else:
        equation.delete(0,END)
        equation.insert(0,val)

def cot():
    try:
        val=math.cot(eval(equation.get()))
    except ValueError or ZeroDivisionError or SyntaxError or NameError:
        equation.delete(0,END)
        equation.insert(0,'Invalid Input')
        err=messagebox.showwarning(title='Invalid Input',message='Please Input valid Syntax')
        if err=='ok':
            equation.delete(0,END)
    else:
        equation.delete(0,END)
        equation.insert(0,val)

def choosefun():
    if choose.get()=='ln':
        nlog()
    elif choose.get()=='log':
        log10()
    elif choose.get()=='sin':
        sin()
    elif choose.get()=='cos':
        cos()
    elif choose.get()=='tan':
        tan()
    elif choose.get()=='cosec':
        cosec()
    elif choose.get()=='sec':
        sec()
    elif choose.get()=='cot':
        cot()
    elif choose.get()=='1/x':
        inverse()
    elif choose.get()=='√':
        sqrt()
    elif choose.get()=='x²':
        sqr()
    
    
ttk.Button(frame,text='=',width=8,command=equal).grid(row=7,column=4)  

ttk.Button(frame,text='7',width=8,command=lambda:press(7)).grid(row=4,column=1)
ttk.Button(frame,text='8',width=8,command=lambda:press(8)).grid(row=4,column=2)
ttk.Button(frame,text='9',width=8,command=lambda:press(9)).grid(row=4,column=3)
ttk.Button(frame,text='4',width=8,command=lambda:press(4)).grid(row=5,column=1,sticky='e')
ttk.Button(frame,text='5',width=8,command=lambda:press(5)).grid(row=5,column=2)
ttk.Button(frame,text='6',width=8,command=lambda:press(6)).grid(row=5,column=3)
ttk.Button(frame,text='1',width=8,command=lambda:press(1)).grid(row=6,column=1,sticky='e')
ttk.Button(frame,text='2',width=8,command=lambda:press(2)).grid(row=6,column=2)
ttk.Button(frame,text='3',width=8,command=lambda:press(3)).grid(row=6,column=3)
ttk.Button(frame,text='0',width=8,command=lambda:press(0)).grid(row=7,column=2)

ttk.Button(frame,text='+',width=8,command=lambda:press('+')).grid(row=6,column=4)
ttk.Button(frame,text='-',width=8,command=lambda:press('-')).grid(row=5,column=4)
ttk.Button(frame,text='x',width=8,command=lambda:press('*')).grid(row=4,column=4)
ttk.Button(frame,text='÷',width=8,command=lambda:press('/')).grid(row=3,column=4)
ttk.Button(frame,text='%',width=8,command=lambda:press('%')).grid(row=3,column=1,sticky='e')
ttk.Button(frame,text='.',width=8,command=lambda:press('.')).grid(row=7,column=3)
ttk.Button(frame,text='(',width=8,command=lambda:press('(')).grid(row=3,column=2)
ttk.Button(frame,text=')',width=8,command=lambda:press(')')).grid(row=3,column=3)

ttk.Button(frame,text='AC',width=8,command=clearall).grid(row=2,column=3)
ttk.Button(frame,text='C',width=8,command=clear).grid(row=2,column=4)
ttk.Button(frame,text='±',width=8,command=sign).grid(row=7,column=1,sticky='e')

ttk.Button(frame,text='Instructions',width=32,command=instr).grid(row=8,column=1,sticky='we',columnspan=4)
Label(fram1,text=' ').grid(row=1,column=0,sticky='e',padx=20)

logop=('log','ln')
trigop=('sin','cos','tan','cosec','sec','cot')
algop=('1/x','√','x²')

choose=StringVar()
choose.set('f(x)')
  
menu_button=ttk.Menubutton(frame,text=choose.get(),width=9)
mainmenu=Menu(menu_button,tearoff=0)

lmenu=Menu(mainmenu,tearoff=0)
for l in logop:
    lmenu.add_radiobutton(value = l,label = l,variable = choose)
mainmenu.add_cascade(label='Logrithmic',menu=lmenu)

tmenu=Menu(mainmenu,tearoff=0)
for t in trigop:
    tmenu.add_radiobutton(value=t,label=t,variable=choose)
mainmenu.add_cascade(label='Trignometric',menu=tmenu)

amenu=Menu(mainmenu,tearoff=0)
for a in algop:
    amenu.add_radiobutton(value=a,label=a,variable=choose)
mainmenu.add_cascade(label='Algebric',menu=amenu)

menu_button.configure(menu=mainmenu)
menu_button.grid(row=2,column=1,sticky='e')
ttk.Button(frame,text='Ok',width=8,command=choosefun).grid(row=2,column=2)

mainloop()