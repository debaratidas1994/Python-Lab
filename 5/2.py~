"""
Experiment with ply
Tokenize the following as follows:
abc * b => (abc, ID) (*, OP) (b, ID)
pq ** b => (pq, ID) (**, OP) (b, ID)
ab < bc + cd => (ab, ID) (< , OP) (bc, ID) (+, OP) (cd, ID)
p --- q => (p, ID) (--, OP) (-, OP) (q, ID)
"""
import ply.lex as lex
tokens=['ID','OP']
t_ID=r'[a-z]+'
t_OP=r'-{1,2}|\+|\*{1,2}|<'
l=lex.lex()
l.input(input())
for i in l:
	print (i.value,i.type)

