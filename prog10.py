'''
def func_name():
	#do the activity here


'''

# creating a calculator for computing addition, subtraction, multiplication, division

def addition(x):
	y,z=x
	print y+z
print "step1"
def subtraction(x):
	y,z=x
	print y-z
print "step2"
def multiplication(x):
	y,z=x
	print y*z
print "step3"
def division(x):
	y,z=x
	print y/z
print "step4"
def remainder(x):
	y,z=x
	print y%z
print "step4"
def square(x):
	sq = x*x
	print sq
def user_input():
	if (choice!='6'):
		a=int(raw_input("please enter the first number:"))
		b=int(raw_input("please enter the second number:"))
		return a,b
	else:
		a=int(raw_input("please enter the number:"))
		return a
	
# call a function

# addition()
# subtraction()
# multiplication()
# division()
# remainder()
# square()
while True:
	choice=raw_input("please enter your choice \n1.add\n2.sub\n3.multiply\n4.divide\n5.remainder\n6.square\n7.exit\n")
	if (choice=='1'): 
		addition(user_input())
	elif (choice=='2'):
		subtraction(user_input())
	elif (choice=='3'):
		multiplication(user_input())
	elif (choice=='4'):
		division(user_input())
	elif (choice=='5'):
		remainder(user_input())
	elif (choice=='6'):
		square(user_input())
	elif (choice=='7'):
		break
	else:
		print "give correct input"

'''
30
10
200
2
0
100
'''
