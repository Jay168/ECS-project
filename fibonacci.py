def fibonacci(x):
	i=0
	a=-1
	b=1
	c=0
	print "The first ",x," fibonacci numbers are"
	while (i <= x ):
		c=a+b
		print c
		a=b
		b=c
		i=i+1
n=input("Enter the number of fibonacci  numbers to be displayed\n")
fibonacci(n)	
	