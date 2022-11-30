#630510642
#Wachiranan Phuangpanya
#section002
#Lab05_3

def year_athi(y):                   #A function to find a leap year.
    if y % 4 == 0:
        if y % 400 == 0:
            return 1                #1 = True1
        elif y % 100 == 0:
            return 0                #0 = False
        else:
            return 1
    elif y % 4 == 1:
        return 0
    elif y % 4 == 2:
        return 0
    elif y % 4 == 3:
        if (y+1)%4 ==0:
            if (y+1)%400 == 0:
                return 2            #2 = True2
            elif (y+1)%100 == 0:
                return 0
            else:
                return 2
        else:
            return 0
    
def count_down_to_songkran(d,m,y):
    if year_athi(y) == 1:               #Find the number of days in a leap year.
        if d == 13 and m == 4:
            return 0
        elif m < 4:
            if m == 1:
                return (31-d)+(29+31+13)
            if m == 2:
                return (29-d)+(31+13)
            if m == 3:
                return (31-d)+(13)
        elif m>=4:
            if m == 4:
                if d>13:
                    return (30-d)+(31+30+31+31+30+31+30+31+31+28+31+13)
                elif d<13:
                    return (13-d)
            if m == 5:
                return (31-d)+(30+31+31+30+31+30+31+31+28+31+13)
            if m == 6:
                return (30-d)+(31+31+30+31+30+31+31+28+31+13)
            if m == 7:
                return (31-d)+(31+30+31+30+31+31+28+31+13)
            if m == 8:
                return (31-d)+(30+31+30+31+31+28+31+13)
            if m == 9:
                return (30-d)+(31+30+31+31+28+31+13)
            if m == 10:
                return (31-d)+(30+31+31+28+31+13)
            if m == 11:
                return (30-d)+(31+31+28+31+13)
            if m == 12:
                return (31-d)+(31+28+31+13)
    elif year_athi(y) == 2:                 #Find the number of days in the year in which the next year is a leap year.
        if d == 13 and m == 4:
            return 0
        elif m < 4:
            if m == 1:
                return (31-d)+(28+31+13)
            if m == 2:
                return (28-d)+(31+13)
            if m == 3:
                return (31-d)+(13)
        elif m>=4:
            if m == 4:
                if d>13:
                    return (30-d)+(31+30+31+31+30+31+30+31+31+29+31+13)
                elif d<13:
                    return (13-d)
            if m == 5:
                return (31-d)+(30+31+31+30+31+30+31+31+29+31+13)
            if m == 6:
                return (30-d)+(31+31+30+31+30+31+31+29+31+13)
            if m == 7:
                return (31-d)+(31+30+31+30+31+31+29+31+13)
            if m == 8:
                return (31-d)+(30+31+30+31+31+29+31+13)
            if m == 9:
                return (30-d)+(31+30+31+31+29+31+13)
            if m == 10:
                return (31-d)+(30+31+31+29+31+13)
            if m == 11:
                return (30-d)+(31+31+29+31+13)
            if m == 12:
                return (31-d)+(31+29+31+13)
    else:                               #Find the number of days in a year that is not a leap year.
        if d == 13 and m == 4:
            return 0
        elif m < 4:
            if m == 1:
                return (31-d)+(28+31+13)
            if m == 2:
                return (28-d)+(31+13)
            if m == 3:
                return (31-d)+(13)
        elif m>=4:
            if m == 4:
                if d>13:
                    return (30-d)+(31+30+31+31+30+31+30+31+31+28+31+13)
                elif d<13:
                    return (13-d)
            if m == 5:
                return (31-d)+(30+31+31+30+31+30+31+31+28+31+13)
            if m == 6:
                return (30-d)+(31+31+30+31+30+31+31+28+31+13)
            if m == 7:
                return (31-d)+(31+30+31+30+31+31+28+31+13)
            if m == 8:
                return (31-d)+(30+31+30+31+31+28+31+13)
            if m == 9:
                return (30-d)+(31+30+31+31+28+31+13)
            if m == 10:
                return (31-d)+(30+31+31+28+31+13)
            if m == 11:
                return (30-d)+(31+31+28+31+13)
            if m == 12:
                return (31-d)+(31+28+31+13)
            
    
def main():
    x = int(input())                #Fill in the values.
    y = int(input())
    z = int(input())
    print(count_down_to_songkran(x,y,z))    #Show results.


if __name__=='__main__':
    main()
