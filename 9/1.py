"""
Write a function which gets no: of strings using variable no: of arguments
and find unique characters in each string.
Write a function which concatenates all given strings to a single string.
User can specify sep - default should be comma.
User can specify first string - default should be 'result: '

"""
def fun1(*l):
	for s in l:
		print(s,list(set(s)))
def fun2(*l,sep=',',default='result:'):
	return default+sep.join(list(l))

fun1('ad','dfdf','dfdfffffsaa')

print(fun2('asd','ad','ccasa','lopedew','edldp'))
print(fun2('asd','ad','ccasa','lopedew','edldp',default='xyz:'))
