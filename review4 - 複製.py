mylist= list(range(0, 101))
a= int(input())
if (a%2==0) :
	for a in range(0, 101, 2):
		print(a)
	
else:
	for a in range(1, 100, 2):
		print(a) 
