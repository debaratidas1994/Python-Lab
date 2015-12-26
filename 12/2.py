'''
Create a table Person, with fields Name (contains first name followed by
last name), Age, AreaofInterest (Music, Dance, Sports, Travel), Occupation
a) Find all persons whose last name is “Sharma”
b) Find the most common area of interest among all persons
c) Delete all entries having area of interest other than ( Music, Dance,
Sports, Travel)
Demonstrate autocommit feature in sqlite
'''
import sqlite3
con=sqlite3.connect('Person')
con.execute('create table if not exists person(name text primary key,age int,areaofinterest text)')
con.executescript('''
insert into person values('a bcd',20,'music');
insert into person values('a sharma',20,'cs');
insert into person values('ksjdk sjfhj',20,'cs');
insert into person values('hfj djkfh',23,'dance');
insert into person values('b sharma',20,'sports');
insert into person values('ab sharma',10,'music');
insert into person values('abc sharma',25,'travel');
''');
cur=con.execute("select name from person where name like '% sharma'")

print(cur.fetchall())

cur=con.execute('''select areaofinterest 
		   from (select areaofinterest,count(*) as counts
		   	 from person
			 group by areaofinterest) as X
	           where X.counts=(select max(counts) from (select areaofinterest,count(*) as counts
		   	 from person
			 group by areaofinterest))''')
print(cur.fetchall())
cur=con.execute('''delete from Person where areaofinterest not in ('music','dance','sports','travel')''')
cur=con.execute('''select * from person''')
print(cur.fetchall())

#print(sqlite3.sqlite3_get_autocommit())
