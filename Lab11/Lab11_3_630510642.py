#630510642
#Wachiranan Phuangpanya
#section002
#Lab11_3
import copy
def is_magic_square(board):
	sum_1 = []
	sum_2 = []
	sum_3 = 0
	sum_4 = 0
	sum_5 = []
	for i in range(len(board)): 	#Put all the numbers in a new list.
		for j in board[i]:
			sum_5.append(j)

	for i in range(len(sum_5)): 		#Compare each number in the list.
		for j in sum_5[i+1:]:

			if j > (len(board))**2:
				return False
			elif sum_5[i] == j:
				return False
			else:
				continue
	for i in range(len(board)): 		#Create a horizontal total list.
			sum_1.append(sum(board[i]))
	for j in range(len(board[0])): 		#Create a list of vertical totals.
		sumV2 = 0
		for k in range(len(board)):
			sumV2 += board[k][j]
		sum_2.append(sumV2)
	for i in range(len(board)): 		#Create a diagonal list of totals.
		sum_3 += board[i][(len(board)-1)-i]
		sum_4 += board[i][i]

	for i in sum_1: 					#Compare grand totals.
		for j in sum_2:
			if i == j == sum_3 == sum_4:
				continue
			else:
				return False
	return True
	



def main():
	board = [[3, 8, 7],[10, 6, 2],[5, 4, 9]] 	#list
	print(is_magic_square(board)) 			#Show results.

if __name__=='__main__':
	main()