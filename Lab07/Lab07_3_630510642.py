#630510642
#Wachiranan Phuangpanya
#section002
#Lab07_3

def triangle(n):
    print('*')      #First line print
    print('*.*')    #Second line print
    dot(n)          #Call function.
    
        

def dot(n):
    x = '.'         #Substitutes the characters in the variable.
    z1 = '*'        #Substitutes the characters in the variable.
    z2 = ' '        #Substitutes the characters in the variable.
    z = z1+z2       #The variable to be used in the last line.
    for i in range(1,n-1):
        y = (2*i)+1     #The equation for the number of times each line is printed.
        d = x*y
        if i == n-2:
            p = (z*n)
            print(p)            #Type * on the last line.
        else:
            p = (d)
            print('*%s*'%(p))   #Type the dots on each other, starting with and ending with *.


def main():
    n = int(input())        #Fill in values.
    triangle(n)             #Call function.


if __name__=='__main__':
    main()
