#630510642
#Wachiranan Phuangpanya
#section002
#Lab02_5
F = (1+(5**(1/2)))/2                          #F is the equation to find the golden ratio constant.
n = float(input('Enter n: '))                 #Enter the number of terms used in the calculation.
Fn = (((F**n)/(5**(1/2)))+(1/2))//1         #Put the value of n in the formula to find the Fibonacci number.
print('fib(%d) = %d' %(n,Fn))               #Show calculation results.
