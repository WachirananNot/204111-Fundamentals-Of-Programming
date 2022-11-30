#630510642
#Wachiranan Phuangpanya
#section002
#Lab02_4
x = int(input('Input number of milliseconds: '))    #x is the value of milliseconds.
D = x//86400000                                     #Take the x to find the number of days.       
x2 = x-(D*86400000)                                 #x2 is the number of milliseconds left after finding the number of days.
H = x2//3600000                                     #H is the number of hours determined by using the value x2.
x3 = x2-(H*3600000)                                 #x3 is the number of milliseconds left after finding the number of hours. 
Mn = x3//60000                                       #Use x3 instead in the equation for the number of minutes.
x4 = x3-(Mn*60000)                                  #x4 is the number of milliseconds left after finding the number of minutes.
Ml = x4//1000                                       #Substitute the x4 value in the equation to find the number of seconds.
Mls = x4-(Ml*1000)                                  #Mls is the number of milliseconds remaining at the end.

print('Results = %s day(s), %s hour(s), %s minute(s), %s second(s), and %s millisec(s)' %(D,H,Mn,Ml,Mls))           #Show calculation results.
