a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))
#comparing 3 values
if(a>b and a>c):
	print(a,"is greater")
elif(b>c and b>a):
	print(b,"is greater")
else:
	print(c,"is greater")
