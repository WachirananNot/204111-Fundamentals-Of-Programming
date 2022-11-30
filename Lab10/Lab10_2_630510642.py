#630510642
#Wachiranan Phuangpanya
#section002
#Lab10_2

def classify(list_x):
	list_a = []
	list_b = []
	list_c = []				#Create empty lists.
	for i in list_x: 			#Create a loop to check the types.
		if isinstance(i,int):
			list_a.append(i)
		elif isinstance(i,float):
			list_b.append(i)
		elif isinstance(i,str):
			list_c.append(i)
	x = (list_a,list_b,list_c)
	return x 		#Returns the value to Tuples.

def main():
	list_x = [10,1.1,'1.2',200,'hello',23.5,4]
	a,b,c = classify(list_x)
	print(a)
	print(b)
	print(c) 			#Print results.

if __name__=='__main__':
	main()