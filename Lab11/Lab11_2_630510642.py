#630510642
#Wachiranan Phuangpanya
#section002
#Lab11_2

import copy
def remove_row_col(list_a,row,col):
	a = copy.deepcopy(list_a)  		#copy list_a
	if col < 0: 			#Primary case less than 0
		if abs(col) <= len(a[0]): 		#If the principal value is less than the length of the matrix.
			for i in range(len(a)): 	#Create loops to cut numbers.
				for j in range(len(a[i])):
					del a[i][col]
					break
	elif col >= 0 and col <= len(a[0])-1: 	#Primary case greater than 0.
			for i in range(len(a)):		#Create loops to cut numbers.
				for j in range(len(a[i])):
					del a[i][col]
					break
	if row < 0: 		#If row is less than 0.
		if abs(row) <= len(a):	
			del a[row]		#Cut out numbers.
	elif row >= 0 and row <= len(a)-1: 		#If row is greater than 0.
			del a[row] 		#Cut out numbers.
	return a





def main():
	list_a = [[2,3,4,5],[8,7,6,5],[0,1,2,3]]  #list_a
	row = int(input()) 	#input row
	col = int(input())	#input col
	print(remove_row_col(list_a,row,col)) 	#Show results.
 
if __name__ =='__main__':
	main()
