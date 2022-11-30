#630510642
#Wachiranan Phuangpanya
#section002
#Lab05_5

def zodiac_element(year):
    if year%10 == 0 or year%10 == 1:    #In the case of Metal years.
        if year%12 == 0:                #The year of the zodiac is sorted by the remainder.
            return 'Metal Monkey'
        elif year%12 == 1:
            return 'Metal Rooster'
        elif year%12 == 2:
            return 'Metal Dog'
        elif year%12 == 3:
            return 'Metal Pig'
        elif year%12 == 4:
            return 'Metal Rat'
        elif year%12 == 5:
            return 'Metal Ox'
        elif year%12 == 6:
            return 'Metal Tiger'
        elif year%12 == 7:
            return 'Metal Rabbit'
        elif year%12 == 8:
            return 'Metal Dragon'
        elif year%12 == 9:
            return 'Metal Snake'
        elif year%12 == 10:
            return 'Metal Horse'
        elif year%12 == 11:
            return 'Metal Goat'
    elif year%10 == 2 or year%10 == 3:  #In the case of Water years.
        if year%12 == 0:                #The year of the zodiac is sorted by the remainder.
            return 'Water Monkey'
        elif year%12 == 1:
            return 'Water Rooster'
        elif year%12 == 2:
            return 'Water Dog'
        elif year%12 == 3:
            return 'Water Pig'
        elif year%12 == 4:
            return 'Water Rat'
        elif year%12 == 5:
            return 'Water Ox'
        elif year%12 == 6:
            return 'Water Tiger'
        elif year%12 == 7:
            return 'Water Rabbit'
        elif year%12 == 8:
            return 'Water Dragon'
        elif year%12 == 9:
            return 'Water Snake'
        elif year%12 == 10:
            return 'Water Horse'
        elif year%12 == 11:
            return 'Water Goat'
    elif year%10 == 4 or year%10 == 5:  #In the case of Wood years.
        if year%12 == 0:                #The year of the zodiac is sorted by the remainder.
            return 'Wood Monkey'
        elif year%12 == 1:
            return 'Wood Rooster'
        elif year%12 == 2:
            return 'Wood Dog'
        elif year%12 == 3:
            return 'Wood Pig'
        elif year%12 == 4:
            return 'Wood Rat'
        elif year%12 == 5:
            return 'Wood Ox'
        elif year%12 == 6:
            return 'Wood Tiger'
        elif year%12 == 7:
            return 'Wood Rabbit'
        elif year%12 == 8:
            return 'Wood Dragon'
        elif year%12 == 9:
            return 'Wood Snake'
        elif year%12 == 10:
            return 'Wood Horse'
        elif year%12 == 11:
            return 'Wood Goat'
    elif year%10 == 6 or year%10 == 7:  #In the case of Fire years.
        if year%12 == 0:                #The year of the zodiac is sorted by the remainder.
            return 'Fire Monkey'
        elif year%12 == 1:
            return 'Fire Rooster'
        elif year%12 == 2:
            return 'Fire Dog'
        elif year%12 == 3:
            return 'Fire Pig'
        elif year%12 == 4:
            return 'Fire Rat'
        elif year%12 == 5:
            return 'Fire Ox'
        elif year%12 == 6:
            return 'Fire Tiger'
        elif year%12 == 7:
            return 'Fire Rabbit'
        elif year%12 == 8:
            return 'Fire Dragon'
        elif year%12 == 9:
            return 'Fire Snake'
        elif year%12 == 10:
            return 'Fire Horse'
        elif year%12 == 11:
            return 'Fire Goat'
    elif year%10 == 8 or year%10 == 9:  #In the case of Earth years.
        if year%12 == 0:                #The year of the zodiac is sorted by the remainder.
            return 'Earth Monkey'
        elif year%12 == 1:
            return 'Earth Rooster'
        elif year%12 == 2:
            return 'Earth Dog'
        elif year%12 == 3:
            return 'Earth Pig'
        elif year%12 == 4:
            return 'Earth Rat'
        elif year%12 == 5:
            return 'Earth Ox'
        elif year%12 == 6:
            return 'Earth Tiger'
        elif year%12 == 7:
            return 'Earth Rabbit'
        elif year%12 == 8:
            return 'Earth Dragon'
        elif year%12 == 9:
            return 'Earth Snake'
        elif year%12 == 10:
            return 'Earth Horse'
        elif year%12 == 11:
            return 'Earth Goat'
def main():
    x = int(input())                #Enter the year.
    print(zodiac_element(x))        #Show results.
        
    
    

if __name__=='__main__':
    main()
