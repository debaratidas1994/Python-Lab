"""

Write a program to sum the elements of an array (list) using 4 threads. Let
each thread add quarter of the array. Assume that the size of the array is a
multiple of 4. Use global variable “total_sum” which gets updated by each
thread once it computes partial sum. Use lock when global variable is
getting updated.
"""



from threading import *
total_sum=0
l=Lock()
def sum_it(x):
	global total_sum
	x=sum(x)
	l.acquire()
	total_sum+=x
	l.release()
list=eval(input())
x=len(list)//4
t1=Thread(target=sum_it,args=(list[:x],))
t2=Thread(target=sum_it,args=(list[x:2*x],))
t3=Thread(target=sum_it,args=(list[2*x:3*x],))
t4=Thread(target=sum_it,args=(list[3*x:4*x],))
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
print(total_sum)
