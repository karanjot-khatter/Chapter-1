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
#similar to 1.5
def main():
    n = eval(input("how many numbers should i print"))
    x = eval(input("Choose a number between 1 + 2"))
    for i in range(n):
         x= 3.9 * x * (1 - x)
         print (x)

main()