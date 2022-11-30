#630510642
#Wachiranan Phuangpanya
#section002
#Lab12_3

def prime_factor(n):
	i = 2
	y = n
	prime = []
	if n == 1 or n == 0:
		return prime
	while i <= n**0.5:
		while n%i==0:
			if n != i:
				prime.append(i)
			else:
				break
			n = n/i
		i += 1
	if y == n:
		prime.append(y)
	else:
		prime.append(int(n))
	return prime
def coprime_factor(a,b):
	a2 = prime_factor(a)
	b2 = prime_factor(b)
	fu = []
	for i in a2:
		if i in b2:
			fu.append(i)
			b2.remove(i)
			continue
	return sorted(fu)

def main():
	a = int(input())
	b = int(input())
	print(coprime_factor(a,b))

if __name__ =='__main__':
	main()