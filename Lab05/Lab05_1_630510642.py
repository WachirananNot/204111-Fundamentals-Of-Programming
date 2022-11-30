#630510642
#Wachiranan Phuangpanya
#section002
#Lab05_1

def euclid_dis(x1,y1,x2,y2):
    return (((x1-x2)**2)+((y1-y2)**2))**0.5  #Formula for distance between radius.

def circle_intersect(x1,y1,r1,x2,y2,r2,epsilon=10**-6):
    dis_circle = euclid_dis(x1,y1,x2,y2)
    if abs((dis_circle-abs(r1+r2))) < epsilon or abs(dis_circle-abs(r1-r2))< epsilon:
        return 0                        #If the circles touch each other.
    elif abs(r1-r2)<dis_circle<r1+r2:
        return 1                        #In case of contrasting circles.
    else:
        return -1                       #In the case of circles that do not intersect.
def main():
    x1 = float(input())                 #Fill in the values.
    y1 = float(input())
    r1 = float(input())
    x2 = float(input())
    y2 = float(input())
    r2 = float(input())
    print(circle_intersect(x1,y1,r1,x2,y2,r2))    #Show results.
    
    
    

if __name__=='__main__':
    main()
