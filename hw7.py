case=int(input())
l=[]
count=0
k=1
x=0
while x<case:
    n=int(input())
    l.append(n)
    x=x+1
for i in l:
    while 1:
        if i==1:
            count=count+1 
            break
        if i%2==0:
            i=i/2
            count=count+1 
        else:
            i=i*3+1 
            count=count+1 
    print("Case ", k,":", count)
    k=k+1 
    count=0 
    
