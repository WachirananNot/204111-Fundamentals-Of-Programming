#630510642
#Wachiranan Phuangpanya
#section002
#Lab07_EX2

def pyramid_stairs(n):
	for i in range(1,n+1): 	#Number of steps loops.
		for j in range(1,5):  		#What loops to print at each stage.
			if i == n: 				#Print the manpower and the service level correctly.
				if j == 1:
					print('  o  '+'*'*6+(' '*((i-1)*10)+('*'*6))+'  o')
				elif j == 4:
					print('*'*((i*10)+12))
				elif j == 2:
					print(' /|\\ '+'*'+(' '*(i*10)+'*'+' /|\\'))
				elif j == 3:
					print(' / \\ '+'*'+(' '*(i*10)+'*'+' / \\'))
			elif i == 1: 				#Print the manpower and the service level correctly.
				if j == 1:
					print(' '*(5*(n-i))+'  o  '+'*'*((i*10)+2)+'  o')
				elif j == 4:
					print('',end='')
				elif j == 2:
					print(' '*(5*(n-i))+' /|\\ '+'*'+(' '*(i*10)+'*'+' /|\\'))
				elif j == 3:
					print(' '*(5*(n-i))+' / \\ '+'*'+(' '*(i*10)+'*'+' / \\'))
			else: 						#Print the manpower and the service level correctly.
				if j == 1:
					print(' '*(5*(n-i))+'  o  '+'*'*6+(' '*((i-1)*10)+('*'*6))+'  o')
				elif j == 4:
					print('',end='')
				elif j == 2:
					print(' '*(5*(n-i))+' /|\\ '+'*'+(' '*(i*10)+'*'+' /|\\'))
				elif j == 3:
					print(' '*(5*(n-i))+' / \\ '+'*'+(' '*(i*10)+'*'+' / \\'))

		



def main():
	x = int(input()) 			#Enter the number of steps.
	pyramid_stairs(x)
	main() 			#Call function.
	
if __name__=='__main__':
	main()