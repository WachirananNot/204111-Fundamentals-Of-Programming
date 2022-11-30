#630510642
#Wachiranan Phuangpanya
#section002
#Lab07_4

def life_path(n):
    sum_ = 0     #The variable holds the value from the first combination.
    sum_2 = 0    #The variable holds the value from the second combination.
    sum_3 = 0    #The variable holds the value from the last combination.
    while n != 0:
        r1 = n%10
        sum_ += r1          #Add each digit of the number together.
        n = n//10 
    if sum_ >= 10:          #If the total is greater than 10 Need to add new numbers again.
        while sum_ != 0:
            r2 = sum_%10
            sum_2 += r2
            sum_ = sum_//10
        if sum_2 >= 10:        #If the total is greater than 10 Need to add new numbers again.
            while sum_2 != 0:
                r3 = sum_2%10
                sum_3 += r3
                sum_2 = sum_2//10
            return sum_3        #Returns the sum of a single digit.
        else:
            return sum_2        #Returns the sum of a single digit.
    else:
        return sum_             #Returns the sum of a single digit.
            
def main():
    n = int(input())            #Enter n values.
    print(life_path(n))         #Show results.
        



if __name__=='__main__':
    main()
