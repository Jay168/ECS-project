#lists

'''
list_name=[]

'''

groceries = ['Daal','Rice','Sambar masala',1,2.5,'100 gms']
print groceries

#list slicing
print groceries[0:3]
print groceries[2:5]

#accessing list using while
i=len(groceries)-1
while i>=0:
	print groceries[i]
	i=i-1

#accessing list using for loop

for element in groceries:
	print element
	
#print numbers from 1 to 50 using for loop
for i in range (0,51):
	print i

for idx,i in enumerate(range(100,111)):
	print (idx,i)
	
#create 2 lists of same size
#name the first list gro name the second as weights
#finally print the gro's and their associated weights
# new1=['rice','sambar','daal']
# new2=[10,'100gms',10]
# for gro,weights in enumerate(new1,new2)
# print gro,weights

lis1=[1,2,3,4,5,6]
lis2=[1,0,3,5,4,6]
final_list=[]
for idx,i in enumerate(lis1):
	if i == lis2[idx]:
		final_list.append(True)
	else:
		final_list.append(False)

print final_list