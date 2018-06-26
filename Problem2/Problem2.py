def fibonacci(num):
	a,b=1,2
	c=1
	while c<=num:
		if c%2==0:
			yield a
		a,b,c=b,a+b,c+1
	return 

n=int(input("Enter number of Test Cases:\n"))
for i in range(n):
	t=int(input("Enter Case:\n"))
	print(sum(list(fibonacci(t))))
