#630510642
#Wachiranan Phuangpanya
#section002
#Lab04_4

def round_to_int(x):
    if x>=0:                            #In the case of x is greater than or equal to 0.
        if x-(int(x))<0.5:
            return int(x)               #If the decimal number of the value x is less than 0.5, it is rounded down.
        else:
            return int(x)+1             #If the decimal number of the x value is greater than 0.5, it will be rounded up.
    else:                               #Case x is less than 0
        if (abs(x-(int(x)))<0.5):
            return int(x)               #If the absolute value of the decimal number x is less than 0.5, round down.
        else:
            return (-(abs(int(x))+1))   #If the absolute value of the decimal number x is greater than 0.5, round up.
def main():
    x = float(input())                  #Enter x.
    print(round_to_int(x))              #Show result values.
    

if __name__=='__main__':
    main()
