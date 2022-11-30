#630510642
#Wachiranan Phuangpanya
#section002
#Lab12_1

import string
def sort_date(list_x):
	z = 0
	b = '/'
	for i in list_x:
		list_x[z] = i.split('/')
		z+= 1
	for i in list_x:
		for j in range(len(i)):
			i[j] = int(i[j])
	for i in list_x:
		i[0],i[2] = i[2],i[0]
		continue
	list_x.sort()
	for i in list_x:
		for j in range(len(i)):
			i[j] = str(i[j])
	for i in list_x:
		i[0],i[2] = i[2],i[0]
		continue
	for i in range(len(list_x)):
		list_x[i] = b.join(list_x[i])

def main():
	list_x = ['11/1/2100','5/12/1999','19/1/2003','11/9/2001']
	sort_date(list_x)
	print("---")
	print(list_x)

if __name__ =='__main__':
	main()