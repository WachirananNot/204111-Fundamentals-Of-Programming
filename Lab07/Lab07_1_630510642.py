#630510642
#Wachiranan Phuangpanya
#section002
#Lab07_1

def sum_prime_in_range(x,y):
    sum_ = 0                #storage variable.
    for i in range(x,y+1):
        if factorize(i) == i:
            sum_ += i       #If i is a prime number, i will be added to the storage variable.
        else:
            sum_ = sum_     #If i is not prime, do not add additional variables.
    return sum_
def factorize(x):           #The find function to find a prime number and return it.
    i = 2
    z = x
    for i in range(2,int(x**0.5)+1):
        while x%i==0:
            if x == i:
                break
            x = x/i
    if z == x:
        return x



def main():
    x = int(input())    #Enter the scope of the prime number to add.
    y = int(input())    #Enter the scope of the prime number to add.
    print(sum_prime_in_range(x,y))      #Show results.


if __name__=='__main__':
    main()
