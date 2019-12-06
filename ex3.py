n = int(input())
l =[]
if (n==0 or n==99):
	print('cannot proceed')
elif (n<0):
	a=[]
	l=list(range(n,1))
	l.reverse()
	print(l)
	for i in l:
		a.append(i**2)
	print(a)
	print(l+a)
else:
	a=[]
	l=list(range(0, n+1))
	print(l)
	for i in l:
		a.append(i**2)
	print(a)
	print(l+a)
		
