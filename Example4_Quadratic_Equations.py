import math
a = 1
b = 4
c = 0
d = (b**2) - (4*a*c)
print ("d = ", d)
root = math.sqrt(d)
print ("Root(d) = ", root)

if d==0:
	print ("One solution")
	x = -b / (2*a)
	print ("X = ", x)
elif d>0:
	print ("Two solutions")
	x1 = ((-b) + root) / (2*a)
	x2 = ((-b) - root) / (2*a)
	print ("X1 = ", x1)
	print ("X2 = ", x2)
elif d<0:
	print ("0 solution")
