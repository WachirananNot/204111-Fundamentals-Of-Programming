#630510642
#Wachiranan Phuangpanya
#section002
#Lab13_2

def power_set(set_a):
	pw = [set()]
	for i in set_a:
		for s in pw:
			pw = pw +[list(s)+[i]]
	ps = [set(i) for i in pw]
	return ps





def main():
    a = {'1','2','3','4','5','6'}
    print(power_set(a))
if __name__=='__main__':
    main()