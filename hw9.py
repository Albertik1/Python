def second_max(mylist):
	mylist.sort()
	return 	mylist[-2]
	
	
mylist=[]
mylist2=[]
a=int(input())
i=0
k=0
while i<a:
	x=int(input())
	mylist.append(x)
	mylist2.append(x)
	i=i+1
	
same_value=list(set(mylist))
	
	
print(second_max(same_value))	

#print(second_max(mylist))

