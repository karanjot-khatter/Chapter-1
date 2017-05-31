#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     03/04/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def noLoop():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1:"))
    x = 3.9 * x * (1-x)
    print (x)
    x = 3.9 * x * (1-x)
    print (x)
    x = 3.9 * x * (1-x)
    print (x)

noLoop()