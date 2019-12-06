n=int(input())
fact=1
summ=0
while n>=0:
	for i in range(1,n+1):
		fact=fact*i
	print("factorial ", n)
	print(fact)
	summ=fact+summ
	fact=1
	n=n-1

print("Sum = ", summ)

