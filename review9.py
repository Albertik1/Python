l=[]
l2=[]
l3=[]
summ=0
n = input()
l = n.split()
for i in l:
	if i.isdigit():
		i=int(i)
		l2.append(i)
for i in l2:
	if i%2!=0:
		l3.append(i+1)
	elif i%2==0:
		l3.append(i*i)
print(l3)
print(sum(l3))

