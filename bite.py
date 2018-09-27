#snake and ladder
print("LETS START THE GAME!")
import random
count=0
while True:
	x=input("TO ROLL THE DICE PRESS R  ")
	r=random.randint(1,6)
	count=count+r
	print("DICE",r)
	print(count)

	if(count>100):
		print("YOUR SCORE IS GREATER THAN 100..TRY AGAIN!")
		count=count-r
	elif(count==100):
		print("CONGRATS!.. YOU WON!!")
		break
	elif(count==8):
		count=37
		print("ITS A LADDER GO UP!  ",count)
	elif(count==11):
		count=2
		print("YOU GOT BIT! GO DOWN..",count)
	elif(count==13):
		count=34
		print("ITS A LADDER GO UP!  ",count)
	elif(count==25):
		count=4
		print("YOU GOT BIT! GO DOWN..",count)
	elif(count==38):
		count=9
		print("YOU GOT BIT! GO DOWN..",count)
	elif(count==40):
		count=68
		print("ITS A LADDER GO UP!  ",count)
	elif(count==52):
		count=81
		print("ITS A LADDER GO UP!  ",count)
	elif(count==65):
		count=46
		print("YOU GOT BIT! GO DOWN..",count)
	elif(count==76):
		count=97
		print("ITS A LADDER GO UP!  ",count)
	elif(count==89):
		count=70
		print("YOU GOT BIT! GO DOWN..",count)
	elif(count==93):
		count=64
		print("YOU GOT BIT! GO DOWN..",count)
	

   





