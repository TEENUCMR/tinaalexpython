l=input("DECODE OR CODE?....press d for decode and c for code")




alpha="abcdefghijklmnopqrstuvwxyz"
key=3
newmsg=''


def code():
	msg=input("enter the message you want to convey ^_^....  ")
	for character in msg:
		if character in alpha:
			posi=alpha.find(character)
			nposi=(posi+key)%26
			newcar=alpha[nposi]
			newmsg+=newcar
		else:
			newmsg+=character

	print('your secret message is...',newmsg)



def decode():
	msg=input("enter the message you want to convey ^_^....  ")
	for character in msg:
		if character in alpha:
			posi=alpha.find(character)
			nposi=(posi-key)%26
			newcar=alpha[nposi]
			newmsg+=newcar
		else:
			newmsg+=character

	print('your secret message is...',newmsg)




if(l=='c'):
	code()
elif(l=='d'):
	decode()
else:
	print("wrong key")
	exit()







