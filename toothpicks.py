import random
toothpicks = int(input("How many toothpicks to start with? "))
onTurn = 0
while toothpicks > 0:
	if onTurn == 1:
		toTake = random.randint(1, min(3, toothpicks))
		print("Computer took", toTake, "toothpicks")
	else:
		message = "Player " + str(onTurn + 1)+ " on turn, " + str(toothpicks) + " toothpicks remain. How many to take? "
		toTake = int(input(message))
		if toTake > 3 or toTake > toothpicks or toTake < 1:
			print("Invalid turn.")
			continue
	toothpicks -= toTake
	onTurn = (onTurn + 1) % 2
print("That was the last toothpick! Player", onTurn + 1, "wins!")
