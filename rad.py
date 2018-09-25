import random
#roll a dice
while True:
	a=input("Enter 'r' to roll the dice and press 'q' to quit  ")
	if(a=="r"):
		r=random.randint(1,6)
		print(r)
	else:
		print("BYE!")
		break
