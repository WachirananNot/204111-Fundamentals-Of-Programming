#630510642
#Wachiranan Phuangpanya
#section002
#Lab09_1

def gcd(x,y):
	if y == 0:
		return x   			#If the divisor is 0.
	else:
		return gcd(y,x%y)	#divide and conquer with combine.
		
def main():
	x = int(input()) 		#Enter the x value.
	y = int(input())		#Enter the y value.
	print(gcd(x,y))			#Show results

if __name__=='__main__':
    main() 
