#630510642
#Wachiranan Phuangpanya
#section002
#Lab04_3

def calculate_p2p_evolve_exp(p,c):
    if p==1 and c>=12:
        exp = 500
        return exp                          #In the case of p = 1 exp, the maximum is only 500.
    elif p>1:                               #If p> 1, it can be divided into 2 cases.
        if c//11>=p:
            exp = 500*p                     #In the case of c // 12, the value is greater than or equal to 12.
        else: #c//12<p
            exp=((c+(p-2))//11)*500
        return exp                          #Cases other than this will find the exp value from the formula.
    else:
        exp = 0
        return exp                          #In addition to all cases, exp is equal to 0.
def main():
    x = int(input())                        #Fill out the bird value.
    y = int(input())                        #Fill up candy.
    print(calculate_p2p_evolve_exp(x,y))    #Show result values.
    


if __name__=='__main__':
    main()
          
#1 12,2 11,2 22,3 11