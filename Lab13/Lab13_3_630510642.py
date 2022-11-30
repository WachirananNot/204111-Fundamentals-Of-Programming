#630510642
#Wachiranan Phuangpanya
#section002
#Lab13_3

import string
def word_count(text):
	text = text.lower()
	d = {}
	text = text.split()
	s = string.punctuation
	for i in text:
		text[text.index(i)] = i.strip(s)
	for i in text:
		d[i] = 0
	for j in text:
		if j in d:
			d[j]+= 1
	return d

	

def main():
	text = "He doesn't want to pay $40,000 for a new car, but his wife doesn't seem to care."
	print(word_count(text))


	

if __name__ =='__main__':
	main()