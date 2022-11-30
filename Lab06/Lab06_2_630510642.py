#630510642
#Wachiranan Phuangpanya
#section002
#Lab06_2

def int_to_bin(x):
    if x>=0:                        #In case of positive integers.
        base = x//1
        result = 0
        i = 0
        while base > 0:             #Looping by dividing two Then reorder the numerator numbers.
            r = base%2
            result += r*(10**i)
            base = base//2
            i += 1
        return result
    else:                           #In the case of negative integers.
        base = abs(x)//1
        result = 0
        i = 0
        while base > 0:             #Looping by dividing two Then reorder the numerator numbers.
            r = base%2
            result += r*(10**i)
            base = base//2
            i += 1
        return -(result)
def float_(x):
    if x>=0:                        #In case of positive decimal numbers.
        base = x%1
        result = 0
        r = base*2
        r2 = r//1
        for i in range(1,7):        #Looping by multiplying the decimal by two If more than one, then reorder 1 and 0.
            result = result +(r2*(10**(-i)))
            r = (r-r2)*2
            r2 = r//1
        return result
    else:                            #In case of negative decimal numbers.
        base = abs(x)%1
        result = 0
        r = base*2
        r2 = r//1
        for i in range(1,7):        #Looping by multiplying the decimal by two If more than one, then reorder 1 and 0.
            result = result +(r2*(10**(-i)))
            r = (r-r2)*2
            r2 = r//1
        return -(result)
    
def float_to_bin(x):                #Functions that combine 2 functions.
    return (int_to_bin(x)+float_(x))

def main():
    x = float(input())              #Fill in values.
    print('%.6f'%(float_to_bin(x)))  #Print to 6 decimal places.
    
if __name__ == '__main__':
    main()
