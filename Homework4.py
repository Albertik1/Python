myList = []
n = int(input())
for i in range(n):
	i = str(input()) 
	i = i.rstrip()
	myList.append(i)
print (myList)
maximum = max(myList,key=len)
print("Maximum:", maximum)
minimum = min(myList,key=len)
print("Minimum:", minimum)
totalString = sum(len(a) for a in myList)
print("Total strings:", totalString)
myList.sort(key=len)
print("Ordered by length:", myList)
myList.remove(max(myList,key=len))
myList.remove(min(myList,key=len))
print("Sliced list:", myList)
