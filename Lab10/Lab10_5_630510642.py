#630510642
#Wachiranan Phuangpanya
#section002
#Lab10_5

def three_digits_to_word(n):
	#list words 1-19
	list_1 = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
	#list Ten digits.
	list_10 = ['','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
	y1k,n = divmod(n,1000)
	y100,n = divmod(n,100)
	x10,x1 = divmod(n,10)
	if 0<y100 and x10 == 0 and x1 == 0: 	#The case of a hundred integers.
		return list_1[y100]+' hundred'
	elif 0<y100 and x1 == 0:	#In the case of integers a hundred and an integer of ten.
		return list_1[y100]+' hundred '+list_10[x10]
	elif 0<y100 and n<=19:		#In the case of an integer and the number of units.
		return list_1[y100]+' hundred '+list_1[n]
	elif 0<y100 and n>19 and x10<10: 	#In the case of Hundreds, Tens, and Units.
		return list_1[y100]+' hundred '+list_10[x10]+'-'+list_1[x1]
	elif n <= 19: 		#In the case of number of digits.
		return list_1[n]
	elif x1 == 0:		#Case of ten integers.
		return list_10[x10]
	elif n>19 and x10<10:
		return list_10[x10]+'-'+list_1[x1] 		#Case number 20-29.

def num_to_word(num):
	x1k,x100 = divmod(num,1000)
	x1m,x1k = divmod(x1k,1000)
	x1b,x1m = divmod(x1m,1000)
	num_100 = three_digits_to_word(x100)
	if x100 == 0:
		num_1k = three_digits_to_word(x1k)+' thousand' 	#Thousand integers.
	else:
		num_1k = three_digits_to_word(x1k)+' thousand '+ num_100 	#In the case of integers, but with a fraction.
	if x1k == 0 and x100 == 0:
		num_1m = three_digits_to_word(x1m)+' million' 	#Case of integer million.
	else:
		num_1m = three_digits_to_word(x1m)+' million '+ num_1k 		#In the case of integers, millions and fractions.
	if x1m == 0 and x1k == 0 and x100 == 0:
		num_1b = three_digits_to_word(x1b)+' billion' 	#Case of integers billion.
	else:
		num_1b = three_digits_to_word(x1b)+' billion '+ num_1m 		#Cases where an integer is a billion and a fraction.
	if 0 < num < 1000:  			#Cases less than 1000.
		return num_100
	elif 1000 <= num < 1000000: 	#More than 1000 but less than 1000000.
		return num_1k
	elif 1000000 <= num < 1000000000: 	#More than 1000000 but less than 1000000000.
		return num_1m
	elif 1000000000 <= num:  		#More than 1000000000.
		return num_1b
	else:							#Zero case.
		return 'zero'

def main():
	n = int(input()) 				#Enter number.
	print(three_digits_to_word(n))	#Print a word, read 3 digits.
	print(num_to_word(n))			#Print a word to read numbers less than 12 digits.

if __name__=='__main__':
	main()