import math 

def primefactors(num):
	if num%2==0:
		yield 2
		num=num/2
	# print(int(math.sqrt(num)))
	for i in range(3,int(math.sqrt(num))+1,2):
		if num%i==0:
			yield i
			while num%i==0:
				num=num//i
	if num>2:
		yield num

n=int(input("Enter number of Test Cases:\n"))
for i in range(n):
	t=int(input("Enter Case:\n"))
	x=max(list(primefactors(t)))
	print(x)