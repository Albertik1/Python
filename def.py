def second_max(mylist):
	mylist.sort()
	return mylist[-2]	
mylist=[]
a=int(input())
i=0
while i<a:
	x=int(input())
	mylist.append(x)
	i=i+1
print(mylist)
print("2nd largest number: ", second_max(mylist))
print(mylist)
