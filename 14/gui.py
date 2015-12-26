'''
Write a graphics based program using Tkinter. Main window must have
dimensions 250 x 200 placed at 100,100 from top left. Provide one button
with background color “red” labelled “Click Me”, one label having initial
text “Not Clicked Yet” with background color “blue” and a button labelled
“EXIT”. On first click of the button, the label text must change to “1 click”
and font must change to Times, Bold and size 20. On every subsequent
click, label text should show how many clicks. On even click, background
color of label must change to “purple” and on odd click, it must change to
“green”. When button labelled “EXIT” is clicked, it should exit the GUI
'''

from Tkinter import *
count=0
def fun():
	global count
	count+=1
	if count%2==1:
		l.configure(bg='green')
	else:
		l.configure(bg='purple')
	s.set('{} Clicks'.format(count))
	l.configure(font=('Times',20,'bold'))

root=Tk()
root.geometry('250x250+100+100')
s=StringVar(root)
s.set('Not Clicked Yet')
l=Label(root,textvar=s,bg='blue')
b1=Button(root,bg='red',text='Click Me',command=fun)
b2=Button(root,text='Exit',command=exit)
l.pack()
b1.pack()
b2.pack()
root.mainloop()
