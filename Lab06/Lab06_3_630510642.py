#630510642
#Wachiranan Phuangpanya
#section002
#Lab06_3

def factorize(x):
    i = 2               #Starting factor.
    y = x               #Keep the initial x.
    print(x,'is',end=' ')
    while i <= x**0.5:  #If the factor is not greater than the square root of x, the loop will still work.
        while x%i==0:   #If x is divisible by the i-value. The loop will still work.
            if x != i:  #If x is not equal to i.
                print(i,end=' * ')  #Print the i * value.
            else:       #If x is equal to i.
                break   #Loop stops working.
            x = x/i     #Change the x-value by dividing the i-value.
        i += 1          #The i value is increased by 1 per loop.
    if y == x:          #If the initial x is equal to the x after exiting the loop Concluded that it was a prime number.
        print("prime")
    else:               #If not, print the last x value.
        print(int(x))

def main():
    x = int(input())    #Fill in values
    factorize(x)        #Call function


if __name__ == '__main__':
    main()
