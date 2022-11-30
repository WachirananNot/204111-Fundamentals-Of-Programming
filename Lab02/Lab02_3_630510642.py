#630510642
#Wachiranan Phuangpanya
#section002
#Lab02_3
print('First Equation')                         #Various values ​​in the first equation.                       
m1 = float(input('Input m1: '))                 #Add m1, where m1 is slope.
b1 = float(input('Input b1: '))                 #Add b1, where b1 is the y-intercept.
print('Second Equation')                        #Various values ​​in the second equation.
m2 = float(input('Input m2: '))                 #Add m2, where m2 is not equal to m1.
b2 = float(input('Input b2: '))                 #Add b2, where b2 is the y-intercept.
x = (b2-b1)/(m1-m2)                             #Reformatting the equation for x.
y = (((m1+m2)*x)+(b1+b2))/2                     #Take the value of x to format the equation to find y.
print('The point of intersection is at x = %.2f and y = %.2f' %(x,y))       #Substitute the value and get the answer as x and y values.
