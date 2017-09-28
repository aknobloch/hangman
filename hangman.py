import re

# Food (answer = cereal)
# word = "*e*ea*"
# guessed = ['b','d','f','g','i','s','y']

# Animal (answer = elephant)
# word = "*l*ph**t"
# guessed = ['c','d','f','g','i','k','o','s']

# Fun and games
word = "c*e**"
guessed = ['a','b','g','j','k','l','o','r']

length = len(word)
word = word.replace("*", "\\w")
regex = re.compile(word, re.IGNORECASE)

dictionary = open("words.txt")
for line in dictionary :

	if regex.match(line) :

		contained = False

		for word in line :

			if(word in guessed) :
				contained = True

		if not contained and len(line.strip()) == length:

			print line