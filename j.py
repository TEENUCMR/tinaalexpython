alpha="abcdefghijklmnopqrstuvwxyz"
key=3
newmsg=''



msg=input("enter the message you want to convey ^_^....  ")
for character in msg:
	if character in alpha:
		posi=alpha.find(character)
		nposi=(posi-key)%26
		newcar=alpha[nposi]
		newmsg+=newcar
	else:
		newmsg+=character

print("your secret message is...",newmsg)

