#630510642
#Wachiranan Phuangpanya
#section002
#Lab05_4

def is_overlapped(l1,t1,w1,h1,l2,t2,w2,h2):
    if l1+w1 < l2 or t1+h1 < t2 or t2+h2 < t1 or l2+w2 < l1: #Compare points that do not overlap.
        return False
    else:                   #The rest of the cases will be if the squares overlap.
        return True

def main():
    L1 = int(input())               #Fill in the values.
    T1 = int(input())
    W1 = int(input())
    H1 = int(input())
    L2 = int(input())
    T2 = int(input())
    W2 = int(input())
    H2 = int(input())
    print(is_overlapped(L1,T1,T1,H1,L2,T2,W2,H2))  #Show results.
    
    

if __name__=='__main__':
    main()
