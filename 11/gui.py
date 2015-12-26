from Tkinter import *

root=Tk()

l1=Label(root,text='Num1')
l1.grid(row=0,column=0,columnspan=2)
e1=Entry(root)
e1.grid(row=0,column=2,columnspan=2)
l2=Label(root,text='Num2')
l2.grid(row=1,column=0,columnspan=2)
e2=Entry(root)

e2.grid(row=1,column=2,columnspan=2)
v=IntVar(root)
t=StringVar(root)
def add():
	try:
		t.set(str(int(e1.get())+int(e2.get())))
	except:
		t.set('Bad Input')
def sub():
	try:
		t.set(str(int(e1.get())-int(e2.get())))
	except:
		t.set('Bad Input')
def mul():
	try:
		t.set(str(int(e1.get())*int(e2.get())))
	except:
		t.set('Bad Input')
def div():
	try:
		t.set(str(int(e1.get())/int(e2.get())))
	except:
		t.set('Bad Input')
r1=Radiobutton(root,text='ADD',variable=v,value=1,command=add)
r1.grid(row=3)
r2=Radiobutton(root,text='SUB',variable=v,value=2,command=sub)
r2.grid(row=3,column=1)
r3=Radiobutton(root,text='MUL',variable=v,value=3,command=mul)
r3.grid(row=3,column=2)
r4=Radiobutton(root,text='DIV',variable=v,value=4,command=div)
r4.grid(row=3,column=3)
lll=Label(root,text='Result')
lll.grid(row=4,column=0,columnspan=2)
r=Entry(root,textvariable=t)
r.grid(row=4,column=2,columnspan=2)
root.mainloop()
