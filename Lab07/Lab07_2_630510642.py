#630510642
#Wachiranan Phuangpanya
#section002
#Lab07_2

def digit_count(x,base = 10):
    count = 1                 #Storage variable.
    while abs(x)//base != 0:  #Divide until 0 is left.
        count+=1
        x = abs(x)//base  #This is a loop to divide x by the base value. And then add the number of times to divide in the storage variable.
    return count

def test_digit_count():         #Input validation function.
    assert(digit_count(258) == 3)       #Check without entering the base value. Will use the base = 10 instead.
    assert(digit_count(258,2) == 9)     #Check by filling in base = 2 Will make the number count to be 9.
            




def main():
    x = int(input())            #Enter the x value.
    y = int(input())            #Enter the base value.
    print(digit_count(x,y))     #Show results.
    test_digit_count()          #Run the input validation function.
   

if __name__=='__main__':
    main()
