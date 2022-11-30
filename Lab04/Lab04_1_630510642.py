#630510642
#Wachiranan Phuangpanya
#section002
#Lab04_1

def love6(first,second):
    return (first == 6 or second == 6 or first+second == 6 or (first-second) == 6 or (second-first) == 6)
#Evaluates to true or false using the or command.

def main():
    f = int(input())                #Enter the first number value.
    s = int(input())                #Enter the second number value.
    print(love6(f,s))               #Show result values.
if __name__ == '__main__':
    main()
