#630510642
#Wachiranan Phuangpanya
#section002
#Lab08_1

import string
def square_frame(n,sep=' '):
	list_ = []  			#Create a blank list.
	sq = (n**2)-((n-2)**2) 	#The equation for the number entered in the frame.
	for k in range(1,sq+1): 	#Loops add numbers to the list.
	 	if k < 10:
	 		list_.append("0"+(str(k)))
	 	else:
	 		list_.append(str(k))

	for i in range(1,n+1):       	#Line loops to draw a frame.
		for j in range(1,n+1): 		#Loop of the printed stuff on each line.
			if j == n:
				print(list_[n+(i-2)],end='')
			elif 1 < i <n :
				print(list_[-i+1]+sep*((2*n)+(n-1)-4),end=list_[n+(i-2)])
				break
			elif i==1:
				print(list_[j-i],end=sep)
			elif i==n:
				print(list_[(-i+1)-(j-1)],end=sep)
			
		print() 				#Start a new line.
			
def main():
	x = int(input()) 			#Enter n values.
	y = input() 				#Enter sep value.
	square_frame(x,y)     		#Call function.

if __name__ == '__main__':
	main()

