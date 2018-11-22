'''class D:
	x=int(input("ENTER YOUR USN  "))
	y=input("ENTER YOUR NAME ")

	def hey(ob):
		print(ob.x,ob.y)
p=D()
p.hey()'''


'''f=open("dl2.txt","r")
print(f.read())'''
#IT IS USED TO READ THE FILE


'''f=open("dl2.txt",'a')
print(f.write("HOW ARE YOU?"))'''
# IT WILL CONTINUE WRITING IF WE USE APPEND
f=open("dl2.txt","w")
f.write("BYE")
#IT WILL OVERWRITE IF WE USE WRITE
f=open("dl2.txt","r")
print(f.read())





