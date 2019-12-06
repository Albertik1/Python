maxpts = 32
score = 24
percentage = round(score / maxpts * 100)
grade = round(6-score / maxpts*5)
# If you want to display character instead of number, use this 
grade = chr(64 + grade)
# If yuou want to extend the expression on multiple lines, use ()
message = ("Dear Parents!\nWe had a test. I got " 
+ str(score) + "/" + str(maxpts) + ", which is " 
+ str(percentage) + "%, namely grade " + str(grade) 
+ ". Hope yo are happy.\nLove, your son")
print(message)
print()
print()
# For grandparents, you can use the same message ( no need to write again), just change
# some words with the replace() method and make it uppercase (easier to read :)
print(message.replace("Parents", "Grandparents").replace("son", "grandson").upper())
