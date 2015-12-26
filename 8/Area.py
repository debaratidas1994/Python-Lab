Cpi=3.14
def circle(r):
	return pi*r*r
def rect(a,b):
	return a*b
def tri(a,b,c):
	s=(a+b+c)/2
	return (s*(s-a)*(s-b)*(s-c))**0.5
if __name__=='__main__':
	import sys
	name=sys.argv[1]
	if name=='circle':
		if len(sys.argv)==3:
			print(circle(int(sys.argv[2])))
		else:
			print('More args than expected' if len(sys.argv)>3 else 'Lesser args than expected')
	elif name=='rect' and len(sys.argv)==4:
		print(rect(int(sys.argv[2]),int(sys.argv[3])))
	elif name=='tri' and len(sys.argv)==5:
		print(tri(int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])))
	else:
		print('Bad Input')

