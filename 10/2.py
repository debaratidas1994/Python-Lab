'''
Create a table which has name and date of birth of a person.
(Use date type for date of birth, enter date as ‘yyyy-mm-dd’)
a) Read the name and date of birth from the keyboard for four
records, store them in a list of tuples and insert into the table. (Use
executemany function)

b) Display the name and the age of the person (in years).
Check julianday() function
julianday(d1)-julianday(d2) gives the difference between two dates
in no of days

c) Find all persons whose birthday falls in a given month (eg: input is
‘04’ for april,’01’ for jan)
'''
import sqlite3
con=sqlite3.connect('Person.db')

con.execute('create table if not exists person(name text,dob date)')
l=[('me','1995-02-25'),('bharath','1995-08-15'),('darshan','1995-09-09'),('deepak','1995-05-18')]

#for i in range(4):
#	name,dob=input().split(',')
#	l.append((name,dob))

con.executemany('insert into person values(?,?);',l)
cur=con.execute('select name,julianday("now")-julianday(dob) from person;')
l=cur.fetchall()

for i in l:
	print(i[0],':',i[1]//365)
while input('ch')!='-1':
	m=input('enter month')
	cur=con.execute('select name,person.dob from person where "{}"=strftime("%m",dob);'.format(m))
	print(cur.fetchall())
