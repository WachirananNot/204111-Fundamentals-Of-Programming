#630510642
#Wachiranan Phuangpanya
#section002
#Lab11_1
import copy
def matrix_mult(m1,m2):
	a = copy.deepcopy(m1) #Copy list m1
	b = copy.deepcopy(m2) #Copy list m2
	c = []			#Create an empty list.
	d = [] 		
	if len(a[0]) == len(b): 	#If a matrix can be multiplied.
		for i in range(len(a)): 		#Create loops in matrix multiplication.
			c = []
			for j in range(len(b[0])):
				f = 0
				for k in range(len(b)):
					f += a[i][k]*b[k][j]
					continue
				c.append(f)
			d.append(c)
		return d


	else:				#If the matrix cannot be multiplied.
		return None



def main():
	x = [[1,2,3],		#list m1
	     [4,5,6]]
	y = [[7,8],			#list m2
	     [9,10],
	     [11,12]]
	print(matrix_mult(x,y)) 	#Show results.

if __name__=='__main__':
	main()