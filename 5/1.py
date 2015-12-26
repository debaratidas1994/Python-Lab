from Shapes import *
while True:
	x=input('1.Triangle,2.Square and 3.Circle')
	if x=='1':
		x,y,z=map(int,input('Enter 3 sides').split())
		print(Triangle.area(x,y,z))
		print(Triangle.perimeter(x,y,z))
	elif x=='2':
		x=int(input('Enter side of square'))
		print(Square.area(x))
		print(Square.perimeter(x))
	elif x=='3':
		x=int(input('Enter radius'))
		print(Circle.area(x))
		print(Circle.circumference(x))
	else:
		break
