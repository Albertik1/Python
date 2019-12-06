l= input().split()
i=0

s=0
f=0


for i in l:
	if i=="True":
		s=s+1
	if i=="False":
		f=f+1
		
if f==0:
	print("Not one False")
elif s>=1:
	print("At least one True")
elif s==0:
	print("All false")

