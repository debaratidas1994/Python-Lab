"""

Create table employee with fields ID primary key, name, age, salary,
deptid(foreign key refers id in dept)
a) Find youngest employee from each department
b) Display department name and total number of employees in that
department
c) Find the department name with the highest paid employee. Also
display employee name
"""
import sqlite3
con=sqlite3.connect('employee')
con.execute('create table if not exists dept(id int,deptname text,primary key(id))')
con.execute('create table if not exists employee(id int,name text,age int,salary int,deptid int,primary key(id),foreign key(deptid) references dept(id))')
print(con.execute('select * from dept').fetchall())
con.executescript('''insert into dept values(1,"Comp");
		    insert into dept values(2,"ECE");
		    insert into dept values(3,"EEE");
		    ''')

con.executescript('''insert into employee values(100,"abc",25,3000,1);
		    insert into employee values(101,"asd",28,3500,2);
		    insert into employee values(102,"wer",30,4000,3);
		    insert into employee values(103,"dsv",33,10000,1);	
		    insert into employee values(104,"ops",35,3245,2);	
    		    insert into employee values(105,"wer",38,3535,3);
		''')


cur=con.execute('''select deptname,name,age
		   from employee as E,dept as D
		   where E.deptid=D.id and E.age=(select min(age) 
		   			    from   employee E1
					    where E1.deptid=E.deptid)''')
for i in cur.fetchall():
	print(i)

cur=con.execute('''select deptname,deptid,count(*)
		   from employee,dept
		   where employee.deptid=dept.id
		   group by deptname,deptid''')
for i in cur.fetchall():
	print(i)

cur=con.execute('''select deptname,name,salary
		   from employee,dept
		   where employee.deptid=dept.id and employee.salary=(select max(salary) from employee)''')
for i in cur.fetchall():
	print(i)

