'''
Given an input file, do the following using regular expression and create
an output file.
a) Remove extra whitespaces between two words.
b) Insert a white space after the end of a sentence (after . or ? or !).
c) First letter of each sentence should be upper case
d) Remove consecutive duplicate words.
'''
f=open('inp.txt')
l=f.read()
import re

def fun1(m):
	return m.group(1)
l=re.sub(r'(\s)+',fun1,l)

def fun2(m):
	return m.group(1)+' '+m.group(2)
l=re.sub(r'([.?!])(\w)',fun2,l)


l=re.sub(r'(\b)(\w+)(\s\2)+',r'\1\2',l)

def fun3(m):
	return m.group(1)+m.group(2)+m.group(3).upper()
l=re.sub(r'([.?!])(\s)(\w)',fun3,'. '+l)[2:]

f.close()
g=open('op.txt','w')
g.write(l)
