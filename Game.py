def easyDifficulty():
	points = 0

	print('''You have selected the easy difficulty. There will be
		no penalities for wrong answers. If you get them wrong,
		they are just wrong. The questions will all be multiple
		choice. Good luck.''')
	print('''Question 1: What are the first ten amendments
		to the Constitution called?
		A) The Ten Amendments
		B) The Bill of Rights
		C) The Articles of Confederation
		D) The Rule of Ten''')
	answer = input()

	while answer not in ('A','a','B','b','C','c','D','d'):
		print("That is an invalid choice. Please enter A, B, C, or D")
		answer = input()


	if answer == 'A' or answer == 'a':
		print("Incorrect")
	elif answer == 'B' or answer == 'b':
		print ("Correct")
		points+=1
	elif answer == 'C' or answer == 'c':
		print("Incorrect")
	else:
		print("Incorrect")

	print("Total points: {}".format(points))

	print('''Question 2: Who was the first president of the United States?
		A) Thomas Jefferson
		B) Alexander Hamilton
		C) Aaron Burr
		D) George Washington''')

	answer = input()

	while answer not in ('A','a','B','b','C','c','D','d'):
		print("That is an invalid choice. Please enter A, B, C, or D")
		answer = input()

	if answer == 'A' or answer == 'a':
		print("Incorrect")
	elif answer == 'B' or answer == 'b':
		print ("Incorrect")
	elif answer == 'C' or answer == 'c':
		print("Incorrect")
	else:
		print("Correct")
		points+=1

	print("Total points: {}".format(points))

	print('''Question 3: What reindeer was originally ridiculed but
		ended up saving Christmas?
		A) Rudolph
		B) Prancer
		C) Dancer
		D) Blitzen''')

	answer = input()

	while answer not in ('A','a','B','b','C','c','D','d'):
		print("That is an invalid choice. Please enter A, B, C, or D")
		answer = input()

	if answer == 'A' or answer == 'a':
		print ("Correct")
		points+=1
	elif answer == 'B' or answer == 'b':
		print("Incorrect")
	elif answer == 'C' or answre == 'c':
		print ("Incorrect")
	else:
		print ("Incorrect")

	print("Total points: {}".format(points))

	print('''Question 4: What mountain range travels along the eastern 
		parts of the US?
		A) The Rocky Mountains
		B) The Great Smoky Mountains
		C) The Sierra Nevada
		D) The Appalachian Mountains''')

	answer = input()

	while answer not in ('A','a','B','b','C','c','D','d'):
		print("That is an invalid choice. Please enter A, B, C, or D")
		answer = input()

	if answer == 'A' or answer == 'a':
		print("Incorrect")
	elif answer == 'B' or answer == 'b':
		print("Incorrect")
	elif answer == 'C' or answer == 'c':
		print("Incorrect")
	else:
		print("Correct")
		points+=1

	print("Total points: {}".format(points))

	print('''Question 5 In the popular video game series, what type of animal is Sonic?
		A) Hedgehog
		B) Echidna
		C) Groundhog
		D) Labradoodle''')

	answer = input()

	while answer not in ('A','a','B','b','C','c','D','d'):
		print("That is an invalid choice. Please enter A, B, C, or D")
		answer = input()

	if answer == 'A' or answer == 'a':
		print("Correct")
		points+=1
	elif answer == 'B' or answer == 'b':
		print("Incorrect")
	elif answer == 'C' or answer == 'c':
		print ("Incorrect")
	else:
		print("Incorrect")

	print("Total points: {}".format(points))

	print('''Question 6: What rock musician is often referred to as "The Boss"?
		A) Don Henley
		B) Phil Collins
		C) Bruce Springsteen
		D) Eddie Van Halen''')

	answer = input()

	while answer not in ('A','a','B','b','C','c','D','d'):
		print("That is an invalid choice. Please enter A, B, C, or D")
		answer = input()

	if answer == 'A' or answer == 'a':
		print("Incorrect")
	elif answer == 'B' or answer == 'b':
		print("Incorrect")
	elif answer == 'C' or answer == 'c':
		print("Correct")
		points+=1
	else:
		print("Incorrect")

	print("Total points: {}".format(points))

	print('''Question 7: This Looney Tunes character is famous for his catchphrase
		"What's up Doc?" Who is that character?
		A) Porky Pig
		B) Daffy Duck
		C) Yosemite Sam
		D) Bugs Bunny''')

	answer = input()

	while answer not in ('A','a','B','b','C','c','D','d'):
		print("That is an invalid choice. Please enter A, B, C, or D")
		answer = input()

	if answer == 'A' or answer == 'a':
		print("Incorrect")
	elif answer == 'B' or answer == 'b':
		print("Incorrect")
	elif answer == 'C' or answer == 'c':
		print("Incorrect")
	else:
		print("Correct")
		points+=1

	print("Total points: {}".format(points))

	print('''Question 8: The Old City of Jerusalem is divided into how many sections?
		A) Four Sections
		B) Six Sections
		C) Three Sections
		D) Five Sections''')

	answer = input()

	while answer not in ('A','a','B','b','C','c','D','d'):
		print("That is an invalid choice. Please enter A, B, C, or D")
		answer = input()

	if answer == 'A' or answer == 'a':
		print("Correct")
		points+=1
	elif answer == 'B' or answer == 'b':
		print("Incorrect")
	elif answer == 'C' or answer == 'c':
		print("Incorrect")
	else:
		print("Incorrect")

	print("Total points: {}".format(points))

	print('''Question 9: The four faces of Mount Rushmore are George Washington, Abraham Linocln,
		Teddy Roosevelt, and who else?
		A) Thomas Jefferson
		B) Alexander Hamilton
		C) John Adams
		D) Samuel Adams''')

	answer = input()

	while answer not in ('A','a','B','b','C','c','D','d'):
		print("That is an invalid choice. Please enter A, B, C, or D")
		answer = input()

	if answer == 'A' or answer == 'a':
		print("Correct")
		points+=1
	elif answer == 'B' or answer == 'b':
		print("Incorrect")
	elif answer == 'C' or answer == 'c':
		print("Incorrect")
	else:
		print("Incorrect")

	print("Total points: {}".format(points))

	print('''Question 10 will be slightly more difficult than the previous
		nine and thus will be worth more. Question 10 will be worth 3 points.''')

	print('''Question 10: Hip-hop music can trace its roots origins to the 1970s. 
		While Blondie was the first musical act to have a song featuring rapping chart at number 1, they
		were not the first ot have a rap song on the charts at all. Which rap group/artist was
		the first to achieve a rap song on the U.S. Billboard Top 40 chart?
		A) Afrika Bambaataa
		B) The Sugarhill Gabg
		C) Grandmaster Flash and the Furious Five
		D) Fab 5 Freddy''')

	answer = input()

	while answer not in ('A','a','B','b','C','c','D','d'):
		print("That is an invalid choice. Please enter A, B, C, or D")
		answer = input()

	if answer == 'A' or answer == 'a':
		print("Incorrect")
	elif answer == 'B' or answer == 'b':
		print("Correct")
		points += 3
	elif answer == 'C' or answer == 'c':
		print("Incorrect")
	else:
		print("Incorrect")

	print('''Calculating final score...
		...
		...
		...
		Final score is: {}'''.format(points))

	if points == 12:
		print("You got a perfect score!")
	elif points > 10:
		print("You scored great!")
	elif points > 6:
		print("You did a pretty good job")
	else:
		print("Better luck next time")

	print("Thank you for playing. Goodbye")

