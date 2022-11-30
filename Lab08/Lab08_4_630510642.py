#630510642
#Wachiranan Phuangpanya
#section002
#Lab08_4

import string
def uniform(line):
	up_count = 0 		#The variable holds the value of uppercase letters.
	low_count = 0		#The variable holds the value of lowercase letters.
	re = '' 			#The variable holds the literal value.
	for i in line: 		#Loops for counting letter sizes.
		if i.islower():
			low_count += 1
		elif i.isupper():
			up_count += 1
		else:
			low_count = low_count
			up_count = up_count
	if up_count > low_count: 	#Use the number to compare to change the font size.
		line = line.upper()
	elif up_count < low_count:
		line = line.lower()
	else:
		if line[0].isupper():
			line = line.upper()
		else:
			line = line.lower()
	return line 		#Return variable.


def main():
	x = input() 		#Enter line value.
	print(uniform(x)) 	#Print function values.

if __name__=='__main__':
	main()