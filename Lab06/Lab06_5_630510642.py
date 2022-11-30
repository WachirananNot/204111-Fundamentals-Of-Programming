#630510642
#Wachiranan Phuangpanya
#section002
#Lab06_5

def longest_digit_run(n):
    count = 1            #Variable stores adjacent numbers.
    max_ = 1             #The variable holds the maximum value.
    while n != 0:
        r = n%10         #Find the last digit.
        r2 = (n//10)%10  #Find the next digit
        if r2 == r:      #Compare two digit numbers
            count +=1    #If the same, update the value

        if r2 != r:     #If not the same, reset the value.
            count = 1

        n = n//10       #Update n values
        if max_<count:  #Compare the value to find the numbers that are most contiguous
            max_ = count
        elif max_ > count:  #Compare the value to find the numbers that are most contiguous
            max_ = max_


    return max_         #Return max value.


def main():
    x = int(input())    #Enter the x value.
    print(longest_digit_run(x))     #Show result value.


    
    
if __name__ == '__main__':
    main()
