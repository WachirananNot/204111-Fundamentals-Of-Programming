#630510642
#Wachiranan Phuangpanya
#section002
#Lab10_3

def nondest_rotate_list(list_a, n):
	list_ro = []
	list_a2 = []   			#Create empty lists.
	list_a2.extend(list_a)
	list_ro.extend(list_a)	#copy list_a into blank list.
	le = len(list_a)
	mo = abs(n)%le
	sl = le - (abs(n)%le)
	if n >= 0: 				#Positive case.
		del list_a2[:sl]
		del list_ro[sl:]
		list_a2.extend(list_ro)
		return list_a2 			#Move the number and return it.
	else: 					#Case minus.
		del list_a2[mo:]
		del list_ro[mo-1::-1]
		list_ro.extend(list_a2)
		return list_ro			#Move the number and return it.

def main():
	list_a = [1,2,3,4,5]
	n = int(input()) 				#Enter the number of times the number has been shifted.
	print(nondest_rotate_list(list_a,n)) 	#Print results.

if __name__=='__main__':
	main() 