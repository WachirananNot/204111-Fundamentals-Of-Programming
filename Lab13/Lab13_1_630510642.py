#630510642
#Wachiranan Phuangpanya
#section002
#Lab13_1


def count_segment(list_a):
	q1 = 0
	q2 = 0
	q3 = 0
	q4 = 0

	for i in list_a:
		x = i[0]
		y = i[1]
		r = i[2]
		ra = ((x**2)+(y**2))**0.5
		if x>0 and y>0:
			q1 +=1
			if ra < r:
				q3 += 1
			if x - r < 0:
				q2 += 1
			if y - r < 0:
				q4 += 1
		elif x<0 and y>0:
			q2 += 1
			if ra < r:
				q4 += 1
			if abs(x) - r < 0:
				q1 += 1
			if y - r < 0:
				q3 += 1
		elif x<0 and y<0:
			q3 += 1
			if ra < r:
				q1 += 1
			if abs(x) - r < 0:
				q4 += 1
			if abs(y) - r < 0:
				q2 += 1
		elif x>0 and y<0:
			q4 += 1
			if ra < r:
				q2 += 1
			if x - r < 0:
				q3 += 1
			if abs(y) - r < 0:
				q1 += 1
		elif x == 0 and y>0:
			q1 += 1
			q2 += 1
			if y - r < 0:
				q3 += 1
				q4 += 1
		elif x == 0 and y < 0:
			q3 += 1
			q4 += 1
			if abs(y) - r < 0:
				q1 += 1
				q2 += 1
		elif y == 0 and x > 0:
			q1 += 1
			q4 += 1
			if x - r < 0:
				q2 += 1
				q3 += 1
		elif y == 0 and x < 0:
			q2 += 1
			q3 += 1
			if abs(x) - r < 0:
				q1 += 1
				q4 += 1
		elif x==0 and y==0 and r>0:
			q1 += 1
			q2 += 1
			q3 += 1
			q4 += 1
		else:
			continue
	return (q1,q2,q3,q4)



def main():
	list_a = [(2, 7, 1.5),(3.2, 2.5, 4.06),(-5.5, -4.5, 2.5),(2, -5.2, 3),(7.2, -2.8, 1.2)]
	print(count_segment([(0,0,1)]))


	

if __name__ =='__main__':
	main()