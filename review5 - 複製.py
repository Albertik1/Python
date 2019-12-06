mylist = list(range(0, 11))
n=int(input())
m=n
c=0
a=0
del(mylist[5])
for num in mylist:
	print(num)
for num in mylist:
	a+=num
	c+=1
aver=a/c
print(float(aver))
print(float(aver*m))

