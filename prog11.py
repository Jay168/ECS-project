'''
while (condition):
	do the action
	
	update condition
'''

# i=10
# while i>0:
		# print " Jai ",i
		# i=i-1
	
	
# write a program to find if a person can marry
# conditions for male - age limit - 21
# conditions for female - age limit - 18

	
while True:
	gender = raw_input(" Give gender \t")
	age = int(input(" Give age \t"))
	# gender =' '.join(gender.split())
	if (gender == 'Male' or 'male' and age >= 21) :
			print "Congratulations you can marry"
	elif (gender == 'Male' or 'male' and age < 21) :
			print "We regret to inform you cannot marry"
	elif (gender == "Female" or "female" and age >= 18) :
			print "Congratulations you can marry"
	elif (gender == "Female" or "female" and age < 18) :
			print "We regret to inform you cannot marry"
	else:
			print "Gender or age mismatch"
			
