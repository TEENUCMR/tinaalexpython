a=['1','2','3','4','5','6','7','8','9']
#tictaktoo
def game():
	print("-------------------")
	print("|",a[0],"|",a[1],"|",a[2],"|")
	print("-------------------")
	print("|",a[3],"|",a[4],"|",a[5],"|")
	print("-------------------")
	print("|",a[6],"|",a[7],"|",a[8],"|")
	print("-------------------")

p1=True
while True:
	game()
	p=input("CHOOSE A LOCATION--")
	if(p in a):
		if(a[int(p)-1]=='X' or a[int(p)-1]=='O'):
	 		print("LOCATION TAKEN TRY AGAIN!")
	 		continue 
		else:
	 		if p1:
	 			print("player 1 >>>>")
	 			a[int(p)-1]='X'
	 			p1=not p1
	 		else:
	 			print("player 2 >>>>")
	 			a[int(p)-1]='O'
	 			p1= not p1
	 		for i in(0,3,6):
	 			if(a[i]==a[i+1]and a[i]==a[i+2]):
	 				print("game over")
	 				exit()
	 		for i in range(3):
	 			if(a[i]==a[i+3] and a[i]==a[i+6]):
	 				print("game over")
	 				exit()
	 		
	 		if(a[0]==a[4] and a[0]==a[8]):
	 			print("game over")
	 			exit()

	 		if(a[2]==a[4] and a[2]==[6]):
	 			print("game over")
	 			exit()

			
			


	if(p not in a):
		print("INVALID KEY")
		continue
	else:
		print("tie")
		


