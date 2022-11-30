#630510642
#Wachiranan Phuangpanya
#section002
#Lab08_3

import string
def patterned_message(message,pattern):
	a = message
	a_back = a.replace(' ','') 		#Remove spaces.
	a_plus = a_back 				#Keep old values.
	b = pattern
	c = '' 							#The variable holds the literal value.
	for i in b: 					#Loops run in pattern.
		if i =='\n':				#If encountered \n
			c += '\n' 				
			continue 				
		else:
			for j in a_plus: 		#The loop runs on a value in a message with no spaces removed.
				if i == ' ': 		#If the loop runs with a gap, print the space.
					c += ' '
					if a_plus=='':  	#If there are no characters left in a_plus, return a_back.
						a_plus = a_back
					break
				else:
					c += i.replace(i,j) 	#Substitute j for i and store it in variable c. And move a_plus to 1 position.
					a_plus = a_plus[1:]
					if a_plus=='':
						a_plus = a_back 	##If there are no characters left in a_plus, return a_back.
					break
			
	print(c)



def main():
	x = input()   				#Enter the message value.
	y = input()	 				#Enter the pattern value.
	patterned_message(x,y) 		#Call function.

if __name__=='__main__':
	main()