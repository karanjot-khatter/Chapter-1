#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     02/02/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#modify chaos program so it prints 20 values instead of 10
def main():
    x = eval(input("Enter a number between 1+2"))
    for i in range(20):
        x= 3.9 * x * (1-x)
        print(x)

    main()
