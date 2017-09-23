#swapping variables without using temporary variables

def swapping(x,y):
	x=x+y
	y=x-y
	x=x-y
	return x,y

a=input("input the first number A:\n")
b=input("input the second number B:\n")
a,b=swapping(a,b)
print "The value of A after swapping is:",a
print "The value of B after swapping is:",b
