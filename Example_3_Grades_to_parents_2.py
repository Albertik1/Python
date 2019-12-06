score=32
maxpts=64

# calculate percentage
percentage = score / maxpts * 100
percentage = round(percentage)

# Create message template
message = """Hello WHO!
We had a test recently, i got POINTS/MAX, which is PERC%! 
I hope you are happy with my results.
Love & kisses from your ME."""

# Replace result
message = message.replace("POINTS", str(score)).replace("MAX", str(maxpts)).replace("PERC", str(percentage))

# Message specific for parents
messageToParents = message
messageToParents = messageToParents.replace("WHO", "Mom & Dad").replace("ME", "son")
print(messageToParents)

# Message specific for parents
messageToGrandParents = message
messageToGrandParents = messageToGrandParents.replace("WHO", "Grandparents").replace("ME", "grandson")
# Just some blank line to separate the messages
print()
print()
print(messageToGrandParents.upper())
