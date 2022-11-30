#630510642
#Wachiranan Phuangpanya
#section002
#Lab06_4

def calculate_score():
    y = int(input('Total students: '))  
    max_ = 0    #The variable holds the maximum value.
    min_ = 0    #The variable holds the next largest value.
    full = 0
    print('Enter score:')
    for i in range(1,y+1): #The loop runs by the number of students.
        x = int(input())   #Fill in the score value.
        full += x           #Update totals.
        if max_<x:          #The condition compares the maximum to the x-value.
            min_=max_
            max_= x
        elif max_>x:        #The condition compares the maximum to the x-value.
            if min_<x:      #Conditions for comparing the next larger value to the x-value.
                min_= x
            # elif min_>x:    #Conditions for comparing the next larger value to the x-value.
            #     min_=min_
            # max_= max_

    print('---')
    print('Max score is: %.2f'%(max_))      #Print the max value.
    if min_== max_ or min_== 0:
        print('Runner up is: None')         #If the runner up value will be none.
    elif min_< max_:
        print('Runner up is: %.2f'%(min_))  #Print the runner up value.
    aver = full/y
    print('Average is: %.2f'%(aver))        #Print average.


def main():
        #Enter the number of students.
    calculate_score()                        #Call function.
    
    
if __name__ == '__main__':
    main()
