'''
The file test.py has the following code:
import re
print(help(re))
Run the program test.py as follows.
python3 test.py > re.doc
Process this file re.doc. Find all functions (print only function names)
declared between FUNCTIONS and DATA sections.
'''
import re
inp=open('re.txt').read()
x=re.search('FUNCTIONS(.*)DATA',inp,re.DOTALL).group(1)
t=re.finditer('([^\s]*?)\(.*?\)',x)
for i in t:
	if i.group(1)!='':print(i.group(1))
