#630510642
#Wachiranan Phuangpanya
#section002
#Lab10_4

def dest_rotate_list(list_a,n):
	le = len(list_a)
	mo = abs(n)%le
	if n<0:					#Positive case.
		for i in range(mo): 			#Create loops to move numbers.
			list_a.append(list_a[0])
			del list_a[0]
	else:					#Case minus.
		for i in range(mo): 			#Create loops to move numbers.
			list_a.extend(list_a[0:le])
			del list_a[0:le-1]
			del list_a[-1]


			

def main():
	list_a = [1,2,3,4]
	n = int(input()) 				#Enter the number of times the number has been shifted.
	dest_rotate_list(list_a,n) 		#Call function.
	print(list_a)					#Print a list that has been shifted numbers.

if __name__=='__main__':
	main() 