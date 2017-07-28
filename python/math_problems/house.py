#! /usr/bin/env python3

def main():
   checker() 

def sum(n):
    return (n*(n+1))/2

def checker():
    for number_of_houses in range(50, 500):
        for house_number in range(1, number_of_houses):
            left = sum(house_number - 1)
            right = sum(number_of_houses) - sum(house_number)
            if left == right:
                print('the house number is %d' % (house_number))
                print('the number of houses is %d' % (number_of_houses))

main()
