# Rock Paper Sissors
import random

pScore = 0
cScore = 0
ties = 0
computerChoices = ["r" , "s" , "p"]



print("wELCOME TO rOCK PAPER sISSORES")
pName = input("What is your name?")

def printScore():
	print("The Score is: ")
	print(pName + " : " + str(pScore))
	print("Computer:" + str(cScore))
	print("ties: " + str(ties))
while True:
	printScore()
	pChoice = input("Enter r , p , s or q for quit")
	if pChoice == "q":
		break
	cChoice = random.choice(computerChoices)
	if pChoice == "r":
		if cChoice == "r":
			print("Computer picked rock")
			print("tie")
			ties = ties + 1

		elif pChoice == "p":
	 		print("com picked paper you lose")
	 		print("HAHAHA")
	 		cScore = cScore + 1



		elif pChoice == "s":
	 		print("com picked paper you lose")
			print("HAHAHA")
			cScore = cScore + 1


		else:
			print("sissors")
			print("noooo")
			pScore = pScore + 1


	elif pChoice == "p":
		pass
	elif pChoice == "s":
		pass
	elif pChoice == "q":
		break




