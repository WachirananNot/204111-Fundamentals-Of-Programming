#630510642
#Wachiranan Phuangpanya
#section002
#Lab09_5

def reverse_num(num):
	L = len(str(num))-1 			#Use the letter length as the exponent.
	if num%10 == num:				##base case.
		return num
	return reverse_num(num//10)+((num%10)*(10**L)) 			#divide and conquer with combine.

def main():
    num = int(input())				#Enter the num value.
    print(reverse_num(num)) 		#Show results.
if __name__=='__main__':
    main() 