#630510642
#Wachiranan Phuangpanya
#section002
#Lab09_3

def is_prime(n):
	y = n 			#Keep the n values ​​in the y variable.
	def find(n,y): 	#Create an additional function to use y as the divisor.
		if y == 1:
			return True 		#If the denominator is 1, returns True.
		else:
			return n%y!=0 and find(n,y-1) 		#Compare 2 cases In other cases it is a recursive function. Both must be true in order to return True.
	return find(n,int(n**0.5))		#Decrease the denominator value



def main():
	x = int(input())	 		#Enter the x value.
	print(is_prime(x))			#Show results.


if __name__=='__main__':
    main() 
