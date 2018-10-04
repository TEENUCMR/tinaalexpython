print("WELCOME TO THE GAME")
#rock paper scissores
import random
r=random.randint(1,3)
s1=0
s2=0
while True:
	p=input("PRESS R FOR ROCK ,P FOR PAPER AND S FOR SCISSORS  -")
	a=['r','p','s']
	c=random.choice(a)
	print(c)

	if(p==c):
		print("DRAW")
	elif(s1==3):
		print("SCORE-",s1)
		print("BRAVOOO! YOU WON")
		break
	elif(s2==3):
		print("SCORE-",s2)
		print("COMPUTER WINS")
		break
	elif(p=="r"):
		if(c=="s"):
			print("POINT")
			s1=s1+1
			print("SCORE-",s1)
		else:
			print("TRY AGAIN")
			s2=s2+1
			print("SCORE-",s2)
	elif(p=="p"):
		if(c=="r"):
			print("POINT")
			s1+=1
			print("SCORE-",s1)
		else:
			print("TRY AGAIN")
			s2+=1
			print("SCORE-",s2)
	elif(p=="s"):
		if(c=="p"):
			print("POINT")
			s1+=1
			print("SCORE-",s1)
		else:
			print("TRY AGAIN")
			s2+=1
			print("SCORE-",s2)

	



	



