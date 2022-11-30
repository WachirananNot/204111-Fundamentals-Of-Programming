#630510642
#Wachiranan Phuangpanya
#section002
#Lab10_1

import string
def is_anagram(str1,str2):
	str1 = str1.lower()
	str2 = str2.lower()			#Change the letter to lowercase.
	for i in str1: 				#Loops to cut out spaces.
		if i not in string.ascii_letters:
			str1 = str1.replace(i,'')
		else:
			str1 = str1
	for j in str2: 				#Loops to cut out spaces.
		if j not in string.ascii_letters:
			str2 = str2.replace(j,'')
		else:
			str2 = str2
	if sorted(str1)==sorted(str2): 		#Compare letters.
		return True
	else:
		return False

def main():
	str1 = input()			#Word input.
	str2 = input() 			#Word input.
	print(is_anagram(str1,str2))		#Print results.

if __name__=='__main__':
	main()