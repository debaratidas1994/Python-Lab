"""
Given a file “stateinfo.txt” containing names of the state and cities
separated by “:”, create a file for each state named as “statename”.txt
containing names of cities in that state. Sample input file “stateinfo.txt” is
attached. Steps to follow:
Walk through the file. Create a dictionary whose key is the state name and
value is the file handle. Write city names into the file.
Do close all the files at the end of processing using values in dictionary.
"""
f=open('stateinfo.txt','r')
import os
try:
	os.mkdir('op_files')
except Exception as E:
	print(E)
d=dict()
for i in f:
	st_name,cy_name=i.strip().split(':')
	d[st_name]=d.get(st_name,list())+[cy_name]
os.chdir('op_files')
for i in d:
	g=open(i+'.txt','w')
	for j in d[i]:
		g.write(j+'\n')
	g.close()
f.close()
