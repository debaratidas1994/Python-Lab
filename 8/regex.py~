'''
Do the following using regular expressions:-
a) Find all occurrences of a word in a multiline string. The search
must be case insensitive. Also find and display the starting index of
each matched word in the input string.
b) Given a line of text find all characters other than vowels and space
characters.
c) Given a list of strings find all strings that start with a digit or an
underscore.
'''

import re
s='''hello how the ThE there
are you
the world is awesome'''
for i in re.finditer(r'\bthe\b',s,re.I):
	print(i.string[i.span()[0]:i.span()[1]])
print(re.findall('[^aeiou\s]',s,re.M))
l=eval(input())
print( [x for x in l if re.match(r'[0-9_]',x)])
#print(list(filter(lambda x:re.match(r'[0-9_]',x),l)))
