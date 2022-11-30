#630510642
#Wachiranan Phuangpanya
#section002
#Lab07_EX1

def xmas_tree(x):
	s = ' '     	#Variables instead of spaces.
	u = '_'			#Variables instead of underscore.
	under = (x+3)*u 	#Underscore variable.
	line = '|||' 		#Tree base.
	space = 4+x 		#Number of spacing times.
	space_2 = 2+x 		#Number of spacing times.
	space_3 = 3+x 		#Number of spacing times.
	dot = '* '  		#Storage variable *.
	Asn = str() 		#The variable holds the text value.
	Asn += '\n' 			#Collect the tree tops.
	Asn+=(s*space+'|\n')  		#Collect the tree tops.
	Asn+=(s*space_2+'--*--\n')  #Collect the tree tops.
	Asn+=(s*space_3+'/|\\\n') 	#Collect the tree tops.
	Asn+=(s*space_2+'/* *\\\n')   #Collect the tree tops.
	for i in range(1,x+1):   		#Loop to hold up the tree layer by layer.
		for j in range(i,i+3): 		#Loop to hold up the tree layer by layer.
			Asn += (((x+2)-j)*s+'/* ')
			Asn += (dot*j)
			Asn += ('*\\')
			Asn +=('\n')
	Asn += ((x+3)*s+'|||\n')   		#Collect the tree base.
	Asn += (''+under+line+under)	#Collect the tree base.
	return Asn 					#Return variable.



def main():
	x = int(input()) 			#Fill in the number of layers.
	print(xmas_tree(x)) 		#Print function.

	

if __name__=='__main__':
	main()