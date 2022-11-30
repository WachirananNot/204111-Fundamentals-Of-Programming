#630510642
#Wachiranan Phuangpanya
#section002
#Lab08_5

import string
def decode(code_table,text):
	c = code_table
	len_c = len(c) 		#Character length of code_table.
	t = text
	t_n = t.replace('\n',' \n ')  #Insert a space before and after of \n.
	t2 = t_n.split(' ')  #Cut gap.
	for j in t2: 	#The loop runs a text value without spaces and \ n.
		if j == '\n':
			print()
		elif j == '':
			continue
		else:
			for i in c:  	#The loop runs the value in code_table.
				int_=c.find(i) 	#Find the location of i.
				str_=str(c.find(i))  	#Change the element of i to str.
				if int(j) == int_: 		#If j-value is equal to the position of i, print the i-value.
					print(i,end='')
				elif int(j) >= len_c or int(j) < 0: 	#If the value j is greater than the length of the text Or less than 0, print _.
					print('_',end='') 
					break



def main():
	x = input() 		#Enter a code_table value.
	y = input() 	 	#Enter a text value.
	decode(x,y) 		#Call function.

if __name__ == '__main__':
	main()



		


