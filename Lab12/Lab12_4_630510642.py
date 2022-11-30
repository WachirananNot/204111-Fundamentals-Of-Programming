#630510642
#Wachiranan Phuangpanya
#section002
#Lab12_4

import string
import copy
def polynomial_addition(p1,p2):
	pc1 = sorted(p1,reverse=True)
	pc2 = sorted(p2,reverse=True)
	pc_1 = copy.deepcopy(pc1)
	pr = []
	for i in range(len(pc1)):
		for j in range(len(pc2)):
			if pc1[i][0] == pc2[j][0]:
				if pc1[i][1] + pc2[j][1] == 0:
					del pc2[j]
					pc_1[i] = []
					break
				else:
					pr.append((pc1[i][0],pc1[i][1]+pc2[j][1]))
					del pc2[j]
					pc_1[i] = []
					break
			else:
				continue
	for i in pc_1:
		if i != []:
			pr.append(i)
	for j in pc2:
		if j != []:
			pr.append(j)
	return sorted(pr,reverse=True)





def main():
	p1 = [(2, 6), (1, 34), (0, -8)]
	p2 = [(2, -6), (0, 2), (1, 1)]
	x = polynomial_addition(p1,p2)
	# print(p1)
	# print(p2)
	print(x)

if __name__ =='__main__':
	main()