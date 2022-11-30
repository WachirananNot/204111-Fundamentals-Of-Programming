#630510642
#Wachiranan Phuangpanya
#section002
#Lab04_2

def my_max_mid_min(a,b,c):
    if a > b:               #Find the max and min values ​​from case a greater than b.
        max_= a
        min_= b
    else:                   #Find the max and min values ​​from case b greater than a.
        max_= b
        min_= a
    if c > max_:            #The value of c if greater than max.
        max_= c
    if c < min_:            #The value of c if the value is less than min.
        min_= c
    full = a+b+c            #Find the sum of all values.
    mid_=full-(max_+min_)   #Find the mid value from the difference between the sum and the max and min combined.
    print('max =',max_,)
    print('mid =',mid_,)
    print('min =',min_,)    #Show result values

def main():
    x=int(input())          #Enter a value.
    y=int(input())          #Enter b value.
    z=int(input())          #Enter c value.

    my_max_mid_min(x,y,z)   #Show result values


if __name__ == '__main__':
    main()
        

