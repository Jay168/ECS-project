'''
def func_name():
	#do the activity here


'''

# creating a calculator for computing addition, subtraction, multiplication, division

def addition(x,y):
	add = x+y
	print add
print "step1"
def subtraction(x,y):
	sub = x-y
	print sub
print "step2"
def multiplication(x,y):
	prod = x*y
	print prod
print "step3"
def division(x,y):
	quo = x/y
	print quo
print "step4"
def remainder(x,y):
	rem = x%y
	print rem
print "step4"
def square(x):
	sq = x*x
	print sqw
	
# call a function

# addition()
# subtraction()
# multiplication()
# division()
# remainder()
# square()

choice=raw_input("please enter your choice \n1.add\n2.sub\n3.multiply\n4.divide\n5.remainder\n6.square\n")
a=int(raw_input("please enter the first number:"))
b=int(raw_input("please enter the second number:"))
if (choice=='1'): 
	addition(a,b)
elif (choice=='2'):
	subtraction(a,b)
elif (choice=='3'):
	multiplication(a,b)
elif (choice=='4'):
	division(a,b)
elif (choice=='5'):
	remainder(a,b)
elif (choice=='6'):
	square(a)
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
