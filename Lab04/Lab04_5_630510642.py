#630510642
#Wachiranan Phuangpanya
#section002
#Lab04_5

def nearest_odd(x):
    if x>=0:                    #In the event that x is greater than or equal to 0.
        if int(x)%2==0: 
            return int(x)+1     #If x is divided by 2, then there remain remainder 0 Return the integer value x + 1.
        if int(x)%2==1:
            return int(x)       #If x is divided by 1, then there remain remainder 0 Return the integer value x.
    else:                       #Case x is less than 0.
        if abs((x)%2)==0:
            return int(x)+1     #If the absolute value of x divided by 2, then get the numerator equal to 0 Return the whole number x + 1.
        elif int(x)%2 ==0:
            return int(x)-1     #If the integer value of x divided 2 and get the numerator equal to 0 Return the whole number x-1.
        else:
            return int(x)       #In addition to all cases Return an integer x.
def main():
    x = float(input())          #Enter x.
    print(nearest_odd(x))       #Show result values
    main()
if __name__=='__main__':
    main()
        

