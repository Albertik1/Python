l=[]
numm=0
nummm=0
def eliminate(l2):
	i=1
	while i<len(l2):
		if l2[i][:-1].isdigit():
			l2.remove(l2[i])
			i=0
		elif i==-1:
			print("Empty")	
		else:
			i=i+1
while True:
	n=input()
	l.append(n)		
	if '-1' in l:
		break		
del l[-1]
for k in l:
	numm=numm+1
for k in l:	
	print(k)
eliminate(l)
for i in l:
	print(i)
if numm==0:
	print('Empty')
