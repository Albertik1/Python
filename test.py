mylist = range(101)
x = int(input())
for x in mylist:
	factors = []
	for factor in range(2, 11):
		if x % factor == 0:
			factors.append(factor)
	print(x, "can be divided by", factors)

print()

odd = range(1,14,2)
even = range(10,-7,-2)
for a in odd:
	for b in even:
		print(a,b)
	print("-------------")

odd = range(1,14,2)
even = range(10,-7,-2)
for a in odd:
	for b in even:
		if a*a >= b**2:
			print(a,b)
	print("-------------")
	
#Create a list of 20 random numbers
import random
arbitList = []
for i in range(20):
	arbitList.append(random.randrange(100))
print("Arbitrary list:", arbitList)
average = sum(arbitList) / len(arbitList)

overAvg = 0
for i in arbitList:
	if i > average:
		overAvg += 1
print ("List average:", average)
print("Over average count:", overAvg)

#Preview for next time 
avg = sum(arbitList) / len(arbitList)
overAvg = len([i for i in arbitList 
	if i > avg])
print(overAvg)
