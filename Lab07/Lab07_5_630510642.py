#630510642
#Wachiranan Phuangpanya
#section002
#Lab07_5

def rotate(num,pos):
    x = find_count(num)             #Substitute the created function in the variable.
    if pos >=0:                     #Positive case.
        for i in range(1,pos+1):
            r = num%10
            num2 = num//10
            num = (r*(10**(x-1)))+num2      #Take a variable that represents a function. To be used as an exponent in the formula.
        return num
    else:                           #Negative case.
        for i in range(1,abs(pos)+1):
            r = num%(10**(x-1))
            num2 = num//(10**(x-1))         #Take a variable that represents a function. To be used as an exponent in the formula.
            num = (r*10)+num2
        return num
        



def find_count(num):        #Function to find the number of digits of the entered number.
    count = 0
    while num !=0:
        num = num//10
        count += 1
    return count
        
        
            
def main():
    n = int(input())            #Enter the num value.
    p = int(input())            #Enter pos value.
    print(rotate(n,p))          #Show results.
        



if __name__=='__main__':
    main()
