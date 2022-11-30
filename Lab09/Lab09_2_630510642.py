#630510642
#Wachiranan Phuangpanya
#section002
#Lab09_2

def n_base_to_10(n,num):
	L = len(str(num))-1 		#Use the letter length as the exponent.
	if num%(10**L) == num:
		return num				#base case
	return (n_base_to_10(n,num%(10**L)))+(((num//(10**L)))*(n**L))  #divide and conquer with combine.

def main():
	x = int(input())				#Enter the x value.
	y = int(input())				#Enter the y value.
	print(n_base_to_10(x,y)) 		#Show results

if __name__=='__main__':
    main() 
