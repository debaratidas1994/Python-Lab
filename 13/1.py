'''
i.
Write a line of code using generator expression for the following:-
(Do not use list comprehension anywhere)

a) Find the longest and second longest word in a multiline string (can
use inbuilt sorted method for sorting)

b) Find all words in a line of text where a character repeats anywhere
in that word

ii. Write a line of code for the following using list comprehension.
a) Given a list L containing numbers, return a new list with
cumulative sum, that is, a new list where the ith element is the sum
of first i+1 elements from the original list.
For example, given a list [1,2,3,4] the result should be [1,3,6,10]
b) Find all numbers between a pair of numbers which are perfect
squares and sum of all digits in the number is less than 10
'''
import re
#l=eval(input())
l='''hello tihs is deb'''
g=(list (sorted (l,key=lambda x:len(x),reverse=True))[i] for i in range(2))

for i in g:
	print(i)
g=(i for i in input().split() if len(i)!=len(set(i)))

for i in g:
	print(i)
#
#s="hello face hi i am deb"
#print(list(x for x in s.split(' ') if re.search(r'(\w).*\1',x)))

l=[1,2,3,4]
print([sum(l[:i]) for i in range(1,len(l)+1)])

l=range(100)
print([i for i in l if int(i**0.5)**2==i and sum(map(int,str(i)))<=10])

