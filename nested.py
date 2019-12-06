numbers = range(100)

# Enumerating all elements
for i in numbers:
	print(i)

# Calculating some formula for each element
for i in numbers:
	print( (i - 6) * 5)

# Calculating some list invariant - average, maximum, minimum...
sumOfNumbers = 0
for i in numbers:
	sumOfNumbers += i
print("average is", sumOfNumbers / len(numbers))

maximum = numbers[0]
for i in numbers:
	if i > maximum:
		maximum = i
print("Maximum is", maximum)
#You can try product etc....

# Verifying if array has an element that satifies certain condition
for i in numbers:
	if i % 2 == 1:
		print("There is an odd number!!!", i)

# Filtering the array - creating a new array with some elements removed
filtered = []
for i in numbers:
	if i > 30:
		filtered.append(i)
print("Filtered:",filtered)

# Mapping the array - creating a new array with elements processed by
# some function (e.g., x2)
mapped = []
for i in numbers:
	mapped.append(-i)
print("Mapped", mapped)
