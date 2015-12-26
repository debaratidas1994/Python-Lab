def next_prime():
	i=2
	while True:
		for j in range(2,i):
			if i%j==0:
				break
		else:
			yield i
		i+=1
max=10
x=next_prime()
for i in range(max):
	print(next(x))
