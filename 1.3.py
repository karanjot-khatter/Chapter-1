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
#2 different types of input
def main():
    x = eval(input("Number inbetween 1 and 2"))
    y = eval(input("Number bween 1 and 2"))
    for i in range (10):
        x= 3.9 * x * (1 - x)
        y= 3.9 * y * (1 - y)
        print(x)
        print(y)
main()