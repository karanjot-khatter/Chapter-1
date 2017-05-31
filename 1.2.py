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

#enter and run chaos function as described from section 1.6
def main():
    print("chaos function")
    x = eval(input("Number inbetween 3 and 4"))
    for i in range (10):
        x= 3.9 * x * (4 - x)
        print(x)
main()