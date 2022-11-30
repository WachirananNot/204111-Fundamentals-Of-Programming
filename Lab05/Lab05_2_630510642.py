#630510642
#Wachiranan Phuangpanya
#section002
#Lab05_2

def is_p_triple(a,b,c):
    if ((a**2)+(b**2)) == c**2: 
        return True                 #If c is hypotenuse.
    elif ((c**2)+(b**2)) == a**2:
        return True                 #If a is hypotenuse.
    elif ((c**2)+(a**2)) == b**2:
        return True                 #If c is hypotenuse.
    else:
        return False                #If not a right triangle.

def main():
    x=int(input())                  #Fill in the values.
    y=int(input())
    z=int(input())
    print(is_p_triple(x,y,z))       #Show results.
    

if __name__=='__main__':
    main()
