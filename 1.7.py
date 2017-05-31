#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     01/02/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#accepts 2 inputs and prints a table with the number of columns chosen by the user
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter another number between 0 and 1: "))
    n = eval(input("Enter amount of columns"))
    #how many times it will print - from learners choice.
    for i in range(n):
        x = 3.9 * (x - x * x)
        y = 3.9 * (y - y * y)
        #if number between 0 and 10 - 6d.p
        print("{0:10.6f} {0:10.6f}" .format(x, y))


main()

