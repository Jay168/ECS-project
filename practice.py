#practice 1
def balance(x):
	y=100-x
	return y
	
import datetime
now=datetime.datetime.now()
year=now.year
age=input("What is your current age ?\n")
bal=balance(age)
centenary=year+bal
if (centenary > year):
	print "You will be 100 yrs old by",centenary
else:
	print "You were 100 yrs old by",centenary
	

