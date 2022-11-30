#630510642
#Wachiranan Phuangpanya
#section002
#Lab09_4

def series(n):
	if n <= 1: 			#base case.
		return n   
	else:				#divide and conquer with combine.
	    if n%2==0:
	    	return (2*series(n-1))+1
	    else:
	    	return (2*series(n-1))-1

def main():
    n = int(input())			#Enter the n value.
    print(series(n)) 			#Show results.
if __name__=='__main__':
    main() 