def mediumDifficulty():
	points = 0
	penalties = 0
	answer_choices = ['A','a','B','b','C','c','D','d']

	print('''You have selected the medium difficulty. Things will be different here.
			 You will once again be asked multiple choice questions, however, there is one caveat.
			 You will be penalized for every missed question and will have a limit of three penalties.
			 After three missed questions, you lose. Good luck.''')

	while penalties < 3:
		print('''Question 1: Who created the Belgian detective Hercule Poirot?
				A) Sir Arthur Conan Doyle
				B) Agatha Christie
				C) Robert Ludlum
				D) Ian Fleming ''')
		answer = input()

		while answer not in answer_choices:
			print("That is an invalid choice. Please enter A, B, C, or D")
			answer = input()

		if answer == 'A' or answer == 'a':
			print("Incorrect")
			penalties+=1
		elif answer == 'B' or answer == 'b':
			print("Correct")
			points+=1
		elif answer == 'C' or answer == 'c':
			print("Incorrect")
			penalties+=1
		else:
			print("Incorrect")
			penalties+=1

		print("Total points: {}  Total penalties: {}".format(points,penalties))

		print('''Question 2: Which European city is home to the Trevi Fountain?
				A) Rome
				B) Bern
				C) Naples
				D) Berlin ''')
		answer = input()

		while answer not in answer_choices:
			print("That is an invalid choice. Please enter A, B, C, or D")
			answer = input()

		if answer == 'A' or answer == 'a':
			print("Correct")
			points+=1
		elif answer == 'B' or answer == 'b':
			print("Incorrect")
			penalties+=1
		elif answer == 'C' or answer == 'c':
			print("Incorrect")
			penalties+=1
		else:
			print("Incorrect")
			penalties+=1

		print("Total points: {}  Total penalties: {}".format(points,penalties))

		print('''Question 3: What country does the dish Goulash originally come from?
				A) Hungary
				B) Russia
				C) Belarus
				D) Ukraine''')
		answer = input()

		while answer not in answer_choices:
			print("That is an invalid choice. Please enter A, B, C, or D")
			answer = input()

		if answer == 'A' or answer == 'a':
			print("Correct")
			points+=1
		elif answer == 'B' or answer == 'b':
			print("Incorrect")
			penalties+=1
		elif answer == 'C' or answer == 'c':
			print("Incorrect")
			penalties+=1
		else:
			print("Incorrect")
			penalties+=1

		print("Total points: {}  Total penalties: {}".format(points,penalties))
		if penalties == 3:
			break

		print('''Question 4: How many carats is pure gold?
				A) 24 carats
				B) 21 carats
				C) 15 carats
				D) 32 carats''')
		answer = input()

		while answer not in answer_choices:
			print("That is an invalid choice. Please enter A, B, C, or D.")
			answer = input()

		if answer == 'A' or answer == 'a':
			print("Correct")
			points+=1
		elif answer == 'B' or answer == 'b':
			print("Incorrect")
			penalties+=1
		elif answer == 'C' or answer == 'c':
			print("Incorrect")
			penalties+=1
		else:
			print("Incorrect")
			penalties+=1

		print("Total points: {}  Total penalties: {}".format(points,penalties))
		if penalties == 3:
			break

		print('''Question 5: In traditional occupations, what did a cooper make?
				A) Barrels
				B) Shoes
				C) Coops
				D) Crafts''')
		answer = input()

		while answer not in answer_choices:
			print("That is an invalid choice. Please enter A, B, C, or D.")
			answer = input()

		if answer == 'A' or answer == 'a':
			print("Correct")
			points+=1
		elif answer == 'B' or answer == 'b':
			print("Incorrect")
			penalties+=1
		elif answer == 'C' or answer == 'c':
			print("Incorrect")
			penalties+=1
		else:
			print("Incorrect")
			penalties+=1

		print("Total points: {}  Total penalties: {}".format(points,penalties))
		if penalties == 3:
			break

		print('''Question 6: In traditional occupations, what did a cobbler make? 
				A) Barrels
				B) Shoes
				C) Coops
				D) Crafts''')
		answer = input()

		while answer not in answer_choices:
			print("That is an invalid choice. Please enter A, B, C, or D.")
			answer = input()

		if answer == 'A' or answer == 'a':
			print("Incorrect")
			penalties+=1
		elif answer == 'B' or answer == 'b':
			print("Correct")
			points+=1
		elif answer == 'C' or answer == 'c':
			print("Incorrect")
			penalties+=1
		else:
			print("Incorrect")
			penalties+=1

		print("Total points: {}  Total penalties: {}".format(points,penalties))
		if penalties == 3:
			break;

		print('''Question 7: What was Elton John's first U.S. Number 1 hit?
				A) Crocodile Rock
				B) Your Song
				C) Goodbye Yellow Brick Road
				D) Candle in the Wind''')
		answer = input()

		while answer not in answer_choices:
			print("That is an invalid choice. Please enter A, B, C, or D")
			answer = input()

		if answer == 'A' or answer == 'a':
			print("Correct")
			points+=1
		elif answer == 'B' or answer == 'b':
			print("Incorrect")
			penalties+=1
		elif answer == 'C' or answer == 'c':
			print("Incorrect")
			penalties+=1
		else:
			print("Incorrect")
			penalties+=1

		print("Total points: {}  Total penalties: {}".format(points,penalties))
		if penalties == 3:
			break

		print('''Question 8: Which group made the albums Bare Trees and Penguin?
				A) The Moody Blues
				B) Cream
				C) Fleetwood Mac
				D) Santana''')

		answer = input()

		while answer not in answer_choices:
			print("That is an invalid choice. Please enter A, B, C, or D.")
			answer = input()

		if answer == 'A' or answer == 'a':
			print("Incorrect")
			penalties+=1
		elif answer == 'B' or answer == 'b':
			print("Incorrect")
			penalties+=1
		elif answer == 'C' or answer == 'c':
			print("Correct")
			points+=1
		else:
			print("Incorrect")
			penalties+=1

		print("Total points: {}  Total penalties: {}".format(points,penalties))
		if penalties == 3:
			break

		print('''Question  9: Where in the U.K. is actor Liam Neeson from?
				A) England
				B) Northern Ireland
				C) Scotland
				D) Wales''')
		answer = input()

		while answer not in answer_choices:
			print("That is an invalid choice. Please enter A, B, C, or D.")
			answer = input()

		if answer == 'A' or answer == 'a':
			print("Incorrect")
			penalties+=1
		elif answer == 'B' or answer == 'b':
			print("Correct")
			points+=1
		elif answer == 'C' or answer == 'c':
			print("Incorrect")
			penalties+=1
		else:
			print("Incorrect")
			penalties+=1

		print("Total points: {}  Total penalties: {}".format(points,penalties))
		if penalties == 3:
			break

		print('''Question 10 will be slightly more difficult than the previous nine and
				will thus be worth more. Question 10 will be worth 3 points''')
		print('''Question 10: All the President's Men, released in 1976 and based on the
				book of the same name, deatiled the Watergate Scandal which brought an end
				to Richard Nixon's presidency. This landmark political thriller starred
				Robert Redford and what other 1970's acclaimed actor?
				A) Al Pacino
				B) Dustin Hoffman
				C) Gene Hackman
				D) Jack Nicholson''')
		answer = input()

		while answer not in answer_choices:
			print("That is an invalid choice. Please enter A, B, C, or D.")
			answer = input()

		if answer == 'A' or answer == 'a':
			print("Incorrect")
			penalties+=1 
		elif answer == 'B' or answer == 'b':
			print("Correct")
			points+=3
		elif answer == 'C' or answer == 'c':
			print("Incorrect")
			penalties+=1
		else:
			print("Incorrect")
			penalties+=1

		print('''Calculating final score...
				...
				...
				...
				Final score is {}'''.format(points))

		if penalties == 3:
			break
		else:
			if points == 12:
				print("You got a perfect score!")
			elif points > 10:
				print("You scored great!")
			elif points > 6:
				print("You did a pretty good job")
			else:
				print("Better luck next time")

		print("Thank you for playing. Goodbye")
		break







if __name__ == '__main__':
	print('''Let's play a game. I will ask you trivia question and you must
		try and guess the correct answer. I will ask you 10 questions.
		What difficulty would you like?
		Select Easy, Medium, or Hard: ''')

	difficulty = input()

	if difficulty == "Easy":
		easyDifficulty()

	elif difficulty == "Medium":
		mediumDifficulty()









