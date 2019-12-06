n=int(input())
i=0
a=0
l=[]
while i<n:
	a=int(input())
	l.append(a)
	i=i+1
for i in l:
  print((sum(l)-i))
