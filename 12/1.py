'''
Write a function which prints a message given as argument. Decorate the
function twice with different decorators
Assume the function is print_message and the message to be printed is
"hello".
Decorating print_message with a function called stars should print :
*****
hello
*****
Decorating print_message twice using dollars and stars should print :
$$$$$
*****
hello
*****
$$$$$
Create a
'''
def dollar_dec(fun):
	def inner(x):
		print('$'*len(x))
		fun(x)
		print('$'*len(x))
	return inner
def star_dec(fun):
	def inner(x):
		print('*'*len(x))
		fun(x)
		print('*'*len(x))
	return inner
@dollar_dec
@star_dec
def print_it(x):
	print(x)
print_it(str(input()))
