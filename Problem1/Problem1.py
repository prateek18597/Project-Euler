# Multiples of 3 and 5
def sum_multiple_3_and_5(num):
	num-=1
	mul3=3*(num//3)*(num//3+1)//2
	mul5=5*(num//5)*(num//5+1)//2
	mul15=15*(num//15)*(num//15+1)//2
	print(mul3+mul5-mul15)

sum_multiple_3_and_5(1000)
sum_multiple_3_and_5(49)
sum_multiple_3_and_5(19564)