#630510642
#Wachiranan Phuangpanya
#section002
#Lab13_4

import string
def square_matrix(list_x):
	x = [len(i) for i in list_x]
	x.append(len(list_x))
	x = max(x)
	
	if x > len(list_x):
		for i in range(x-len(list_x)):
			emp = []
			for j in range(x-len(list_x)):
				emp.append(0)
			list_x.append(emp)
	for i in list_x:
		for j in range(x-len(i)):
			i.append(0)
	

def main():
	list_x = [[2, 3, 4,5,6],[1, 2, 3]]
	print(square_matrix(list_x))

	

if __name__ =='__main__':
	main()