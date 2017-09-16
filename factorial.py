while True:
	try:
		inp=int(input("Enter a number\t"))
		result=1
		while inp > 1:
			result=result*inp
			inp=inp-1
		print result	
	except NameError:
		print("illegal characters found")