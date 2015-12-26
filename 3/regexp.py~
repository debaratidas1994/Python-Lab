'''
Given an input file which contains list of names, phone numbers and
email-ids separated by spaces in the following format:-
Alex 80-23425525 alex234@yahoo.com
Emily 322-56775342 em_44@gmail.com
Grace 20-24564555 softech_grace@rediffmail.com
Phone number contains 3 or 2 digit area code and a hyphen followed by 8
digit number
Perform the following using regular expressions:-
a) Find all phone numbers having 4 consecutive 0s at the end.
b) Find all names having phone numbers with 3 digit area code.
c) Find the total number of people having gmail id.
d) Find user name part of email id for all people whose name start
with 'G' or 'E' and ends with 'y'
e) Find all names whose phone numbers are not in proper format.
'''
import re
#f=open('inp.txt')
names=['deb','lisa','poo']
phones=['9980035629','789-5679','678-7890','567-0000']
emails=['debarati@gmail.com','lisa@yahoo.com']
'''
for i in f:
	name,ph,email=i.strip().split()
	names.append(name)
	phones.append(ph)
	emails.append(email)
for i in phones:
	if(re.match(r'0000$',i)):
		print i
'''
for i in phones:
	if re.fullmatch('[0-9]{2,3}-[0-9]{4}0000',i):
		print(i)
'''
for j in range(len(phones)):
	i=phones[j]
	if re.match('[0-9]{3}-[0-9]{8}',i):
		print(names[j])

count=0;
for j in emails:
	if re.fullatch('.*?@gmail/.com',j):
		count+=1
print(count)

for j in range(len(names)):
	if re.fullmatch('[GE].*y',names[j]):
		print(re.match('(.*?)@.*/.com$',j).group(1))
for i in range(len(phones)):
	j=phones[i]
	if re.fullmatch('[0-9]{2,3}-[0-9]{8}',j)==None:
		print(names[i])
'''
