#630510642
#Wachiranan Phuangpanya
#section002
#Lab06_1

def int_power(x,y):
    if y == 0:              #If the exponent is zero.
        return 1
    elif y > 0:             #If the exponent is greater than zero.
        result = 1
        base = x
        for i in range(1,y+1):   #x times x by the number of y-values.
            result = result*base
        return result
    else:                   #If the exponent is less than zero
        result = 1
        base = 1/x              #The exponent must be positive by converting x to one over x.
        for i in range(1,abs(y)+1):
            result = result*base
        return result
            

def main():
    x = float(input())              #Enter the base number.
    y = int(input())                #Enter the exponent.
    print(int_power(x,y))           #Show results.

if __name__ == '__main__':
    main()
