mylist=[]
mylist2=[]
mylist3=[]
tepelist=[]
a=int(input())
i=0
while i<a:
	b=int(input())
	mylist.append(b)
	mylist2.append(b)
	mylist3.append(b)
	tepelist.append(b)
	i=i+1
k=0
myb=[]
l=0
while k<3:
	myb.append(min(mylist))
	for num in myb:
		for num2 in mylist:
			if num==num2:
				mylist.remove(num2)	
	k=k+1
while l<3:
	myb.append(max(mylist))
	for num in myb:
		for num2 in mylist:
			if num==num2:
				mylist.remove(num2)	
	l=l+1
print(sorted(myb))

for num in mylist:
	for num2 in mylist2:
		if num==num2:
			mylist2.remove(num2)
print(mylist2)
j=1
while j<len(mylist3):
	del mylist3[j]
	j=j+1
print(mylist3)
s=0
g=0
while s<len(tepelist):
	del tepelist[s]
	s=s+3
print(tepelist)
