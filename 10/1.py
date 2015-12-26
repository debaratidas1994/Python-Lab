'''
Write an iterator (class) that returns numbers in the Fibonacci series for a
given range.
If the range is 30, it should return 0 1 1 2 3 5 8 13 21
'''
class Fib:
	def __init__(self,end):
		self.end=end
		self.next=0
		self.a=0
		self.b=1
	def __iter__(self):
		return self
	def __next__(self):
		t=self.next
		if t>self.end:
			raise StopIteration
		if self.next==0:
			self.next=1
		else:
			self.a=self.b
			self.b=self.next
			self.next=self.a+self.b
		return t
f=Fib(30)
print(list(f))
