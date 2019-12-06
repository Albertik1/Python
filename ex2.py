mylist=[10, 20, 50, 40, 30]
a=int(input())
if (a==1):
	mylist.sort()
	for i in list(mylist):
		print(i)
elif a==2:
	mylist.sort()
	mylist.reverse()
	for i in list(mylist):
		print(i)
elif a==3:
	#sum=10+20+30+40+50;
	#average= sum(mylist)/len(mylist);
	print(int(sum(mylist)/len(mylist)))
else:
	for i in list(mylist):
		print(i)
