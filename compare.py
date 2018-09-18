a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))
#comparing 3 values
if(a>b & a>c):
	print(a,"is greater")
elif(b>c & b>a):
	print(b,"is greater")
elif(c>a & c>b):
	print(c,"is greater")
