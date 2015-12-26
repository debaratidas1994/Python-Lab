d,m,y=map(int,input().split('/'))
def leap(y):
	return (y%400==0) or (y%4==0 and y%100!=0)
if y<=0:
	print('Invalid')
	exit()
if not(1<=m<=12):
	print('Invalid')
	exit()
if m in (1,3,5,7,8,10,12) and not(1<=d<=31):
	print('Invalid')
	exit()
elif m==2:
	if leap(y):
		print('leap year')
		if not(1<=d<=29):
			print('Invalid')
			exit()
	else:
		print('not leap year')
		if not(1<=d<=28):
			print('Invalid')
			exit()
print('Valid!')
