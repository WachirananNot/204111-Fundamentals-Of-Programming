#630510642
#Wachiranan Phuangpanya
#section002
#Lab11_4
import copy
def sum_nested_list(list_a):
	b = copy.deepcopy(list_a)   #copy list_a
	for i in b: 		#Looping to extend list back into the original list.
		if isinstance(i,list):
			while isinstance(i,list):
				b.extend(i)
				break
	while True:		
		try:
			b = sum(b) 			#Number combination trial.
			return b 			#If total is possible, return the sum.
		except TypeError:
			for j in b: 		#If TypeError, loop delete the list.
				if isinstance(j,list):
					b.remove(j)
					continue





def main():
	list_a = [1, 2, [[2, [[145], 34]], [48, 22]]]  #list_a
	print(sum_nested_list(list_a))			#Show results.
if __name__=='__main__':
	main()