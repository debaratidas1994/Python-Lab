"""
Write a line of code using lambda function along with map/reduce/filter
functions to do the following:-
a) Given x and n (read as user input), create a list having powers of x
from 1 to n
Eg: If x=2,n=5 the result must be [2,4,8,16,32]

b) Given a list of strings, remove all strings having first character as
digit

c) Given a list of numbers, find maximum in the list

d) Given a list of tuples containing two integers, remove all tuples
where second element in tuple is not a factor of first element.

e) Given a list of integers, combine all integers to form a single
integer.
Eg: [1,25,32,4,5] ==> 1253245

"""
x,n=2,5
print(list(map(lambda i:x**i,range(1,n+1))))

l=['abc','1abc','def','2def','wrweg','353dsfg']
print(list(filter(lambda x:not(x[0].isdigit()),l)))

l=range(10)
from functools import reduce
print(reduce(lambda x,y:max(x,y),l))

l=[(2,1),(9,3),(10,5)]
print(list(filter(lambda x:x[0]%x[1]==0,l)))

l=[1,25,32,4,5]
print(reduce(lambda x,y:str(x)+str(y),l))
