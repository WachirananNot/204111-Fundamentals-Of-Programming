#630510642
#Wachiranan Phuangpanya
#section002
#Lab08_2

import string
def is_palindrome(x,b):
    full = 0                #Create a variable.
    i = 0                   #Create a variable.
    while x!=0:             #Base conversion loop.
        r = x%b
        full += r*(10**i)
        i+=1
        x=x//b
    s_full = str(abs(full))     #Convert int to str.
    mid_ = len(s_full)//2       #Find the middle point of the text.
    if len(s_full)%2 ==1:       #If the character length is odd.
        if s_full[:mid_] == (s_full[mid_+1:])[::-1]:
            return True
        else:
            return False
    else:                       #If the character length is an even number.
        if s_full[:mid_] == (s_full[mid_:])[::-1]:
            return True
        else:
            return False
def main():
    x = int(input())            #Enter number.
    y = int(input())            #Enter base number.
    print(is_palindrome(x,y))   #Print function.

if __name__ == '__main__':
    main()